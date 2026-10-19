# Отчёт об извлечении японского исходника — том 5

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| `image/cover.jpg` | 750511 | `586668a870fa20879d43000f18364d3389ed9cbb0c42c4451c6c172a273ee07b` |
| `image/gaiji-cid776-m-v.png` | 4828 | `f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf` |
| `image/i-bookwalker.jpg` | 116828 | `93da8cbcf35fc14c16188ff6e325669b90ced56a14d72ce495631c76c76b6b75` |
| `image/kuchie-001.jpg` | 666712 | `bd8b04dfa65c4e15c34dd7b9b0e20d29c9978aa22c0c84d7728a10099b666cc6` |
| `image/kuchie-002.jpg` | 477195 | `79a67b6c70322d8db155f05366c532ce1222a944c11c0ecccb1faf919acb561b` |
| `image/logo-sneaker.png` | 4267 | `3c68cdfe60118126cac64e2efc73d20294a63b7c1cece9c1adfb59553fa93f88` |
| `image/p004-005.jpg` | 809815 | `839b5f6566c0fff9f09f983e61793d1d13d2d951ecd2cdc2177b39eefe723a02` |
| `image/p016-017.jpg` | 1083461 | `5f8a8dce552f3498b983a239ea280503664ab0080b40088d5ea2f7b42a2fefa6` |
| `image/p100-101.jpg` | 1335750 | `c55df81a39d4c6e94c187e090d323bff504a492b7a1b82e3824750f86d2c76d5` |
| `image/p202-203.jpg` | 946065 | `c877573468b94414c7dcddcd8ae973fc9f568774a960d52d1fa7bffbfad64632` |
| `image/p272-273.jpg` | 1016776 | `6a53dc5311ddb856633c38971991b3e34b691252878f6ff015d5c7454fed5d5b` |
| `image/toc-001.jpg` | 1272023 | `236a93f6510a6c145e3bfb549da2ddee6c0f6b45c6b36e4e8bb0e3ee28818b9c` |
| `navigation-documents.xhtml` | 1432 | `ee4ed5876ed1d62a2de102bbcf8581b9823e173f60ec942e1ca5d7919158bedd` |
| `standard.opf` | 8954 | `721cac9facb30f9642e635b6a949a6e3a4ee066eab2461e88706d6cd9063161e` |
| `style/book-style.css` | 6265 | `8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe` |
| `style/fixed-layout-jp.css` | 134 | `d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6` |
| `style/style-advance.css` | 84707 | `2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306` |
| `style/style-check.css` | 2656 | `d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a` |
| `style/style-kadokawa.css` | 7024 | `b740df19e7fb68db8d4e55c2b0bbf9e640444a0f72bd1105e67005518cca3c5c` |
| `style/style-karc.css` | 1569 | `4c16008a60f369029d740186aa957b960f317382331c3bb582f08fbd854051f9` |
| `style/style-reset.css` | 2366 | `105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899` |
| `style/style-standard.css` | 54465 | `89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a` |
| `xhtml/p-001.xhtml` | 791 | `5867e0c3fac606bbe298018fba5bffebf6d235fbc93cc461b96791a272b5f840` |
| `xhtml/p-002.xhtml` | 19447 | `72d51e5c7234d4ce1f28a0239d8e4568138796fea1ab81e543250be12d96b80b` |
| `xhtml/p-003.xhtml` | 826 | `5de6512418fe199b52543790fba26ac579aac7a984b35352b65138e577b2cf89` |
| `xhtml/p-004.xhtml` | 152258 | `0b32529706328c4ecf78bc4c7b237b43cf6b7c5ff23bb2ff5836de6b39b45739` |
| `xhtml/p-005.xhtml` | 791 | `e2db9fd505cc64fb8275c9f0456dd6531d8b5447277adf3a671cea3705be7ecd` |
| `xhtml/p-006.xhtml` | 182144 | `a1be65488c32e7f0e2c62ce08d68c93d6bd808df224716fd037a61c0dadd5bd2` |
| `xhtml/p-007.xhtml` | 798 | `eb382eec489c0ec2f3f0c8685c651721602f862258f750a7608340ac6ca443d3` |
| `xhtml/p-008.xhtml` | 118657 | `c27c7b1d5afbc2d6b4c13954401ae3154dc0352fd7acbeb63421a82716ed014c` |
| `xhtml/p-009.xhtml` | 793 | `7d44ed36557cce615e9f4dd930f0de3b96970a33eff0779a9166126f1401496d` |
| `xhtml/p-010.xhtml` | 11290 | `3fa541a3efc8dc67638a6c6a8afdef48cde653264bb80e17da16a5aad86c1b1c` |
| `xhtml/p-011.xhtml` | 4229 | `6b5c0532ecb98ea02bb4d1be61e5c0e6f22d9eda4a5c87c2472d786781c6b4b9` |
| `xhtml/p-bookwalker.xhtml` | 671 | `1757004b8dd65a767fbba5fce482c063c27d14aa4225e6dc46e91621cc1ca879` |
| `xhtml/p-caution.xhtml` | 1305 | `d347da7e33e919e5d44526455b30e16549fc00d8f35fb373f12788f4539fed52` |
| `xhtml/p-colophon.xhtml` | 2119 | `caf481f3d1e840cf2314db464627f6ac8477947790027ee3f61f3496b8d7a59f` |
| `xhtml/p-cover.xhtml` | 742 | `cd68c353050f329f4921ee0bd5ffa5813b5fe2f3f21b97dc8def737deedd13e1` |
| `xhtml/p-credit.xhtml` | 618 | `9a7801fa679f1ba81916bbf2b696cccc6577163b6909c9cd5773f1522bcac457` |
| `xhtml/p-fmatter-001.xhtml` | 729 | `1c5cbf9ef24991c01bfb8b91ab3831688676e326bbee7ccd4ec634d94934a9fd` |
| `xhtml/p-fmatter-002.xhtml` | 729 | `5c565a77da7a8d29de959e609039332277575cefeb1b90266c217ceacbdb8c3a` |
| `xhtml/p-titlepage.xhtml` | 1007 | `a2654db9a2c3558c07e8aabd149cea2bec9949a7de7ca43bf49a7ba712d63767` |
| `xhtml/p-toc-001.xhtml` | 726 | `edec028abaef88ef09ce2290db11e5701ce0d06185ed0bf279cbc28f5ab82c26` |
| `xhtml/p-toc-002.xhtml` | 1375 | `9f0655006d22ef5c4f07036e7fa865db995c5f6ea028f6e39e5d3d2b9b1201f2` |

## Полный manifest

| id | href | media-type | Файл найден | Использование |
|---|---|---|---|---|
| toc | <code>navigation-documents.xhtml</code> | application/xhtml+xml | да | package metadata: EPUB3 navigation |
| fixed-layout-jp | <code>style/fixed-layout-jp.css</code> | text/css | да | локальная ссылка |
| book-style | <code>style/book-style.css</code> | text/css | да | локальная ссылка |
| style-reset | <code>style/style-reset.css</code> | text/css | да | локальная ссылка |
| style-standard | <code>style/style-standard.css</code> | text/css | да | локальная ссылка |
| style-advance | <code>style/style-advance.css</code> | text/css | да | локальная ссылка |
| style-check | <code>style/style-check.css</code> | text/css | да | упоминается только в комментарии CSS (@import неактивен): style/book-style.css |
| style-karc | <code>style/style-karc.css</code> | text/css | да | локальная ссылка |
| style-kadokawa | <code>style/style-kadokawa.css</code> | text/css | да | локальная ссылка |
| cover | <code>image/cover.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-001 | <code>image/kuchie-001.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-002 | <code>image/kuchie-002.jpg</code> | image/jpeg | да | локальная ссылка |
| toc-001 | <code>image/toc-001.jpg</code> | image/jpeg | да | локальная ссылка |
| p004-005 | <code>image/p004-005.jpg</code> | image/jpeg | да | локальная ссылка |
| p016-017 | <code>image/p016-017.jpg</code> | image/jpeg | да | локальная ссылка |
| p100-101 | <code>image/p100-101.jpg</code> | image/jpeg | да | локальная ссылка |
| p202-203 | <code>image/p202-203.jpg</code> | image/jpeg | да | локальная ссылка |
| p272-273 | <code>image/p272-273.jpg</code> | image/jpeg | да | локальная ссылка |
| gaiji-cid776-m-v | <code>image/gaiji-cid776-m-v.png</code> | image/png | да | локальная ссылка |
| logo-sneaker | <code>image/logo-sneaker.png</code> | image/png | да | локальная ссылка |
| i-bookwalker | <code>image/i-bookwalker.jpg</code> | image/jpeg | да | локальная ссылка |
| p-cover | <code>xhtml/p-cover.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-001 | <code>xhtml/p-fmatter-001.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-002 | <code>xhtml/p-fmatter-002.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-titlepage | <code>xhtml/p-titlepage.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-caution | <code>xhtml/p-caution.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-toc-001 | <code>xhtml/p-toc-001.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-toc-002 | <code>xhtml/p-toc-002.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-001 | <code>xhtml/p-001.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-002 | <code>xhtml/p-002.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-003 | <code>xhtml/p-003.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-004 | <code>xhtml/p-004.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-005 | <code>xhtml/p-005.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-006 | <code>xhtml/p-006.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-007 | <code>xhtml/p-007.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-008 | <code>xhtml/p-008.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-009 | <code>xhtml/p-009.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-010 | <code>xhtml/p-010.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-011 | <code>xhtml/p-011.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-credit | <code>xhtml/p-credit.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-colophon | <code>xhtml/p-colophon.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-bookwalker | <code>xhtml/p-bookwalker.xhtml</code> | application/xhtml+xml | да | package metadata: spine |

## Spine

| № | idref | XHTML | Статус | p | ruby | rt | img/image |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `p-cover` | `xhtml/p-cover.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 2 | `p-fmatter-001` | `xhtml/p-fmatter-001.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 3 | `p-fmatter-002` | `xhtml/p-fmatter-002.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 4 | `p-titlepage` | `xhtml/p-titlepage.xhtml` | parsed | 4 | 0 | 0 | 1 |
| 5 | `p-caution` | `xhtml/p-caution.xhtml` | parsed | 7 | 0 | 0 | 0 |
| 6 | `p-toc-001` | `xhtml/p-toc-001.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 7 | `p-toc-002` | `xhtml/p-toc-002.xhtml` | TOC logged below, not repeated | 0 | 0 | 0 | 0 |
| 8 | `p-001` | `xhtml/p-001.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 9 | `p-002` | `xhtml/p-002.xhtml` | parsed | 107 | 162 | 228 | 3 |
| 10 | `p-003` | `xhtml/p-003.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 11 | `p-004` | `xhtml/p-004.xhtml` | parsed | 807 | 1085 | 1569 | 5 |
| 12 | `p-005` | `xhtml/p-005.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 13 | `p-006` | `xhtml/p-006.xhtml` | parsed | 1038 | 1178 | 1708 | 4 |
| 14 | `p-007` | `xhtml/p-007.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 15 | `p-008` | `xhtml/p-008.xhtml` | parsed | 735 | 806 | 1143 | 8 |
| 16 | `p-009` | `xhtml/p-009.xhtml` | parsed | 0 | 0 | 0 | 1 |
| 17 | `p-010` | `xhtml/p-010.xhtml` | parsed | 55 | 79 | 111 | 0 |
| 18 | `p-011` | `xhtml/p-011.xhtml` | parsed | 17 | 21 | 30 | 0 |
| 19 | `p-credit` | `xhtml/p-credit.xhtml` | parsed | 5 | 0 | 0 | 0 |
| 20 | `p-colophon` | `xhtml/p-colophon.xhtml` | parsed | 14 | 5 | 8 | 1 |
| 21 | `p-bookwalker` | `xhtml/p-bookwalker.xhtml` | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| `navigation-documents.xhtml` | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| `xhtml/p-001.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-002.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-003.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-004.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-005.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-006.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-007.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-008.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-009.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-010.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-011.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-bookwalker.xhtml` | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| `xhtml/p-caution.xhtml` | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| `xhtml/p-colophon.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-cover.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-credit.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-fmatter-001.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-fmatter-002.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-titlepage.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-toc-001.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| `xhtml/p-toc-002.xhtml` | 終末なにしてますか？ もう一度だけ、会えますか？#05 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『はじまりの話』 - unknown beast - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『交わらぬ道を行け、それこそが──Ｂ』 - dancing fairies - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『死者の行く道』 - a forked road - | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> |
| 『絆を束ねるもの』 - union is strength - | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> |
| 『悪の矜持』 - the ultimate bad king - | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> |
| あとがき／おあとがよろしいようで | <code>xhtml/p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 21; сопоставлены с manifest: 21.
- Абзацы p в основном потоке: 2789; пустых p, отмеченных [пауза]: 181.
- br-элементов: 181; em-sesame: 45.
- Начальных отступов снято: 1535 символов в 1455 абзацах; нестандартных случаев подробно перечислено: 20.
- CSS-классов в XHTML: 40 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 32; уникальных ресурсов в маркерах: 12.
- Изображений manifest без маркера в spine XHTML: 0.
- Расхождений текстового слоя абзацев: 0; расхождений порядка ruby-чтений: 0; ruby warnings: 0.
- Неизвестных элементов: 0; XML-комментариев: 17; processing instructions: 0.
- Литеральных символов 〔〕 вне rt: 0; предупреждений: 0.

### Расхождения текстового слоя


### Профиль начальных отступов

Для компактности стандартный отступ из одного U+3000 агрегирован по количеству. Все абзацы без отступа, не похожие на реплики/заголовки, перечислены по номерам; все удалённые отступы нестандартной длины приведены в подробной таблице ниже.

| XHTML | Категория | Количество p | Номера p (для потенциальных исключений) |
|---|---|---:|---|
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 15 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 28 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 64 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 53 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 5 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 299 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / other | 1 | 197 |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 449 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | empty/whitespace-only | 58 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | heading/style heading | 7 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | no indent / dialogue-like | 445 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | one U+3000 | 528 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 65 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 5 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 297 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 368 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 2 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 17 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 36 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 4 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | no indent / other | 2 | 16-17 |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 10 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 6 | 1-4, 6-7 |
| <code>xhtml/p-colophon.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 12 | 1-2, 4-13 |
| <code>xhtml/p-credit.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-credit.xhtml</code> | no indent / other | 2 | 4-5 |
| <code>xhtml/p-titlepage.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-titlepage.xhtml</code> | no indent / other | 3 | 1-2, 4 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-002.xhtml</code> | 17 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-002.xhtml</code> | 25 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-002.xhtml</code> | 102 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 25 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 85 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 174 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 249 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 313 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 157 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 483 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 609 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 766 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 36 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 255 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 320 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 338 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 447 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 466 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 520 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 721 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |

### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 2 |
| book-title | div | 2 |
| book-title-main | div | 2 |
| copyright | div | 1 |
| em-sesame | span | 45 |
| end-1em | div | 1 |
| font-0em90 | span | 1 |
| font-1em10 | p | 17 |
| font-1em10 | span | 6 |
| font-1em30 | p | 1 |
| font-1em30 | span | 1 |
| gaiji | img | 20 |
| gfont | div | 3 |
| gfont | span | 7 |
| hltr | html | 2 |
| label | div | 2 |
| label-logo | p | 2 |
| label-name | p | 1 |
| main | div | 21 |
| mfont | div | 1 |
| mfont | p | 18 |
| mfont | span | 1 |
| original-books | div | 1 |
| original-first-edition | p | 1 |
| original-title | p | 1 |
| p-caution | body | 1 |
| p-colophon | body | 1 |
| p-text | body | 7 |
| p-titlepage | body | 1 |
| p-toc | body | 1 |
| publish-address | p | 1 |
| publish-company | p | 1 |
| publish-person | p | 1 |
| publisher-data | div | 1 |
| release-date | div | 1 |
| start-1em | div | 1 |
| start-2em | div | 20 |
| support | div | 1 |
| support-contact | p | 1 |
| support-desk | p | 1 |
| support-note | p | 1 |
| tcy | span | 42 |
| vrtl | html | 9 |
| word-break-break-all | span | 11 |
Не обнаружены.

### Расхождения последовательности ruby-чтений

Не обнаружены.

### Ruby warnings

Не обнаружены.

### Неизвестные элементы

Не обнаружены.

### XML-комментарии и processing instructions

- `standard.opf` /*/*[1]/comment()[1]:  作品名 
- `standard.opf` /*/*[1]/comment()[2]:  著者名 
- `standard.opf` /*/*[1]/comment()[3]:  出版社名 
- `standard.opf` /*/*[1]/comment()[4]:  言語 
- `standard.opf` /*/*[1]/comment()[5]:  ファイルid 
- `standard.opf` /*/*[1]/comment()[6]:  更新日 
- `standard.opf` /*/*[1]/comment()[7]:  Fixed-Layout Documents指定 
- `standard.opf` /*/*[1]/comment()[8]:  etc. 
- `standard.opf` /*/*[2]/comment()[1]:  navigation 
- `standard.opf` /*/*[2]/comment()[2]:  style 
- `standard.opf` /*/*[2]/comment()[3]:  image 
- `standard.opf` /*/*[2]/comment()[4]:  xhtml 
- `standard.opf` /*/comment():  g406ee7 
- `xhtml/p-titlepage.xhtml` /*/*[2]/*/comment()[1]:  ======================================================================= 
- `xhtml/p-titlepage.xhtml` /*/*[2]/*/comment()[2]:  ======================================================================= 
- `xhtml/p-colophon.xhtml` /*/*[2]/*/comment()[1]:  ======================================================================= 
- `xhtml/p-colophon.xhtml` /*/*[2]/*/comment()[2]:  ======================================================================= 

### CSS url() и активные @import

- `style/book-style.css` @import `style-reset.css` -> `style/style-reset.css`
- `style/book-style.css` @import `style-standard.css` -> `style/style-standard.css`
- `style/book-style.css` @import `style-advance.css` -> `style/style-advance.css`
- `style/book-style.css` @import `style-karc.css` -> `style/style-karc.css`
- `style/book-style.css` @import `style-kadokawa.css` -> `style/style-kadokawa.css`

### Закомментированные CSS @import (неактивные)

- `style/book-style.css` содержит закомментированный @import `style-check.css` -> `style/style-check.css`; файл найден, но подключение неактивно.

## Проверка локальных ресурсов и фрагментов

| Source | Href | Resolved path | Status |
|---|---|---|---|
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | OK |
| <code>xhtml/p-cover.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-cover.xhtml</code> | <code>../image/cover.jpg</code> | <code>image/cover.jpg</code> | OK |
| <code>xhtml/p-fmatter-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-fmatter-001.xhtml</code> | <code>../image/kuchie-001.jpg</code> | <code>image/kuchie-001.jpg</code> | OK |
| <code>xhtml/p-fmatter-002.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-fmatter-002.xhtml</code> | <code>../image/kuchie-002.jpg</code> | <code>image/kuchie-002.jpg</code> | OK |
| <code>xhtml/p-titlepage.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-titlepage.xhtml</code> | <code>../image/logo-sneaker.png</code> | <code>image/logo-sneaker.png</code> | OK |
| <code>xhtml/p-caution.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../image/toc-001.jpg</code> | <code>image/toc-001.jpg</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../image/p004-005.jpg</code> | <code>image/p004-005.jpg</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../image/p016-017.jpg</code> | <code>image/p016-017.jpg</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/p100-101.jpg</code> | <code>image/p100-101.jpg</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/p202-203.jpg</code> | <code>image/p202-203.jpg</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../image/p272-273.jpg</code> | <code>image/p272-273.jpg</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-credit.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-colophon.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-colophon.xhtml</code> | <code>../image/logo-sneaker.png</code> | <code>image/logo-sneaker.png</code> | OK |
| <code>xhtml/p-bookwalker.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-bookwalker.xhtml</code> | <code>../image/i-bookwalker.jpg</code> | <code>image/i-bookwalker.jpg</code> | OK |
| <code>style/book-style.css</code> | <code>style-reset.css</code> | <code>style/style-reset.css</code> | OK |
| <code>style/book-style.css</code> | <code>style-standard.css</code> | <code>style/style-standard.css</code> | OK |
| <code>style/book-style.css</code> | <code>style-advance.css</code> | <code>style/style-advance.css</code> | OK |
| <code>style/book-style.css</code> | <code>style-karc.css</code> | <code>style/style-karc.css</code> | OK |
| <code>style/book-style.css</code> | <code>style-kadokawa.css</code> | <code>style/style-kadokawa.css</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> | OK |

## Карта размещений изображений

Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.

| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |
|---:|---|---|---|---|---|---|
| 1 | <code>[[EPUB_IMAGE:v5:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/5/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/cover.jpg) | [<code>raw/5/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v5:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/5/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/kuchie-001.jpg) | [<code>raw/5/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2005", "height": "1600", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v5:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/5/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/kuchie-002.jpg) | [<code>raw/5/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2006", "height": "1600", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v5:xhtml/p-titlepage.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/5/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/logo-sneaker.png) | [<code>raw/5/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 5 | <code>[[EPUB_IMAGE:v5:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/5/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/toc-001.jpg) | [<code>raw/5/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2255", "height": "1600", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v5:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/5/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/p004-005.jpg) | [<code>raw/5/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p004-005.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v5:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 8 | <code>[[EPUB_IMAGE:v5:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 9 | <code>[[EPUB_IMAGE:v5:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 10 | <code>[[EPUB_IMAGE:v5:xhtml/p-003.xhtml:p016-017.jpg:occ-01]]</code> | [<code>raw/5/item/image/p016-017.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/p016-017.jpg) | [<code>raw/5/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p016-017.jpg"}</code> |
| 11 | <code>[[EPUB_IMAGE:v5:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 12 | <code>[[EPUB_IMAGE:v5:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v5:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v5:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 15 | <code>[[EPUB_IMAGE:v5:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v5:xhtml/p-005.xhtml:p100-101.jpg:occ-01]]</code> | [<code>raw/5/item/image/p100-101.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/p100-101.jpg) | [<code>raw/5/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p100-101.jpg"}</code> |
| 17 | <code>[[EPUB_IMAGE:v5:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 18 | <code>[[EPUB_IMAGE:v5:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 19 | <code>[[EPUB_IMAGE:v5:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 20 | <code>[[EPUB_IMAGE:v5:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v5:xhtml/p-007.xhtml:p202-203.jpg:occ-01]]</code> | [<code>raw/5/item/image/p202-203.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/p202-203.jpg) | [<code>raw/5/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-007.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p202-203.jpg"}</code> |
| 22 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 25 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 28 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 29 | <code>[[EPUB_IMAGE:v5:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/5/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/gaiji-cid776-m-v.png) | [<code>raw/5/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 30 | <code>[[EPUB_IMAGE:v5:xhtml/p-009.xhtml:p272-273.jpg:occ-01]]</code> | [<code>raw/5/item/image/p272-273.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/p272-273.jpg) | [<code>raw/5/item/xhtml/p-009.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-009.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p272-273.jpg"}</code> |
| 31 | <code>[[EPUB_IMAGE:v5:xhtml/p-colophon.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/5/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/logo-sneaker.png) | [<code>raw/5/item/xhtml/p-colophon.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-colophon.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 32 | <code>[[EPUB_IMAGE:v5:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/5/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/image/i-bookwalker.jpg) | [<code>raw/5/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/5/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『はじまりの話』 - unknown beast -](p-001.xhtml#toc-001)

[『交わらぬ道を行け、それこそが──Ｂ』 - dancing fairies -](p-003.xhtml#toc-002)

[『死者の行く道』 - a forked road -](p-005.xhtml#toc-003)

[『絆を束ねるもの』 - union is strength -](p-007.xhtml#toc-004)

[『悪の矜持』 - the ultimate bad king -](p-009.xhtml#toc-005)

[empty paragraph]

　[あとがき／おあとがよろしいようで](p-011.xhtml#toc-006)
~~~

## Журнал пропусков и нерешённых элементов

| Категория | Число | Где описано |
|---|---:|---|
| Manifest files missing | 0 | Manifest table/warnings |
| Spine ids without manifest mapping | 0 | Spine table |
| XHTML outside spine | 0 | Section above |
| Manifest items without local reference | 1 | Manifest table |
| Image resources without main-flow marker | 0 | Image map/resource audit |
| Unmanifested files on disk | 0 | none |
| Text-layer mismatches | 0 | Full list above |
| Ruby reading sequence mismatches | 0 | Full list above |
| Ruby warnings | 0 | Full list above |
| Parse/resource warnings | 0 | Full list below |

### Полный список предупреждений

Не обнаружены.

## Для будущей сборки EPUB

Не переносить старый CSS/fixed-layout/шрифты. Собрать reflowable EPUB по instructions/pasport proekta.md, восстановить ресурсы по EPUB_IMAGE-маркерам и выполнить EPUBCheck после упаковки.
