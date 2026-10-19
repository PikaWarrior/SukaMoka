# Отчёт об извлечении японского исходника — том 4

## Итог и ограничения

Извлечение сформировано по `standard.opf` и порядку `spine`. Все 21 spine-элемент сопоставлены с файлами `raw/4/item/xhtml/`. До работы `volume4.md` и `volume4_report.md` в `main` отсутствовали; существующие файлы не перезаписывались.

Ограничение парсера: в доступном соединении не удалось запустить `lxml` или стандартную XML-библиотеку. Использован программный структурный токенизатор с деревом тегов/атрибутов и проверкой парности тегов. Это не полная валидация EPUB/XML; ограничение не скрывается и рекомендуется использовать стандартный XML-парсер для следующего тома, если он доступен.

Графические файлы не удалось открыть визуально: прямой запрос к raw image endpoint вернул `cache miss`, а файловый коннектор возвращает текстовые ресурсы. Изображения сохранены маркерами; назначение внутри самих изображений, включая gaiji, не подтверждено визуально.

## Обнаруженные исходные файлы

- `raw/4/item/standard.opf` (структурно прочитан; SHA в GitHub при проверке: `aba8f66de9a2818df19d4184122fbbf306fba73e`).
- `raw/4/item/navigation-documents.xhtml` (использован для заголовков; SHA `8e2398fcc5fabf04415178736e5a136ad839f629`).
- `raw/4/item/xhtml/`: 21 файл: `p-cover.xhtml`, `p-fmatter-001.xhtml`, `p-fmatter-002.xhtml`, `p-titlepage.xhtml`, `p-caution.xhtml`, `p-toc-001.xhtml`, `p-toc-002.xhtml`, `p-001.xhtml`–`p-011.xhtml`, `p-credit.xhtml`, `p-colophon.xhtml`, `p-bookwalker.xhtml`.
- `raw/4/item/image/`: 15 ресурсов: `cover.jpg`, `kuchie-001.jpg`, `kuchie-002.jpg`, `toc-001.jpg`, `p004-005.jpg`, `p014-015.jpg`, `p114-115.jpg`, `p214-215.jpg`, `p268-269.jpg`, `gaiji-cid776-m-v.png`, `gaiji-hwid-038.png`, `gaiji-num-03.png`, `gaiji-num-04.png`, `logo-sneaker.png`, `i-bookwalker.jpg`.
- `raw/4.md` существует (128 957 символов), но содержит Pandoc/HTML passthrough разметку и не использовался как основной источник.

## Порядок чтения по spine

1. `p-cover.xhtml` → `raw/4/item/xhtml/p-cover.xhtml` — графическая страница, сохранена маркером
2. `p-fmatter-001.xhtml` → `raw/4/item/xhtml/p-fmatter-001.xhtml` — графическая страница, сохранена маркером
3. `p-fmatter-002.xhtml` → `raw/4/item/xhtml/p-fmatter-002.xhtml` — графическая страница, сохранена маркером
4. `p-titlepage.xhtml` → `raw/4/item/xhtml/p-titlepage.xhtml`
5. `p-caution.xhtml` → `raw/4/item/xhtml/p-caution.xhtml`
6. `p-toc-001.xhtml` → `raw/4/item/xhtml/p-toc-001.xhtml` — графическая страница, сохранена маркером
7. `p-toc-002.xhtml` → `raw/4/item/xhtml/p-toc-002.xhtml` — текст оглавления сохранён в отчёте, не дублирован в основном тексте
8. `p-001.xhtml` → `raw/4/item/xhtml/p-001.xhtml` — графическая страница, сохранена маркером
9. `p-002.xhtml` → `raw/4/item/xhtml/p-002.xhtml`
10. `p-003.xhtml` → `raw/4/item/xhtml/p-003.xhtml` — графическая страница, сохранена маркером
11. `p-004.xhtml` → `raw/4/item/xhtml/p-004.xhtml`
12. `p-005.xhtml` → `raw/4/item/xhtml/p-005.xhtml` — графическая страница, сохранена маркером
13. `p-006.xhtml` → `raw/4/item/xhtml/p-006.xhtml`
14. `p-007.xhtml` → `raw/4/item/xhtml/p-007.xhtml` — графическая страница, сохранена маркером
15. `p-008.xhtml` → `raw/4/item/xhtml/p-008.xhtml`
16. `p-009.xhtml` → `raw/4/item/xhtml/p-009.xhtml` — графическая страница, сохранена маркером
17. `p-010.xhtml` → `raw/4/item/xhtml/p-010.xhtml`
18. `p-011.xhtml` → `raw/4/item/xhtml/p-011.xhtml`
19. `p-credit.xhtml` → `raw/4/item/xhtml/p-credit.xhtml`
20. `p-colophon.xhtml` → `raw/4/item/xhtml/p-colophon.xhtml`
21. `p-bookwalker.xhtml` → `raw/4/item/xhtml/p-bookwalker.xhtml` — графическая страница, сохранена маркером

## Заголовки, восстановленные по навигации

- `p-001.xhtml` → `『都合の良い夢』 - delusion of dependence -` (заголовок добавлен перед маркером соответствующей графической страницы).
- `p-003.xhtml` → `『その罪人を追え、そして』 - who is tagger? -` (заголовок добавлен перед маркером соответствующей графической страницы).
- `p-005.xhtml` → `『語らぬ者と語れ、あるいは』 - crossing road -` (заголовок добавлен перед маркером соответствующей графической страницы).
- `p-007.xhtml` → `『交わらぬ道を行け、それこそが──Ａ』 - going separated ways -` (заголовок добавлен перед маркером соответствующей графической страницы).
- `p-009.xhtml` → `『沈黙する死者と雄弁な生者』 - the previous night -` (заголовок добавлен перед маркером соответствующей графической страницы).
- `p-011.xhtml`: заголовок послесловия находится в body, содержит ruby и сохранён.
- `p-colophon.xhtml`: перед body добавлен `奥付` по навигации.
- `p-caution.xhtml`: `<title>` = `ご利用上の注意`, но заголовка в body нет. Он не вставлен как текст книги; решение отмечено в Markdown-комментарии.

## Дословное текстовое оглавление

`p-toc-002.xhtml` содержит оглавление, перечисляющее части, которые уже представлены по своим местам в spine. Оно не добавлено вторым блоком в `volume4.md`; исключение зафиксировано комментарием в основном файле. Абзацы исходного оглавления в исходном порядке (пустые блоки обозначены пояснительно):

```text
ｃｏｎｔｅｎｔｓ
[пустой абзац оглавления]
[пустой абзац оглавления]
『都合の良い夢』 - delusion of dependence -
『その罪人を追え、そして』 - who is tagger? -
『語らぬ者と語れ、あるいは』 - crossing road -
『交わらぬ道を行け、それこそが──Ａ』 - going separated ways -
『沈黙する死者と雄弁な生者』 - the previous night -
[пустой абзац оглавления]
あとがき／あとがない状況で書いてます
```

Число пустых `<p>` в `p-toc-002.xhtml`: 3. Они отражены как `[пустой абзац оглавления]` в этой расшифровке, но не как паузы основного текста.
`p-toc-001.xhtml` — отдельная графическая страница в позиции оглавления; изображение помечено, но не просмотрено.

## Программные проверки

- `spine`: 21/21 записей разрешаются в исходные XHTML; необъяснённых пропусков файлов в spine нет.
- Включённые текстовые XHTML: 0 ошибок структурной вложенности и 0 несовпадений основного текстового слоя при поабзацном сравнении.
- Абзацы в обрабатываемых body: 2855 `<p>`; непустых 2698; пустых, представленных как `[пауза]`: 157. Оглавление вынесено отдельно; его пустые блоки подсчитаны отдельно.
- Ruby: 3205 элементов `<ruby>` и 4699 элементов `<rt>`; число сформированных чтений 4699; вся последовательность чтений совпала с исходной: да.
- Неполные/неоднозначные ruby: 0.
- `em-sesame`: 27 фрагментов оформлены как `<em>…</em>`. Семантические `strong`, `em`, `sup`, `sub` сохраняются; оформительские оболочки снимаются без удаления текста.
- Изображения: 35 размещений; 15/15 уникальных ресурсов из списка изображений встречены в XHTML.
- Изображения из списка без использования в XHTML: не обнаружены. Неожиданные ресурсы: не обнаружены.
- Литеральные скобки `〔`/`〕` вне `rt` в проверенных текстовых частях: 0.
- Комментарии XHTML, пропущенные при рендеринге body: 4. Неизвестные именованные XML-сущности: не обнаружены.
- Неизвестные элементы, встретившиеся при рендеринге абзацев: не обнаружены; их содержимое сохраняется.

### Статистика по текстовым XHTML

| XHTML | `<p>` | `<ruby>` | `<rt>` | `<img>/<image>` |
|---|---:|---:|---:|---:|
| `p-titlepage.xhtml` | 4 | 0 | 0 | 1 |
| `p-caution.xhtml` | 7 | 0 | 0 | 0 |
| `p-002.xhtml` | 89 | 104 | 145 | 0 |
| `p-004.xhtml` | 1007 | 1203 | 1771 | 6 |
| `p-006.xhtml` | 1049 | 1176 | 1762 | 9 |
| `p-008.xhtml` | 551 | 561 | 787 | 4 |
| `p-010.xhtml` | 98 | 122 | 179 | 1 |
| `p-011.xhtml` | 31 | 34 | 47 | 3 |
| `p-credit.xhtml` | 5 | 0 | 0 | 0 |
| `p-colophon.xhtml` | 14 | 5 | 8 | 1 |

## Карта всех размещений изображений

Каждый occurrence имеет отдельный маркер `[[EPUB_IMAGE:v4:xhtml/<файл>.xhtml:<имя_ресурса>:occ-NN]]`. В сборке EPUB ресурс берётся из `raw/4/item/image/<имя_ресурса>`, место — из маркера и исходного XHTML. Маркеры нельзя переводить, удалять или объединять.

| № | Маркер | Ресурс в репозитории | Исходный XHTML | Тип размещения / основание | Контекст до/после | Текст изображения |
|---:|---|---|---|---|---|---|
| 1 | `[[EPUB_IMAGE:v4:xhtml/p-titlepage.xhtml:logo-sneaker.png:occ-01]]` | [`raw/4/item/image/logo-sneaker.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/logo-sneaker.png) | [`raw/4/item/xhtml/p-titlepage.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-titlepage.xhtml) | встроенное изображение; embedded image; visual content not checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 2 | `[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-004.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 3 | `[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-004.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 4 | `[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-hwid-038.png:occ-03]]` | [`raw/4/item/image/gaiji-hwid-038.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-hwid-038.png) | [`raw/4/item/xhtml/p-004.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** 番浮遊島に居を構える護翼軍第五師団総団長は、小声でぼやく。 | визуально не проверено; текст изображения не извлечён |
| 5 | `[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-004.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 6 | `[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-hwid-038.png:occ-05]]` | [`raw/4/item/image/gaiji-hwid-038.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-hwid-038.png) | [`raw/4/item/xhtml/p-004.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | まだ **[IMAGE]** 番浮遊島でやることがあるのではないのか、と言われた。 | визуально не проверено; текст изображения не извлечён |
| 7 | `[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-06]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-004.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 8 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 9 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 10 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 11 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 12 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-05]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 13 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-06]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 14 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-07]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 15 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-08]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 16 | `[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-09]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-006.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 17 | `[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-008.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 18 | `[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-02]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-008.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 19 | `[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-008.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 20 | `[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-04]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-008.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 21 | `[[EPUB_IMAGE:v4:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-01]]` | [`raw/4/item/image/gaiji-cid776-m-v.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [`raw/4/item/xhtml/p-010.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-010.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 22 | `[[EPUB_IMAGE:v4:xhtml/p-011.xhtml:gaiji-num-04.png:occ-01]]` | [`raw/4/item/image/gaiji-num-04.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-num-04.png) | [`raw/4/item/xhtml/p-011.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-011.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | おう一冊の中でひとつのエピソードを閉じる形は保ってきていました。が、今回はちょっとその辺り事情が違いまして、「 **[IMAGE]** 」で始まった一番大きなエピソードが、「」の中で完結していません。続きます。上下巻みたいなタイトルのつき方にはな | визуально не проверено; текст изображения не извлечён |
| 23 | `[[EPUB_IMAGE:v4:xhtml/p-011.xhtml:gaiji-num-04.png:occ-02]]` | [`raw/4/item/image/gaiji-num-04.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-num-04.png) | [`raw/4/item/xhtml/p-011.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-011.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | る形は保ってきていました。が、今回はちょっとその辺り事情が違いまして、「」で始まった一番大きなエピソードが、「 **[IMAGE]** 」の中で完結していません。続きます。上下巻みたいなタイトルのつき方にはなってませんが、イメージとしては近い感じ | визуально не проверено; текст изображения не извлечён |
| 24 | `[[EPUB_IMAGE:v4:xhtml/p-011.xhtml:gaiji-num-03.png:occ-03]]` | [`raw/4/item/image/gaiji-num-03.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-num-03.png) | [`raw/4/item/xhtml/p-011.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-011.xhtml) | встроенный gaiji, class=gaiji; XHTML class=gaiji; glyph not visually checked | そして、前巻「 **[IMAGE]** 」のあとがきでも触れましたが、今回から本格的に、前シリーズ『終末なにしてますか？　忙しいですか？　救ってもらっ | визуально не проверено; текст изображения не извлечён |
| 25 | `[[EPUB_IMAGE:v4:xhtml/p-colophon.xhtml:logo-sneaker.png:occ-01]]` | [`raw/4/item/image/logo-sneaker.png`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/logo-sneaker.png) | [`raw/4/item/xhtml/p-colophon.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-colophon.xhtml) | встроенное изображение; embedded image; visual content not checked | **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 26 | `[[EPUB_IMAGE:v4:xhtml/p-cover.xhtml:cover.jpg:occ-01]]` | [`raw/4/item/image/cover.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/cover.jpg) | [`raw/4/item/xhtml/p-cover.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-cover.xhtml) | отдельная графическая страница; manifest property cover-image; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 27 | `[[EPUB_IMAGE:v4:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]` | [`raw/4/item/image/kuchie-001.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/kuchie-001.jpg) | [`raw/4/item/xhtml/p-fmatter-001.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-fmatter-001.xhtml) | отдельная графическая страница; separate graph-only front-matter page; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 28 | `[[EPUB_IMAGE:v4:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]` | [`raw/4/item/image/kuchie-002.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/kuchie-002.jpg) | [`raw/4/item/xhtml/p-fmatter-002.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-fmatter-002.xhtml) | отдельная графическая страница; separate graph-only front-matter page; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 29 | `[[EPUB_IMAGE:v4:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]` | [`raw/4/item/image/toc-001.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/toc-001.jpg) | [`raw/4/item/xhtml/p-toc-001.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-toc-001.xhtml) | отдельная графическая страница; graph-only page in TOC position; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 30 | `[[EPUB_IMAGE:v4:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]` | [`raw/4/item/image/p004-005.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p004-005.jpg) | [`raw/4/item/xhtml/p-001.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-001.xhtml) | отдельная графическая страница; graph-only page before Part 1; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 31 | `[[EPUB_IMAGE:v4:xhtml/p-003.xhtml:p014-015.jpg:occ-01]]` | [`raw/4/item/image/p014-015.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p014-015.jpg) | [`raw/4/item/xhtml/p-003.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-003.xhtml) | отдельная графическая страница; graph-only page before Part 2; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 32 | `[[EPUB_IMAGE:v4:xhtml/p-005.xhtml:p114-115.jpg:occ-01]]` | [`raw/4/item/image/p114-115.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p114-115.jpg) | [`raw/4/item/xhtml/p-005.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-005.xhtml) | отдельная графическая страница; graph-only page before Part 3; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 33 | `[[EPUB_IMAGE:v4:xhtml/p-007.xhtml:p214-215.jpg:occ-01]]` | [`raw/4/item/image/p214-215.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p214-215.jpg) | [`raw/4/item/xhtml/p-007.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-007.xhtml) | отдельная графическая страница; graph-only page before Part 4; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 34 | `[[EPUB_IMAGE:v4:xhtml/p-009.xhtml:p268-269.jpg:occ-01]]` | [`raw/4/item/image/p268-269.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p268-269.jpg) | [`raw/4/item/xhtml/p-009.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-009.xhtml) | отдельная графическая страница; graph-only page before Part 5; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |
| 35 | `[[EPUB_IMAGE:v4:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]` | [`raw/4/item/image/i-bookwalker.jpg`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/i-bookwalker.jpg) | [`raw/4/item/xhtml/p-bookwalker.xhtml`](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-bookwalker.xhtml) | отдельная графическая страница; graph-only page at end of spine; visual contents unverified | Отдельная графическая XHTML-страница в spine. **[IMAGE]** | визуально не проверено; текст изображения не извлечён |

## Неоднозначности и пропуски

- `p-cover`, `p-fmatter-001`, `p-fmatter-002`, `p-toc-001`, `p-001`, `p-003`, `p-005`, `p-007`, `p-009`, `p-bookwalker` сохранены как графические страницы с маркерами и не считаются пустыми.
- Все `img` с `class=gaiji` помечены в точной позиции. Unicode-подстановки не выполнялись: изображение визуально не проверено, значение глифа не извлечено.
- `logo-sneaker.png` встроен в `p-titlepage.xhtml` и `p-colophon.xhtml`; каждое размещение имеет собственный маркер.
- Каждый пустой `<p>` со структурой `<br>` в включённых body представлен как `[пауза]`. Это не доказывает, что он является сценическим разделителем; это лишь явное сохранение пустого блока.
- Оглавление не потеряно: его непустые строки и пустые `<p>` перечислены в этом отчёте вместо повторного блока в `volume4.md`.
- Текст, который может быть нарисован внутри иллюстраций, не извлечён. Этот вопрос остаётся открытым для проверки перед финальным EPUB.

## Инструкции для сборщика будущего EPUB

1. Не переносить исходные CSS, fixed-layout разметку и шрифты из японского EPUB. Создавать новый reflowable EPUB на основе русского перевода и `instructions/pasport proekta.md`.
2. Сохранить все `[[EPUB_IMAGE:...]]` вплоть до сборки. Маркер сопоставляется с точным файлом в `raw/4/item/image/` и исходным XHTML; положение сохраняется относительно абзацев, не переносить все изображения в конец.
3. Визуально проверить все 15 ресурсов, особенно gaiji и текст внутри изображений; подменять их Unicode или сценическим разделителем только после подтверждения.
4. Восстановить заголовки и `[пауза]`; не дублировать текст оглавления, которое приведено выше.
5. Использовать минимальный CSS по паспорту проекта: reflowable, левое выравнивание, без отступа первой строки, без авторасстановки переносов, без встраивания sans-serif, размер около 1.125em, line-height 1.5, интервал абзацев около 0.7em, без жёстких цветов/фона; `* * *` только для подтверждённых сценических разделителей.
6. Перед финальной сборкой убедиться, что все маркеры изображений из исходника присутствуют и не дублированы в переводе.

## Для тома 5

- Если доступна полноценная XML-библиотека (`lxml` или стандартный XML-парсер), использовать её. Если среда ограничена GitHub-коннектором, честно описать ограничение структурного токенизатора и выполнить поабзацную сверку основы и ruby.
- Пропуски и исключения не оставлять без записи в основном Markdown или отчёте; ни пустые блоки, ни изображения, ни графические XHTML-страницы не удалять молча.
- Для следующего запуска использовать `raw/5/item/`, `volume5.md` и `volume5_report.md`.
