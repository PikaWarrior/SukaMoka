# Отчёт об извлечении японского исходника — том 3

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/cover.jpg</code> | 792903 | <code>632beec4f40f5add7172a020ac5d77eeac71d4a9f428ea08fd666448c61dc617</code> |
| <code>image/gaiji-0001.png</code> | 6526 | <code>13b1fde2be79e9d08c2993ea2ac8629bc2f271425a41ed9983b356f3772df9fa</code> |
| <code>image/gaiji-cid776-m-v.png</code> | 4828 | <code>f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf</code> |
| <code>image/i-bookwalker.jpg</code> | 116828 | <code>93da8cbcf35fc14c16188ff6e325669b90ced56a14d72ce495631c76c76b6b75</code> |
| <code>image/kuchie-001.jpg</code> | 641296 | <code>cb74ba861c706da511b382057066eece08782e5306bbf4a65e06e3de2d4344b3</code> |
| <code>image/kuchie-002.jpg</code> | 534390 | <code>188b37ba0c4c18f275e9a025a996a8fd2d3b0cd9dddb07edf2fce178a8d2861e</code> |
| <code>image/logo-sneaker.png</code> | 4267 | <code>3c68cdfe60118126cac64e2efc73d20294a63b7c1cece9c1adfb59553fa93f88</code> |
| <code>image/p004-005.jpg</code> | 1461877 | <code>57d5b33a9b87c68b3a48bf3cb4eae1d7f1915e597d0adf89676a1de4244129bf</code> |
| <code>image/p014-015.jpg</code> | 1337627 | <code>150c9a92911b9a812961051d937da991c328388478552f5a00f4e9bf8a43c7fe</code> |
| <code>image/p102-103.jpg</code> | 1362875 | <code>1f4c05582151f1ba1852a2ad1d762c899644d48e9bb87ddd1961544ed45fd27e</code> |
| <code>image/p204-205.jpg</code> | 1295101 | <code>62b1201f02d227e342ae67a1316247406876158e7baab142ce6f9e60147fabd4</code> |
| <code>image/p272-273.jpg</code> | 1188574 | <code>9a5dd40d588a10a03812909c417b30e25d3a405dcd19f34e52e4ccb3f2e44222</code> |
| <code>image/toc-001.jpg</code> | 683597 | <code>05eb99ce8b7324d19ed66f0641ad1c83c11a4a6013fc89c81b4141b52a53359c</code> |
| <code>navigation-documents.xhtml</code> | 1449 | <code>3a705224e2ab533d43878eed622326eca8f6c1bad24912e400f08869097dfe14</code> |
| <code>standard.opf</code> | 9051 | <code>d143919fc28ac4a503f7949e33839ab821bb02d2eef5f895526013739840c6e0</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 5816 | <code>d34c878a2b279e5876a1a24d2717b73909523d5533818bc2dcd1f34bf4bec58a</code> |
| <code>style/style-karc.css</code> | 1569 | <code>4c16008a60f369029d740186aa957b960f317382331c3bb582f08fbd854051f9</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 797 | <code>0b14c47fb2845ded3e79a0d89be82fafd02f13973008ae8cac91d5b8c0870621</code> |
| <code>xhtml/p-002.xhtml</code> | 17370 | <code>bc6f6cba36ae77c3f7b512dc1c54d578687681e6edc989d17ab4cc112e7d9f84</code> |
| <code>xhtml/p-003.xhtml</code> | 811 | <code>7c3a0a23f51614183b333b4b4b2bebb39daf5385f44e641080126d73510a971f</code> |
| <code>xhtml/p-004.xhtml</code> | 156198 | <code>b2849ea38a866f8b6a7c6cbbd5275c101986966331a45af1cd3fee4cb7002aac</code> |
| <code>xhtml/p-005.xhtml</code> | 809 | <code>6ec8221cd5024b56e1321f12c58e17cf10e41747b8b2a97f9ed48acbaf935cf5</code> |
| <code>xhtml/p-006.xhtml</code> | 169582 | <code>be472661bd2038e6f81f3ff89d52b33f09afc4c5f7916eddba35de807bb48ac6</code> |
| <code>xhtml/p-007.xhtml</code> | 804 | <code>2a094b4ce8b0baecf6219de7c20df62195a37c169673ae0451b146600e52f0a6</code> |
| <code>xhtml/p-008.xhtml</code> | 113149 | <code>a53ae67d40a723e4a26761ff019bc6d0930da9cf8fefb851b8a583ea4884d2ee</code> |
| <code>xhtml/p-009.xhtml</code> | 802 | <code>6d1dfe403177f22bfc22e93d7a3eb6a9e2eca5a80810d99dba3b4723080cc017</code> |
| <code>xhtml/p-010.xhtml</code> | 11889 | <code>30415ad2a9272a3e0b1b80c114941c47bb445ac55903fdd366323a9e1533540e</code> |
| <code>xhtml/p-011.xhtml</code> | 9127 | <code>bdf02a7130883401c20d463a1a24064c0f4c3b0a71ae755a372484343de7c44a</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>1757004b8dd65a767fbba5fce482c063c27d14aa4225e6dc46e91621cc1ca879</code> |
| <code>xhtml/p-caution.xhtml</code> | 1305 | <code>bc9e24d866f32b0b2d5bf5d012a5ff17ad87405d693fffe3629295f083d18288</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2116 | <code>51a78e00a09c61085870bb35ca15ee70acabe08853e370598d46d7006c75e292</code> |
| <code>xhtml/p-cover.xhtml</code> | 744 | <code>407dab20d5e60c3f114ffd0057d99349d8475d7cb64dc32ca1ce2b9661a170bd</code> |
| <code>xhtml/p-credit.xhtml</code> | 677 | <code>5ecd47250f42ef57aaef9b171ca1c037149659b512915d10f04eba58fe92e764</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 731 | <code>5a015e0f9d6d33ef4e12758d4b04e9d2f8f93d5a5568d5ee5aae6487e43afdfa</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 731 | <code>f6746b3aae23b5f1d8dca10b64edcbf29177a062b6f0228ec646235d00962ea3</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 1009 | <code>811106679c8be37206f3957337d05238852f4a88eaaa3d033dd74791e650c95e</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 728 | <code>03c4b37fb42ab0ce9a4305e515e56fb02772aab6620ddfab3e6bddb18805cdb7</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1394 | <code>9b5dc62a26344cec9100fd81e1976a00dbd0a4f50ae87818556e1cd32d17f3aa</code> |

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
| p014-015 | <code>image/p014-015.jpg</code> | image/jpeg | да | локальная ссылка |
| p102-103 | <code>image/p102-103.jpg</code> | image/jpeg | да | локальная ссылка |
| p204-205 | <code>image/p204-205.jpg</code> | image/jpeg | да | локальная ссылка |
| p272-273 | <code>image/p272-273.jpg</code> | image/jpeg | да | локальная ссылка |
| gaiji-0001 | <code>image/gaiji-0001.png</code> | image/png | да | локальная ссылка |
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
| 1 | <code>p-cover</code> | <code>xhtml/p-cover.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 2 | <code>p-fmatter-001</code> | <code>xhtml/p-fmatter-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 3 | <code>p-fmatter-002</code> | <code>xhtml/p-fmatter-002.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 4 | <code>p-titlepage</code> | <code>xhtml/p-titlepage.xhtml</code> | parsed | 4 | 0 | 0 | 1 |
| 5 | <code>p-caution</code> | <code>xhtml/p-caution.xhtml</code> | parsed | 7 | 0 | 0 | 0 |
| 6 | <code>p-toc-001</code> | <code>xhtml/p-toc-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 7 | <code>p-toc-002</code> | <code>xhtml/p-toc-002.xhtml</code> | TOC logged below, not repeated | 0 | 0 | 0 | 0 |
| 8 | <code>p-001</code> | <code>xhtml/p-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 9 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 82 | 149 | 213 | 2 |
| 10 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 11 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 884 | 1080 | 1577 | 8 |
| 12 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 13 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 1146 | 1103 | 1579 | 5 |
| 14 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 15 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 744 | 774 | 1085 | 3 |
| 16 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 17 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 85 | 84 | 112 | 0 |
| 18 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 42 | 53 | 70 | 1 |
| 19 | <code>p-credit</code> | <code>xhtml/p-credit.xhtml</code> | parsed | 5 | 0 | 0 | 0 |
| 20 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 14 | 5 | 8 | 1 |
| 21 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-credit.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#03 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『少しだけ、昔の話』 - broken bond - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『それでも今日を生きていく』 - stained glass - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『明日に向かって歩き出す』 - chained hearts - | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> |
| 『邪魔をしてやる』 - standing back to back - | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> |
| 『迷子の子猫』 - being hungry for kindness - | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> |
| あとがき／の名を借りたＣＭコーナー | <code>xhtml/p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 21; сопоставлены с manifest: 21.
- Абзацы p в основном потоке: 3013; пустых p, отмеченных [пауза]: 171.
- br-элементов: 171; em-sesame: 20.
- Начальных отступов снято: 1782 символов в 1675 абзацах; нестандартных случаев подробно перечислено: 35.
- CSS-классов в XHTML: 38 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 31; уникальных ресурсов в маркерах: 13.
- Изображений manifest без маркера в spine XHTML: 0.
- Расхождений текстового слоя абзацев: 0; расхождений порядка ruby-чтений: 0; ruby warnings: 0.
- Неизвестных элементов: 0; XML-комментариев: 17; processing instructions: 0.
- Литеральных символов 〔〕 вне rt: 0; предупреждений: 0.

### Расхождения текстового слоя

Не обнаружены.

### Профиль начальных отступов

Для компактности стандартный отступ из одного U+3000 агрегирован по количеству. Все абзацы без отступа, не похожие на реплики/заголовки, перечислены по номерам; все удалённые отступы нестандартной длины приведены в подробной таблице ниже.

| XHTML | Категория | Количество p | Номера p (для потенциальных исключений) |
|---|---|---:|---|
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 11 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 16 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 55 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 67 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 4 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 262 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 551 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | empty/whitespace-only | 52 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | heading/style heading | 7 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | no indent / dialogue-like | 505 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | one U+3000 | 582 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 40 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 6 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 287 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 411 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 5 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 29 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 51 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 10 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | no indent / dialogue-like | 4 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | no indent / other | 2 | 41-42 |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 25 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 6 | 1-4, 6-7 |
| <code>xhtml/p-colophon.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 13 | 1-2, 4-14 |
| <code>xhtml/p-credit.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-credit.xhtml</code> | no indent / other | 2 | 4-5 |
| <code>xhtml/p-titlepage.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-titlepage.xhtml</code> | no indent / other | 3 | 1-2, 4 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-002.xhtml</code> | 11 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-002.xhtml</code> | 76 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．笑顔の仮面 |
| <code>xhtml/p-004.xhtml</code> | 46 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 64 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 143 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 228 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．浮遊大陸群の敵 |
| <code>xhtml/p-004.xhtml</code> | 434 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 468 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．還り来る者 |
| <code>xhtml/p-004.xhtml</code> | 536 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 572 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 659 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．輝く瞳 |
| <code>xhtml/p-004.xhtml</code> | 690 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 765 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．冷たい雨の降る街 |
| <code>xhtml/p-006.xhtml</code> | 101 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 274 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 415 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．眠れない夜 |
| <code>xhtml/p-006.xhtml</code> | 494 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．総団長室 |
| <code>xhtml/p-006.xhtml</code> | 550 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．朝早く |
| <code>xhtml/p-006.xhtml</code> | 718 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ５．偽りの赤 |
| <code>xhtml/p-006.xhtml</code> | 743 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 830 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 876 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ６．ベーコンとサラダとオレンジジュース |
| <code>xhtml/p-006.xhtml</code> | 994 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 1030 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ７．死せる黒瑪瑙 |
| <code>xhtml/p-008.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．機械仕掛けで強かった女 |
| <code>xhtml/p-008.xhtml</code> | 62 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．ティアット |
| <code>xhtml/p-008.xhtml</code> | 168 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．囚われの叛逆者 |
| <code>xhtml/p-008.xhtml</code> | 180 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 320 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．憧れの先輩 |
| <code>xhtml/p-008.xhtml</code> | 338 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 451 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ５．立ちふさがる者 |
| <code>xhtml/p-008.xhtml</code> | 503 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 681 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ６．今、その隣に立つ者 |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 2 |
| book-title | div | 2 |
| book-title-main | div | 2 |
| copyright | div | 1 |
| em-sesame | span | 20 |
| font-0em90 | span | 1 |
| font-1em10 | p | 17 |
| font-1em10 | span | 6 |
| font-1em30 | p | 1 |
| font-1em30 | span | 1 |
| gaiji | img | 19 |
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
| publish-phone | p | 1 |
| publish-reception | p | 1 |
| publish-url | p | 1 |
| publisher-data | div | 1 |
| release-date | div | 1 |
| start-2em | div | 2 |
| start-3em | div | 1 |
| tcy | span | 45 |
| vrtl | html | 9 |
| word-break-break-all | span | 7 |

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
| <code>xhtml/p-003.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../image/p014-015.jpg</code> | <code>image/p014-015.jpg</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/p102-103.jpg</code> | <code>image/p102-103.jpg</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/p204-205.jpg</code> | <code>image/p204-205.jpg</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../image/p272-273.jpg</code> | <code>image/p272-273.jpg</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../image/gaiji-0001.png</code> | <code>image/gaiji-0001.png</code> | OK |
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
| 1 | <code>[[EPUB_IMAGE:v3:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/3/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/cover.jpg) | [<code>raw/3/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v3:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/3/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/kuchie-001.jpg) | [<code>raw/3/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2005", "height": "1600", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v3:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/3/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/kuchie-002.jpg) | [<code>raw/3/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2009", "height": "1600", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v3:xhtml/p-titlepage.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/3/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/logo-sneaker.png) | [<code>raw/3/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 5 | <code>[[EPUB_IMAGE:v3:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/3/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/toc-001.jpg) | [<code>raw/3/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v3:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/3/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/p004-005.jpg) | [<code>raw/3/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p004-005.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v3:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 8 | <code>[[EPUB_IMAGE:v3:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 9 | <code>[[EPUB_IMAGE:v3:xhtml/p-003.xhtml:p014-015.jpg:occ-01]]</code> | [<code>raw/3/item/image/p014-015.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/p014-015.jpg) | [<code>raw/3/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2224", "height": "1600", "href": "../image/p014-015.jpg"}</code> |
| 10 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 11 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 12 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 15 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 17 | <code>[[EPUB_IMAGE:v3:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 18 | <code>[[EPUB_IMAGE:v3:xhtml/p-005.xhtml:p102-103.jpg:occ-01]]</code> | [<code>raw/3/item/image/p102-103.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/p102-103.jpg) | [<code>raw/3/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p102-103.jpg"}</code> |
| 19 | <code>[[EPUB_IMAGE:v3:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 20 | <code>[[EPUB_IMAGE:v3:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v3:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 22 | <code>[[EPUB_IMAGE:v3:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v3:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v3:xhtml/p-007.xhtml:p204-205.jpg:occ-01]]</code> | [<code>raw/3/item/image/p204-205.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/p204-205.jpg) | [<code>raw/3/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-007.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p204-205.jpg"}</code> |
| 25 | <code>[[EPUB_IMAGE:v3:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v3:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v3:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/3/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-cid776-m-v.png) | [<code>raw/3/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 28 | <code>[[EPUB_IMAGE:v3:xhtml/p-009.xhtml:p272-273.jpg:occ-01]]</code> | [<code>raw/3/item/image/p272-273.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/p272-273.jpg) | [<code>raw/3/item/xhtml/p-009.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-009.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p272-273.jpg"}</code> |
| 29 | <code>[[EPUB_IMAGE:v3:xhtml/p-011.xhtml:gaiji-0001.png:occ-01]]</code> | [<code>raw/3/item/image/gaiji-0001.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/gaiji-0001.png) | [<code>raw/3/item/xhtml/p-011.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-011.xhtml) | gaiji (класс XHTML; глиф не проверен) | いろいろ進行がうまくいけば、おそらく『終末なにしてますか？　忙しいですか？　救ってもらっていいですか？　 [IMAGE] 』みたいなタイトルで、来年２月には皆さまのもとにお届けできると思います。よろしくお願いします。 | <code>{"class": "gaiji", "src": "../image/gaiji-0001.png", "alt": ""}</code> |
| 30 | <code>[[EPUB_IMAGE:v3:xhtml/p-colophon.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/3/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/logo-sneaker.png) | [<code>raw/3/item/xhtml/p-colophon.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-colophon.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 31 | <code>[[EPUB_IMAGE:v3:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/3/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/image/i-bookwalker.jpg) | [<code>raw/3/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/3/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『少しだけ、昔の話』 - broken bond -](p-001.xhtml#toc-001)

[『それでも今日を生きていく』 - stained glass -](p-003.xhtml#toc-002)

[『明日に向かって歩き出す』 - chained hearts -](p-005.xhtml#toc-003)

[『邪魔をしてやる』 - standing back to back -](p-007.xhtml#toc-004)

[『迷子の子猫』 - being hungry for kindness -](p-009.xhtml#toc-005)

[empty paragraph]

　[あとがき／の名を借りたＣＭコーナー](p-011.xhtml#toc-006)
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
