#!/usr/bin/env python3
"""Universal chunk splitter for extracted SukaSuka/SukaMoca Markdown volumes (v1.2).

Учитывает ~35% накладных расходов на фуригану 〔...〕 и маркеры [[EPUB_IMAGE:...]].
- Вариант А (Стандартный): 1-2 подраздела в чанке (целевой размер 7 500 - 14 000 сырых знаков / 5 000 - 9 500 чистых).
- Вариант Б (Экономный): 2-3 подраздела в чанке (целевой размер 13 000 - 20 200 сырых знаков / 9 000 - 13 500 чистых),
  с умной балансировкой без мелких огрызков (< 9 000) и без лишних разрывов глав.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

# 1. Универсальный паттерн разделителя сцен для всех томов
SCENE_BREAK_RE = re.compile(
    r"(?:\n\n\[пауза\]\n\n)?\n\n"
    r"(?:\[\[EPUB_IMAGE:[^\n]*gaiji[^\n]*\]\]|†|\*\s*\*\s*\*|＊＊＊)"
    r"(?:\n\n\[пауза\])?(?=\n\n)"
)

# 2. Паттерн буквального маркера [пауза]
PAUSE_BREAK_RE = re.compile(r"\n\n\[пауза\](?=\n\n)")

# 3. Страховочный паттерн обычного абзаца
PARAGRAPH_BREAK_RE = re.compile(r"\n\n(?=(?!\[пауза\])[^\n])")


def pure_jp_len(text: str) -> int:
    """Длина текста после удаления фуриганы, маркеров картинок, [пауза] и простых em-тегов."""
    cleaned = re.sub(r"〔[^〕]*〕|⟦[^⟧]*⟧", "", text)
    cleaned = re.sub(r"\[\[EPUB_IMAGE:[^\]]*\]\]|\[пауза\]|</?em>", "", cleaned)
    cleaned = re.sub(r"^#{1,6}\s+", "", cleaned, flags=re.M)
    return len(cleaned.strip())


def strip_wrappers(text: str, keep_colophon: bool = False) -> tuple[str, str]:
    """Отделяет техническую шапку и по умолчанию удаляет конечный издательский колофон 奥付."""
    toc_end = re.search(r"<!--[^\n]*p-toc-[^\n]*-->\s*\n\n", text)
    if toc_end:
        idx = toc_end.end()
        front, body = text[:idx].strip(), text[idx:].strip()
    else:
        first_h2 = re.search(r"^##\s+", text, flags=re.M)
        if first_h2:
            idx = first_h2.start()
            front, body = text[:idx].strip(), text[idx:].strip()
        else:
            front, body = "", text.strip()

    if not keep_colophon:
        # Отсекаем только отдельный заголовок 奥付, если после него нет других Markdown-заголовков.
        # Поэтому упоминание 奥付 в прозе или нетерминальный заголовок не удаляет последующий текст.
        colophon_match = re.search(r"(?m)^##[ \t]+奥付[ \t]*$", body)
        if colophon_match and not re.search(r"(?m)^#{1,6}[ \t]+", body[colophon_match.end():]):
            body = body[:colophon_match.start()].rstrip()
        elif not colophon_match:
            # Совместимость со старым форматом выходных данных, где кредит был отдельной строкой.
            credit_match = re.search(r"(?m)^本作品のイラストは[^\n]*$", body)
            if credit_match and not re.search(r"(?m)^#{1,6}[ \t]+", body[credit_match.end():]):
                body = body[:credit_match.start()].rstrip()

    return front, body


def split_into_sections(body: str) -> list[str]:
    """Делит книгу по заголовкам ## и ###, приклеивая короткие титулы ## к ### 1."""
    raw_parts = re.split(r"(?m)(?=^#{2,3}\s+)", body)
    sections: list[str] = []
    pending_h2 = ""

    for part in raw_parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith("## ") and len(part) < 400:
            pending_h2 = f"{pending_h2}\n\n{part}".strip() if pending_h2 else part
        else:
            if pending_h2:
                part = f"{pending_h2}\n\n{part}"
                pending_h2 = ""
            sections.append(part)

    if pending_h2:
        if sections:
            sections[-1] = f"{sections[-1]}\n\n{pending_h2}"
        else:
            sections.append(pending_h2)

    return sections


def split_section_balanced(text: str, pattern: re.Pattern, max_chars: int) -> list[str]:
    """Делит крупный блок по разделителям на максимально равные части (без мелких хвостов)."""
    matches = list(pattern.finditer(text))
    if not matches:
        return [text]

    cut_points = [0] + [m.start() for m in matches] + [len(text)]
    pieces = [
        text[cut_points[i] : cut_points[i + 1]].strip()
        for i in range(len(cut_points) - 1)
        if text[cut_points[i] : cut_points[i + 1]].strip()
    ]

    num_parts = max(1, (len(text) + max_chars - 1) // max_chars)
    target_size = len(text) / num_parts

    grouped: list[str] = []
    current = ""
    for piece in pieces:
        candidate = f"{current}\n\n{piece}" if current else piece
        if not current:
            current = piece
            continue
        # Если добавление куска превышает max_chars ИЛИ мы уже набрали ближе к target_size
        if len(candidate) > max_chars or (
            len(grouped) < num_parts - 1
            and abs(len(current) - target_size) < abs(len(candidate) - target_size)
            and len(current) >= target_size * 0.65
        ):
            grouped.append(current)
            current = piece
        else:
            current = candidate

    if current:
        if grouped and len(current) < 3500 and len(grouped[-1]) + len(current) + 2 <= max_chars + 2000:
            grouped[-1] = f"{grouped[-1]}\n\n{current}"
        else:
            grouped.append(current)

    return grouped


def split_oversized_block(block: str, max_chars: int) -> list[str]:
    """Каскадно и сбалансированно дробит слишком длинный блок: по сценам -> по [пауза] -> по абзацам."""
    if len(block) <= max_chars:
        return [block]

    by_scenes = split_section_balanced(block, SCENE_BREAK_RE, max_chars)
    by_pauses: list[str] = []
    for piece in by_scenes:
        if len(piece) <= max_chars:
            by_pauses.append(piece)
        else:
            by_pauses.extend(split_section_balanced(piece, PAUSE_BREAK_RE, max_chars))

    final_pieces: list[str] = []
    for piece in by_pauses:
        if len(piece) <= max_chars:
            final_pieces.append(piece)
        else:
            final_pieces.extend(split_section_balanced(piece, PARAGRAPH_BREAK_RE, max_chars))

    return final_pieces


def pack_blocks_smart(blocks: list[str], max_chars: int, min_chunk: int) -> list[str]:
    """Упаковывает блоки в чанки до max_chars и устраняет мелкие одиночные чанки (< min_chunk)."""
    chunks: list[str] = []
    current = ""
    for b in blocks:
        candidate = f"{current}\n\n{b}" if current else b
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = b
    if current:
        chunks.append(current)

    # Пост-проход: если какой-то чанк остался слишком маленьким (< min_chunk),
    # пробуем объединить его с меньшим из соседей (с допуском +12% к max_chars)
    soft_cap = int(max_chars * 1.12)
    i = 0
    while i < len(chunks):
        if len(chunks[i]) < min_chunk and len(chunks) > 1:
            can_prev = i > 0 and (len(chunks[i - 1]) + len(chunks[i]) + 2 <= soft_cap)
            can_next = i + 1 < len(chunks) and (len(chunks[i]) + len(chunks[i + 1]) + 2 <= soft_cap)
            if can_prev and can_next:
                if len(chunks[i - 1]) <= len(chunks[i + 1]):
                    chunks[i - 1] = f"{chunks[i - 1]}\n\n{chunks[i]}"
                    chunks.pop(i)
                    continue
                else:
                    chunks[i + 1] = f"{chunks[i]}\n\n{chunks[i + 1]}"
                    chunks.pop(i)
                    continue
            elif can_prev:
                chunks[i - 1] = f"{chunks[i - 1]}\n\n{chunks[i]}"
                chunks.pop(i)
                continue
            elif can_next:
                chunks[i + 1] = f"{chunks[i]}\n\n{chunks[i + 1]}"
                chunks.pop(i)
                continue
        i += 1

    return chunks


def build_chunks_mode_a(sections: list[str], max_chars: int = 13500, min_chunk: int = 6500) -> list[str]:
    """Вариант А (Стандартный): держит подразделы ### целиком (7 000 - 13 500 сырых знаков / 5k-9k чистых).
    Короткие соседние подразделы склеивает, чтобы не было огрызков.
    """
    refined: list[str] = []
    for sec in sections:
        refined.extend(split_oversized_block(sec, max_chars))
    return pack_blocks_smart(refined, max_chars=max_chars, min_chunk=min_chunk)


def build_chunks_mode_b(sections: list[str], max_chars: int = 20200, min_chunk: int = 11500) -> list[str]:
    """Вариант Б (Экономный): упаковывает по 2-3 целых подраздела ### в крупные блоки
    (13 000 - 20 200 сырых знаков / 9 000 - 13 500 чистых японских знаков).
    """
    refined: list[str] = []
    for sec in sections:
        refined.extend(split_oversized_block(sec, max_chars))
    return pack_blocks_smart(refined, max_chars=max_chars, min_chunk=min_chunk)


def extract_headings(chunk: str) -> str:
    """Возвращает список всех заголовков ## и ### внутри чанка для сводной таблицы."""
    headings = re.findall(r"^#{2,3}\s+(.+)$", chunk, flags=re.M)
    if not headings:
        first_line = chunk.splitlines()[0][:45]
        return f"(продолжение сцены: {first_line}…)"
    clean = [re.sub(r"〔[^〕]*〕", "", h).strip() for h in headings]
    return " + ".join(clean)


def save_and_verify(chunks: list[str], original_body: str, out_dir: Path, label: str) -> None:
    """Проверяет посимвольное совпадение с исходником и сохраняет файлы чанков."""
    reconstructed = "\n\n".join(chunks)
    if reconstructed != original_body:
        raise RuntimeError(
            f"[{label}] ОШИБКА ЦЕЛОСТНОСТИ: длина склеенных чанков ({len(reconstructed)}) "
            f"не совпадает с исходником ({len(original_body)})!"
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    for old_file in out_dir.glob("chunk_*.md"):
        old_file.unlink()

    total_cleaned = sum(pure_jp_len(c) for c in chunks)
    summary_lines = [
        f"# Карта разбиения ({label})",
        "",
        "| Файл | Сырых символов (`.md`) | Символов без фуриганы и тех. маркеров | Содержимое (заголовки) |",
        "|---|---:|---:|---|",
    ]

    print(f"\n=== {label} (Папка: {out_dir}) ===")
    for i, chunk in enumerate(chunks, 1):
        fname = f"chunk_{i:02d}.md"
        (out_dir / fname).write_text(chunk + "\n", encoding="utf-8", newline="\n")
        h_info = extract_headings(chunk)
        clean_len = pure_jp_len(chunk)
        print(f"  {fname} | {len(chunk):6d} (.md) | {clean_len:6d} (без фуриганы и маркеров) | {h_info}")
        summary_lines.append(f"| `{fname}` | {len(chunk)} | {clean_len} | {h_info} |")

    summary_lines.extend([
        "",
        f"- **Всего чанков:** {len(chunks)}",
        f"- **Сумма сырых символов (`.md`):** {len(reconstructed)} (100% совпадение с исходником)",
        f"- **Сумма символов без фуриганы и тех. маркеров:** {total_cleaned}",
    ])
    (out_dir / "_index.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Нарезка volumeX.md на чанки для перевода (Варианты А и Б).")
    parser.add_argument("input", type=Path, help="Путь к файлу volumeX.md (например, volume4.md)")
    parser.add_argument(
        "--mode",
        choices=["a", "b", "both"],
        default="both",
        help="Режим: 'a' (стандартный, 11-13 чанков), 'b' (экономный, 7-8 крупных чанков), 'both' (оба сразу)",
    )
    parser.add_argument(
        "--start-from",
        type=str,
        default=None,
        help="Начать нарезку с указанной подстроки/заголовка (например, '### ６．ラキシュ')",
    )
    parser.add_argument(
        "--keep-colophon",
        action="store_true",
        help="Оставить технический колофон издательства (奥付) в последнем чанке",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Базовая папка для сохранения чанков (по умолчанию: chunks_<имя_файла>)",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"ОШИБКА: Файл не найден: {args.input}", file=sys.stderr)
        return 1

    raw_text = args.input.read_text(encoding="utf-8")
    _, body = strip_wrappers(raw_text, keep_colophon=args.keep_colophon)

    if args.start_from:
        pos = body.find(args.start_from)
        if pos == -1:
            print(f"ОШИБКА: Подстрока '{args.start_from}' не найдена в файле!", file=sys.stderr)
            return 1
        body = body[pos:].strip()

    sections = split_into_sections(body)
    base_out = args.out_dir or (args.input.parent / f"chunks_{args.input.stem}")

    if args.mode in ("a", "both"):
        chunks_a = build_chunks_mode_a(sections)
        dir_a = base_out / "variant_A" if args.mode == "both" else base_out
        save_and_verify(chunks_a, body, dir_a, "Вариант А — Стандартный (по подразделам)")

    if args.mode in ("b", "both"):
        chunks_b = build_chunks_mode_b(sections)
        dir_b = base_out / "variant_B" if args.mode == "both" else base_out
        save_and_verify(chunks_b, body, dir_b, "Вариант Б — Экономный (укрупнённые блоки)")

    print("\nГотово! Проверка целостности текста пройдена на 100%.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
