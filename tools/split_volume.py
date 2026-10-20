#!/usr/bin/env python3
"""Universal chunk splitter for extracted SukaSuka/SukaMoca Markdown volumes (v1.1)."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

# 1. Универсальный паттерн разделителя сцен для всех томов:
# Любой одиночный маркер gaiji на отдельной строке, либо символы † / * * *
SCENE_BREAK_RE = re.compile(
    r"(?:\n\n[пауза]\n\n)?\n\n"
    r"(?:\[\[EPUB_IMAGE:[^\n]*gaiji[^\n]*\]\]|†|\*\s*\*\s*\*|＊＊＊)"
    r"(?:\n\n[пауза])?(?=\n\n)"
)

# 2. Паттерн одиночной пустой строки [пауза]
PAUSE_BREAK_RE = re.compile(r"\n\n[пауза](?=\n\n)")

# 3. Страховочный паттерн обычного абзаца (если на 10 000+ знаков нет ни одной [пауза])
PARAGRAPH_BREAK_RE = re.compile(r"\n\n(?=(?![пауза])[^\n])")


def strip_wrappers(text: str, keep_colophon: bool = False) -> tuple[str, str]:
    """Отделяет техническую шапку в начале и (по умолчанию) издательский колофон 奥付 в конце."""
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
        # Отсекаем блок иллюстратора/колофона (p-credit / ## 奥付) в самом конце тома
        colophon_match = re.search(
            r"\n\n(?:本作品のイラストは|##\s+奥付\b)", body
        )
        if colophon_match:
            body = body[: colophon_match.start()].strip()

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


def split_section_by_regex(text: str, pattern: re.Pattern, max_chars: int) -> list[str]:
    """Делит крупный блок по разделителям, стараясь делать части сбалансированными."""
    matches = list(pattern.finditer(text))
    if not matches:
        return [text]

    cut_points = [0] + [m.start() for m in matches] + [len(text)]
    atomic_pieces = [
        text[cut_points[i] : cut_points[i + 1]].strip()
        for i in range(len(cut_points) - 1)
        if text[cut_points[i] : cut_points[i + 1]].strip()
    ]

    # Чтобы не оставлять маленький хвостик в конце при делении большого подраздела,
    # рассчитываем целевой размер одной части пропорционально:
    num_parts = max(1, (len(text) + max_chars - 1) // max_chars)
    balanced_limit = max(max_chars, (len(text) // num_parts) + 1200)
    effective_limit = min(max_chars, balanced_limit)

    grouped: list[str] = []
    current = ""
    for piece in atomic_pieces:
        candidate = f"{current}\n\n{piece}" if current else piece
        if current and len(candidate) > max_chars:
            grouped.append(current)
            current = piece
        else:
            current = candidate
    if current:
        # Если последний осколок внутри подраздела вышел слишком мелким (< 3000),
        # а сумма с предыдущим не превышает max_chars + 1500 — склеиваем обратно
        if grouped and len(current) < 3000 and len(grouped[-1]) + len(current) + 2 <= max_chars + 1500:
            grouped[-1] = f"{grouped[-1]}\n\n{current}"
        else:
            grouped.append(current)

    return grouped


def split_oversized_block(block: str, max_chars: int) -> list[str]:
    """Каскадно дробит слишком длинный блок: по сценам -> по [пауза] -> по абзацам."""
    if len(block) <= max_chars:
        return [block]

    by_scenes = split_section_by_regex(block, SCENE_BREAK_RE, max_chars)
    by_pauses: list[str] = []
    for piece in by_scenes:
        if len(piece) <= max_chars:
            by_pauses.append(piece)
        else:
            by_pauses.extend(split_section_by_regex(piece, PAUSE_BREAK_RE, max_chars))

    final_pieces: list[str] = []
    for piece in by_pauses:
        if len(piece) <= max_chars:
            final_pieces.append(piece)
        else:
            final_pieces.extend(split_section_by_regex(piece, PARAGRAPH_BREAK_RE, max_chars))

    return final_pieces


def build_chunks_mode_a(sections: list[str], max_chars: int = 9500, merge_below: int = 8500) -> list[str]:
    """Вариант А: 1 подраздел = 1 чанк (делит только >9500, склеивает мелкие <=8500)."""
    refined: list[str] = []
    for sec in sections:
        refined.extend(split_oversized_block(sec, max_chars))

    chunks: list[str] = []
    for block in refined:
        if (
            chunks
            and (len(chunks[-1]) < 4200 or len(block) < 4200)
            and len(chunks[-1]) + len(block) + 2 <= merge_below
        ):
            chunks[-1] = f"{chunks[-1]}\n\n{block}"
        else:
            chunks.append(block)
    return chunks


def build_chunks_mode_b(sections: list[str], max_chars: int = 14000) -> list[str]:
    """Вариант Б: сохраняет подразделы ### ЦЕЛИКОМ, упаковывая их до 14 000 знаков.
    Дробит подраздел по сценам ТОЛЬКО если сам подраздел > 14 000 знаков.
    """
    refined: list[str] = []
    for sec in sections:
        # Если подраздел целиком влезает в 14 000 — НЕ дробим его на сцены!
        refined.extend(split_oversized_block(sec, max_chars))

    chunks: list[str] = []
    current = ""
    for block in refined:
        candidate = f"{current}\n\n{block}" if current else block
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = block

    if current:
        if chunks and len(current) < 3500 and len(chunks[-1]) + len(current) + 2 <= max_chars + 1500:
            chunks[-1] = f"{chunks[-1]}\n\n{current}"
        else:
            chunks.append(current)

    return chunks


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

    summary_lines = [
        f"# Карта разбиения ({label})",
        "",
        "| Файл | Символов | Содержимое (заголовки) |",
        "|---|---:|---|",
    ]

    print(f"\n=== {label} (Папка: {out_dir}) ===")
    for i, chunk in enumerate(chunks, 1):
        fname = f"chunk_{i:02d}.md"
        (out_dir / fname).write_text(chunk + "\n", encoding="utf-8", newline="\n")
        h_info = extract_headings(chunk)
        print(f"  {fname} | {len(chunk):6d} знаков | {h_info}")
        summary_lines.append(f"| `{fname}` | {len(chunk)} | {h_info} |")

    summary_lines.extend([
        "",
        f"- **Всего чанков:** {len(chunks)}",
        f"- **Сумма символов:** {len(reconstructed)} (100% совпадение с исходником)",
    ])
    (out_dir / "_index.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Нарезка volumeX.md на чанки для перевода (Варианты А и Б).")
    parser.add_argument("input", type=Path, help="Путь к файлу volumeX.md (например, volume4.md)")
    parser.add_argument(
        "--mode",
        choices=["a", "b", "both"],
        default="both",
        help="Режим нарезки: 'a' (по подразделам, 5-9.5k), 'b' (экономный, до 14k без разрыва глав), 'both' (оба сразу)",
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
