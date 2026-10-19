# Отчёт об извлечении японского исходника — том 4

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/cover.jpg</code> | 620975 | <code>30451ef1712d6c784e90199be64c83728af2a2e85702759c9c372517c29d997f</code> |
| <code>image/gaiji-cid776-m-v.png</code> | 4828 | <code>f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf</code> |
| <code>image/gaiji-hwid-038.png</code> | 6411 | <code>48bbaa2f7a2b0118c679ea2bb462988f0e678e28eb233bd7a0c35380551e12e5</code> |
| <code>image/gaiji-num-03.png</code> | 7085 | <code>36f08e8078faefe662bbee9f6dd67d91f352f8bb83e2914e7ef1a521e0ff3116</code> |
| <code>image/gaiji-num-04.png</code> | 6628 | <code>45b5bd74bc1183f0b0da51f8e2540ad08b3e3d343a5a2bcf669958a6d677bf88</code> |
| <code>image/i-bookwalker.jpg</code> | 116828 | <code>93da8cbcf35fc14c16188ff6e325669b90ced56a14d72ce495631c76c76b6b75</code> |
| <code>image/kuchie-001.jpg</code> | 487296 | <code>d6b29b374ae9ebbc16658def14a0053de0913b7d4c2cbcc21abd78d548ac5c6f</code> |
| <code>image/kuchie-002.jpg</code> | 575744 | <code>457b3b338d294e4f0857397613b0b5c3652991303743548eab0c96d95f63ee8d</code> |
| <code>image/logo-sneaker.png</code> | 4267 | <code>3c68cdfe60118126cac64e2efc73d20294a63b7c1cece9c1adfb59553fa93f88</code> |
| <code>image/p004-005.jpg</code> | 935212 | <code>c2953ed068397bb12f9dbe0705a18317d59086a9d2e8c1a43344cbeef3cd903d</code> |
| <code>image/p014-015.jpg</code> | 1493662 | <code>9af8449888f17fd30da9bbb2f04dcbe0c88a081c3b0911920560b903117657eb</code> |
| <code>image/p114-115.jpg</code> | 1404551 | <code>caefc4da09a308f09acbdf52ca857f97efac3904cfeec42b84cc7f5384673e03</code> |
| <code>image/p214-215.jpg</code> | 1917170 | <code>d2bade078732270136bfe827f262bdc3677f5fc77415d13ead037e3a09dc3ee0</code> |
| <code>image/p268-269.jpg</code> | 1327535 | <code>aa8d053104f0337e5c7b15a2a81d992b5285db0b55236695a427f61162c31b15</code> |
| <code>image/toc-001.jpg</code> | 603115 | <code>10700cd5c65272e4f7923f4027d88f0e815b6fb39d52d60bdb710caea36dbf46</code> |
| <code>navigation-documents.xhtml</code> | 1500 | <code>b6bbca9acaec55948370742d39e12fe549af98f1557cbd676dd092fda74c4e70</code> |
| <code>standard.opf</code> | 9249 | <code>5294a6a0bb85fb05b70235e3b431d279e36a374473556058fe4b200e78394e56</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 5816 | <code>d34c878a2b279e5876a1a24d2717b73909523d5533818bc2dcd1f34bf4bec58a</code> |
| <code>style/style-karc.css</code> | 1569 | <code>4c16008a60f369029d740186aa957b960f317382331c3bb582f08fbd854051f9</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 802 | <code>6b525dd0c26cc73f2b47e7361255ecc5546f00fd33a755b720729a09237dc41b</code> |
| <code>xhtml/p-002.xhtml</code> | 14847 | <code>6a464466d64bac6612de6263206a22bebe6f70d1fb437c5cc61500698df27606</code> |
| <code>xhtml/p-003.xhtml</code> | 809 | <code>59c5a7b30e23209c2402efe3b411e2a7f98c65420b191069f2b4550381c44fab</code> |
| <code>xhtml/p-004.xhtml</code> | 179300 | <code>7a3dd119052e3ade45e23d198bbe12e3c1c496985bd5ab49ddda5c1986257f20</code> |
| <code>xhtml/p-005.xhtml</code> | 811 | <code>92d07b8bce751a669de1ad4b9db41eb3837a016be2a7ef7bf1fb060d887cac36</code> |
| <code>xhtml/p-006.xhtml</code> | 177611 | <code>e0bf93a9b9ad19c11c2e07baf0368652a755ba8d521d66a917654045ce25bbce</code> |
| <code>xhtml/p-007.xhtml</code> | 833 | <code>671db0b4a6452af7f527c6b234789cfa96f56577c66293618f9c3ae0133e7c8d</code> |
| <code>xhtml/p-008.xhtml</code> | 89594 | <code>269d0670fac24088382494b7f1bc5a66c6277af4841ad3c1aca7360acba52e28</code> |
| <code>xhtml/p-009.xhtml</code> | 816 | <code>ba5caacc9296907275c0ba61b04cb2af2e6ed63522d04f3ac6c1fafb4c1910cc</code> |
| <code>xhtml/p-010.xhtml</code> | 17212 | <code>357552b05818b438ddb6ee6815520926de2c818544bc40d9b681f02dc7a92222</code> |
| <code>xhtml/p-011.xhtml</code> | 7404 | <code>53e95ea4f79b46e2e1ed258176c995897c2ff0a5a9af212f1e3b9a5865e9d5d8</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>1757004b8dd65a767fbba5fce482c063c27d14aa4225e6dc46e91621cc1ca879</code> |
| <code>xhtml/p-caution.xhtml</code> | 1305 | <code>bc9e24d866f32b0b2d5bf5d012a5ff17ad87405d693fffe3629295f083d18288</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2114 | <code>f9fd774ded8e49f76d49b052a33380fa7573595a44d210e85659582839a2288e</code> |
| <code>xhtml/p-cover.xhtml</code> | 744 | <code>42ca115a4e37cde0262853102506753fecb9d4b3d92e60b366833c5d3b395778</code> |
| <code>xhtml/p-credit.xhtml</code> | 629 | <code>095bed95b5e55246f817aa196c4e548b1fc15b460ebb82c38ce47e1749e915ef</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 731 | <code>1dba7824d561bffe0a47d1d98061f20f0f7d25886716046ea1f43dc3d819fa6f</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 731 | <code>d8439beb8ded6ccb5d101ff6fd02fee0c6493eb9f9e8d53e1248eb2593171d1a</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 1009 | <code>c7e71e255b1cab41f0053c851ef75b08e86910fef229849550f186f381fa0890</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 728 | <code>2aeea12aa4569c70797e53515bc89d8d7f7b3ddcc1c0c8f9b78fded43317cf96</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1445 | <code>07f0c465f971fa4013a8a0743f7ded4b0c6b058f8c687c25cb77e3965542632a</code> |

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
| p114-115 | <code>image/p114-115.jpg</code> | image/jpeg | да | локальная ссылка |
| p214-215 | <code>image/p214-215.jpg</code> | image/jpeg | да | локальная ссылка |
| p268-269 | <code>image/p268-269.jpg</code> | image/jpeg | да | локальная ссылка |
| gaiji-cid776-m-v | <code>image/gaiji-cid776-m-v.png</code> | image/png | да | локальная ссылка |
| gaiji-hwid-038 | <code>image/gaiji-hwid-038.png</code> | image/png | да | локальная ссылка |
| gaiji-num-03 | <code>image/gaiji-num-03.png</code> | image/png | да | локальная ссылка |
| gaiji-num-04 | <code>image/gaiji-num-04.png</code> | image/png | да | локальная ссылка |
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
| 9 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 89 | 104 | 145 | 0 |
| 10 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 11 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 1007 | 1203 | 1771 | 6 |
| 12 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 13 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 1049 | 1176 | 1762 | 9 |
| 14 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 15 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 551 | 561 | 787 | 4 |
| 16 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 17 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 98 | 122 | 179 | 1 |
| 18 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 31 | 34 | 47 | 3 |
| 19 | <code>p-credit</code> | <code>xhtml/p-credit.xhtml</code> | parsed | 5 | 0 | 0 | 0 |
| 20 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 14 | 5 | 8 | 1 |
| 21 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-credit.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#04 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『都合の良い夢』 - delusion of dependence - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『その罪人を追え、そして』 - who is tagger? - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『語らぬ者と語れ、あるいは』 - crossing road - | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> |
| 『交わらぬ道を行け、それこそが──Ａ』 - going separated ways - | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> |
| 『沈黙する死者と雄弁な生者』 - the previous night - | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> |
| あとがき／あとがない状況で書いてます | <code>xhtml/p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 21; сопоставлены с manifest: 21.
- Абзацы p в основном потоке: 2855; пустых p, отмеченных [пауза]: 157.
- br-элементов: 157; em-sesame: 27.
- Начальных отступов снято: 1586 символов в 1481 абзацах; нестандартных случаев подробно перечислено: 34.
- CSS-классов в XHTML: 37 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 35; уникальных ресурсов в маркерах: 15.
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
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 7 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 26 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 56 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 43 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 6 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 443 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 515 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | empty/whitespace-only | 60 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | heading/style heading | 7 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | no indent / dialogue-like | 446 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | one U+3000 | 536 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 46 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 3 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 196 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 306 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 6 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 42 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 50 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 9 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | no indent / other | 2 | 30-31 |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 18 | сводный учёт |
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
| <code>xhtml/p-004.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．その日の第五師団 |
| <code>xhtml/p-004.xhtml</code> | 28 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 89 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 218 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．フェオドール・ジェスマン |
| <code>xhtml/p-004.xhtml</code> | 254 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 315 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 366 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．再会 |
| <code>xhtml/p-004.xhtml</code> | 612 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．黒スーツの少年 |
| <code>xhtml/p-004.xhtml</code> | 789 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ５．暗がりの二人 |
| <code>xhtml/p-004.xhtml</code> | 870 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ６．護翼軍第一師団 |
| <code>xhtml/p-006.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．逃走者たち |
| <code>xhtml/p-006.xhtml</code> | 13 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 111 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 179 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．駆ける少年、寄り添う少女 |
| <code>xhtml/p-006.xhtml</code> | 189 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 209 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 267 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 288 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．オデット・グンダカールという女 |
| <code>xhtml/p-006.xhtml</code> | 440 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 449 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．おしゃれな街でのおしゃれな間食 |
| <code>xhtml/p-006.xhtml</code> | 552 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ５．鬼たちのティーパーティ |
| <code>xhtml/p-006.xhtml</code> | 704 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ６．ラキシュ |
| <code>xhtml/p-006.xhtml</code> | 749 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 792 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 857 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ７．黒い同行者 |
| <code>xhtml/p-006.xhtml</code> | 943 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．それから |
| <code>xhtml/p-008.xhtml</code> | 15 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 163 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．愛し合わない二人は |
| <code>xhtml/p-008.xhtml</code> | 209 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 390 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 429 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．交じり合う少女二人 |
| <code>xhtml/p-008.xhtml</code> | 510 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 25 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 2 |
| book-title | div | 2 |
| book-title-main | div | 2 |
| copyright | div | 1 |
| em-sesame | span | 27 |
| font-0em90 | span | 1 |
| font-1em10 | p | 16 |
| font-1em10 | span | 6 |
| font-1em30 | p | 1 |
| font-1em30 | span | 1 |
| gaiji | img | 23 |
| gfont | div | 3 |
| gfont | span | 7 |
| hltr | html | 2 |
| label | div | 2 |
| label-logo | p | 2 |
| label-name | p | 1 |
| main | div | 21 |
| mfont | div | 1 |
| mfont | p | 17 |
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
| start-2em | div | 3 |
| tcy | span | 67 |
| vrtl | html | 9 |
| word-break-break-all | span | 23 |

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
| <code>xhtml/p-003.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../image/p014-015.jpg</code> | <code>image/p014-015.jpg</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-hwid-038.png</code> | <code>image/gaiji-hwid-038.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-hwid-038.png</code> | <code>image/gaiji-hwid-038.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/p114-115.jpg</code> | <code>image/p114-115.jpg</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/p214-215.jpg</code> | <code>image/p214-215.jpg</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../image/p268-269.jpg</code> | <code>image/p268-269.jpg</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../image/gaiji-num-04.png</code> | <code>image/gaiji-num-04.png</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../image/gaiji-num-04.png</code> | <code>image/gaiji-num-04.png</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../image/gaiji-num-03.png</code> | <code>image/gaiji-num-03.png</code> | OK |
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
| 1 | <code>[[EPUB_IMAGE:v4:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/4/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/cover.jpg) | [<code>raw/4/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v4:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/4/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/kuchie-001.jpg) | [<code>raw/4/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2003", "height": "1600", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v4:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/4/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/kuchie-002.jpg) | [<code>raw/4/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2004", "height": "1600", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v4:xhtml/p-titlepage.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/4/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/logo-sneaker.png) | [<code>raw/4/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 5 | <code>[[EPUB_IMAGE:v4:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/4/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/toc-001.jpg) | [<code>raw/4/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2255", "height": "1600", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v4:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/4/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p004-005.jpg) | [<code>raw/4/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p004-005.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v4:xhtml/p-003.xhtml:p014-015.jpg:occ-01]]</code> | [<code>raw/4/item/image/p014-015.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p014-015.jpg) | [<code>raw/4/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p014-015.jpg"}</code> |
| 8 | <code>[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 9 | <code>[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 10 | <code>[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-hwid-038.png:occ-03]]</code> | [<code>raw/4/item/image/gaiji-hwid-038.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-hwid-038.png) | [<code>raw/4/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] 番浮遊島に居を構える護翼軍第五師団総団長は、小声でぼやく。 | <code>{"class": "gaiji", "src": "../image/gaiji-hwid-038.png", "alt": ""}</code> |
| 11 | <code>[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 12 | <code>[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-hwid-038.png:occ-05]]</code> | [<code>raw/4/item/image/gaiji-hwid-038.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-hwid-038.png) | [<code>raw/4/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | まだ [IMAGE] 番浮遊島でやることがあるのではないのか、と言われた。 | <code>{"class": "gaiji", "src": "../image/gaiji-hwid-038.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v4:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v4:xhtml/p-005.xhtml:p114-115.jpg:occ-01]]</code> | [<code>raw/4/item/image/p114-115.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p114-115.jpg) | [<code>raw/4/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2224", "height": "1600", "href": "../image/p114-115.jpg"}</code> |
| 15 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 17 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 18 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 19 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 20 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 22 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v4:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v4:xhtml/p-007.xhtml:p214-215.jpg:occ-01]]</code> | [<code>raw/4/item/image/p214-215.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p214-215.jpg) | [<code>raw/4/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-007.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p214-215.jpg"}</code> |
| 25 | <code>[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 28 | <code>[[EPUB_IMAGE:v4:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 29 | <code>[[EPUB_IMAGE:v4:xhtml/p-009.xhtml:p268-269.jpg:occ-01]]</code> | [<code>raw/4/item/image/p268-269.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/p268-269.jpg) | [<code>raw/4/item/xhtml/p-009.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-009.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p268-269.jpg"}</code> |
| 30 | <code>[[EPUB_IMAGE:v4:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/4/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-cid776-m-v.png) | [<code>raw/4/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 31 | <code>[[EPUB_IMAGE:v4:xhtml/p-011.xhtml:gaiji-num-04.png:occ-01]]</code> | [<code>raw/4/item/image/gaiji-num-04.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-num-04.png) | [<code>raw/4/item/xhtml/p-011.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-011.xhtml) | gaiji (класс XHTML; глиф не проверен) | すが、いちおう一冊の中でひとつのエピソードを閉じる形は保ってきていました。が、今回はちょっとその辺り事情が違いまして、「 [IMAGE] 」で始まった一番大きなエピソードが、「」の中で完結していません。続きます。上下巻みたいなタイトルのつき方にはなってません | <code>{"class": "gaiji", "src": "../image/gaiji-num-04.png", "alt": ""}</code> |
| 32 | <code>[[EPUB_IMAGE:v4:xhtml/p-011.xhtml:gaiji-num-04.png:occ-02]]</code> | [<code>raw/4/item/image/gaiji-num-04.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-num-04.png) | [<code>raw/4/item/xhtml/p-011.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-011.xhtml) | gaiji (класс XHTML; глиф не проверен) | ードを閉じる形は保ってきていました。が、今回はちょっとその辺り事情が違いまして、「」で始まった一番大きなエピソードが、「 [IMAGE] 」の中で完結していません。続きます。上下巻みたいなタイトルのつき方にはなってませんが、イメージとしては近い感じです。それ | <code>{"class": "gaiji", "src": "../image/gaiji-num-04.png", "alt": ""}</code> |
| 33 | <code>[[EPUB_IMAGE:v4:xhtml/p-011.xhtml:gaiji-num-03.png:occ-03]]</code> | [<code>raw/4/item/image/gaiji-num-03.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/gaiji-num-03.png) | [<code>raw/4/item/xhtml/p-011.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-011.xhtml) | gaiji (класс XHTML; глиф не проверен) | そして、前巻「 [IMAGE] 」のあとがきでも触れましたが、今回から本格的に、前シリーズ『終末なにしてますか？　忙しいですか？　救ってもらっていいです | <code>{"class": "gaiji", "src": "../image/gaiji-num-03.png", "alt": ""}</code> |
| 34 | <code>[[EPUB_IMAGE:v4:xhtml/p-colophon.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/4/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/logo-sneaker.png) | [<code>raw/4/item/xhtml/p-colophon.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-colophon.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 35 | <code>[[EPUB_IMAGE:v4:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/4/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/image/i-bookwalker.jpg) | [<code>raw/4/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/4/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『都合の良い夢』 - delusion of dependence -](p-001.xhtml#toc-001)

[『その罪人を追え、そして』 - who is tagger? -](p-003.xhtml#toc-002)

[『語らぬ者と語れ、あるいは』 - crossing road -](p-005.xhtml#toc-003)

[『交わらぬ道を行け、それこそが──Ａ』 - going separated ways -](p-007.xhtml#toc-004)

[『沈黙する死者と雄弁な生者』 - the previous night -](p-009.xhtml#toc-005)

[empty paragraph]

　[あとがき／あとがない状況で書いてます](p-011.xhtml#toc-006)
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
