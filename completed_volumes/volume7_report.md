# Отчёт об извлечении японского исходника — том 7

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/allcover-001.jpg</code> | 333052 | <code>2563ae111725b0b6295470d016ae0369c0cb0ba2048c827d425c86c9aa3c1274</code> |
| <code>image/cover.jpg</code> | 961179 | <code>407e5b6ae5f04f741e67e4adafa462713fa3f0a79404930c07186a93901947bd</code> |
| <code>image/gaiji-cid7699-m-v.png</code> | 6354 | <code>0c2ffa495e4a10dd4b8b08977e6fa58eda0fba7a98f9c0e1152b904028fc5c9b</code> |
| <code>image/gaiji-cid776-m-v.png</code> | 4828 | <code>f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf</code> |
| <code>image/i-bookwalker.jpg</code> | 342205 | <code>7cd722f5a19b77ac2c3b9e336a39ecc9803b7a4263dd236f4e8253f15adf2a4a</code> |
| <code>image/kuchie-001.jpg</code> | 928362 | <code>93b354a1a053706032db24982aa3a5eb7988a6b66541568e9293f0959a5344ee</code> |
| <code>image/kuchie-002.jpg</code> | 948818 | <code>e232f81a7ffa2197361a7d15c9896852e32ab4dd613f179b5a8c90e3a69adf3c</code> |
| <code>image/p004-005.jpg</code> | 622966 | <code>54178babc79257a71e36604e2d5d5cdb736313eefd7c24b11398905dcd03a9bb</code> |
| <code>image/p012-013.jpg</code> | 584662 | <code>b75938f4b8eca72089009abd957151c5b179f80139ac14b367e5f490a6f8c7d7</code> |
| <code>image/p104-105.jpg</code> | 636725 | <code>303e242b90ce8252d694e77ee76ad5416c8703dd9eedcb9a66f691968ff234a4</code> |
| <code>image/p216-217.jpg</code> | 411512 | <code>aa9eebcd9a4e23a7ca08b51e41ef4c5f9ea6049f9bdd1adfdedb3bed0c565787</code> |
| <code>image/p340-341.jpg</code> | 722814 | <code>3e9d5d6f97274bda1b17a870194828581ba93495215a26b0d682ec4ea19f76ea</code> |
| <code>image/titlepage.jpg</code> | 121663 | <code>00628cc4673ad5b87952989478558ce35dbe6e44914b1de4889f2d233a0c9f2b</code> |
| <code>image/toc-001.jpg</code> | 759521 | <code>e9c02f739a91ee0e5a2cbfc4774e027930dcf803b7c860efc6824d660f4012f1</code> |
| <code>navigation-documents.xhtml</code> | 1423 | <code>931cf90e47802e900c9b7ee4f07aa1420f66ebe057e0f450aa100764acf2cf08</code> |
| <code>standard.opf</code> | 9776 | <code>b1a37017ce2947cd3b80f37ee5c4fb35c2a59d8726657ad96e54c8070c731b8f</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 6959 | <code>c821f50d6cdb8e87fc6f45984e2acbef611f4f115ad9de598c8dead3758f4142</code> |
| <code>style/style-karc.css</code> | 1927 | <code>067ce6303605275a60389c7fb8cd59ef0ca47b6ba8eebe6f6438686f1f67552a</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 810 | <code>8cbf9f7d17a9c2acf062dc2427b17cc5c3bf2c41bd696a64e067e4fe313f3fd1</code> |
| <code>xhtml/p-002.xhtml</code> | 9858 | <code>90121b9d94a30f8c63efc93a9ed672f84664964faa21e1eeac7af6956bf692e6</code> |
| <code>xhtml/p-003.xhtml</code> | 791 | <code>9e4612b96cdabfef1b6d301d4020ad78503b48fdf8b36e0d4baae715af5819ff</code> |
| <code>xhtml/p-004.xhtml</code> | 168708 | <code>eff93d843b95a05b0394452948429fcd8390d7cf72f89e508ebe8f3f539952c6</code> |
| <code>xhtml/p-005.xhtml</code> | 795 | <code>5c5ddb1edab1896dc0e9bb1053662c44be466b2d25355e7f3113c9f70c36ef66</code> |
| <code>xhtml/p-006.xhtml</code> | 203244 | <code>57800bd99777bd0efea8ccbdbb459aef3c2839e0d37547d50abb3d9acc09df0d</code> |
| <code>xhtml/p-007.xhtml</code> | 811 | <code>62bd2eeac231f125b00f1051604f7e6a19b7e42c86d8100ea3b28582bf943046</code> |
| <code>xhtml/p-008.xhtml</code> | 169866 | <code>1234a1bfc8c6edd589ec1ab929ed1e4efd63fa9f9607c12191ae6a6388995cc3</code> |
| <code>xhtml/p-009.xhtml</code> | 552 | <code>525b04ee7d145bb13cc108f93720be38b660b5af2f40c05d333ff3254356ebe8</code> |
| <code>xhtml/p-010.xhtml</code> | 45617 | <code>ff36696bc14c632e46388129ec77633cfd724ddc40de4ac7a140559a83b7c925</code> |
| <code>xhtml/p-011.xhtml</code> | 786 | <code>5f5a4201bade2962c0bd80ab9934aba93dbde6d6a41f4a9ef4130dcd216be96d</code> |
| <code>xhtml/p-012.xhtml</code> | 13906 | <code>9c2bd58b07cb2a96bfb787c252843c3898323c320305b1169aa95beb60d01de1</code> |
| <code>xhtml/p-013.xhtml</code> | 6047 | <code>b498f3e76b536c5b595dcda9366c70a6332f6db89ad15e69cdc6daceb01e0df3</code> |
| <code>xhtml/p-allcover-001.xhtml</code> | 728 | <code>44e3c9267c9fa36938ba798bc9e6c143164a7916a8c94338d1919a29be91fcef</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>65719179002ebb0468c3ba14986dda2049ad4c6a087daba3350b8c2189eeb97d</code> |
| <code>xhtml/p-caution.xhtml</code> | 777 | <code>fc6d7b7dcefe7db874df13190bbdb6574ec5157913455b77bfd7917bcb68d08f</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2045 | <code>8744d900d3c7774ba826db15a3fd14419d7fe6071fc3cb5c324ea7440b564aae</code> |
| <code>xhtml/p-colophon2.xhtml</code> | 1026 | <code>f7f9b2a483bdc67e877d096c5afbae6cb6f5145a51d066d4060acb88da26b27b</code> |
| <code>xhtml/p-cover.xhtml</code> | 742 | <code>3d8dd89b49d8c7719436443a3b8c4ea885e67b6040b9f97a12b8aaffdab8a563</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 729 | <code>ea28dfe151f29d28ad9c7b7a1ca5484cbcfe37303729afae923002da3cf437e4</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 729 | <code>366477df183c13edb91ef017dc2303f8d5e5a0b71d030348d55e23e5f04e2229</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 728 | <code>563692262c98abe7b4c573458974bc7f095fe73c0ec03156e0a82dc9343a0b38</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 726 | <code>6cab16d0e7f73f2abe4fb672bd4d385786f02e1618cb56dc53418bd9c15c9c00</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1349 | <code>7cb337f8a9e22dcab39128f8ba8a5688b4671e02fffe52b63ccc50dc32766743</code> |

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
| titlepage | <code>image/titlepage.jpg</code> | image/jpeg | да | локальная ссылка |
| toc-001 | <code>image/toc-001.jpg</code> | image/jpeg | да | локальная ссылка |
| p004-005 | <code>image/p004-005.jpg</code> | image/jpeg | да | локальная ссылка |
| p012-013 | <code>image/p012-013.jpg</code> | image/jpeg | да | локальная ссылка |
| p104-105 | <code>image/p104-105.jpg</code> | image/jpeg | да | локальная ссылка |
| p216-217 | <code>image/p216-217.jpg</code> | image/jpeg | да | локальная ссылка |
| p340-341 | <code>image/p340-341.jpg</code> | image/jpeg | да | локальная ссылка |
| gaiji-cid7699-m-v | <code>image/gaiji-cid7699-m-v.png</code> | image/png | да | локальная ссылка |
| gaiji-cid776-m-v | <code>image/gaiji-cid776-m-v.png</code> | image/png | да | локальная ссылка |
| allcover-001 | <code>image/allcover-001.jpg</code> | image/jpeg | да | локальная ссылка |
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
| p-009 | <code>xhtml/p-009.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-010 | <code>xhtml/p-010.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-011 | <code>xhtml/p-011.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-012 | <code>xhtml/p-012.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-013 | <code>xhtml/p-013.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-allcover-001 | <code>xhtml/p-allcover-001.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-colophon | <code>xhtml/p-colophon.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-colophon2 | <code>xhtml/p-colophon2.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-bookwalker | <code>xhtml/p-bookwalker.xhtml</code> | application/xhtml+xml | да | package metadata: spine |

## Spine

| № | idref | XHTML | Статус | p | ruby | rt | img/image |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | <code>p-cover</code> | <code>xhtml/p-cover.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 2 | <code>p-fmatter-001</code> | <code>xhtml/p-fmatter-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 3 | <code>p-fmatter-002</code> | <code>xhtml/p-fmatter-002.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 4 | <code>p-titlepage</code> | <code>xhtml/p-titlepage.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 5 | <code>p-caution</code> | <code>xhtml/p-caution.xhtml</code> | parsed | 4 | 0 | 0 | 0 |
| 6 | <code>p-toc-001</code> | <code>xhtml/p-toc-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 7 | <code>p-toc-002</code> | <code>xhtml/p-toc-002.xhtml</code> | TOC logged below, not repeated | 0 | 0 | 0 | 0 |
| 8 | <code>p-001</code> | <code>xhtml/p-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 9 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 55 | 71 | 97 | 0 |
| 10 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 11 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 937 | 1235 | 1834 | 11 |
| 12 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 13 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 1091 | 1402 | 2079 | 9 |
| 14 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 15 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 986 | 1209 | 1815 | 10 |
| 16 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 4 | 0 | 0 | 0 |
| 17 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 290 | 293 | 424 | 3 |
| 18 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 19 | <code>p-012</code> | <code>xhtml/p-012.xhtml</code> | parsed | 56 | 119 | 169 | 0 |
| 20 | <code>p-013</code> | <code>xhtml/p-013.xhtml</code> | parsed | 22 | 32 | 42 | 0 |
| 21 | <code>p-allcover-001</code> | <code>xhtml/p-allcover-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 22 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 13 | 5 | 8 | 0 |
| 23 | <code>p-colophon2</code> | <code>xhtml/p-colophon2.xhtml</code> | parsed | 3 | 0 | 0 | 0 |
| 24 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-012.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-013.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-allcover-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-colophon2.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#07 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『おばけが目覚めた話』 - through the dark nights - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『翠緑の英雄譚』 - braves' story - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『終末の箱庭』 - approaching worldend - | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> |
| 『隣に立つ者、結ばれる手と手』 - bond of morn - | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> |
| 『雨烟る夜』 - masked deadman - | <code>xhtml/p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> |
| あとがき／と推測されている何か | <code>xhtml/p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 24; сопоставлены с manifest: 24.
- Абзацы p в основном потоке: 3461; пустых p, отмеченных [пауза]: 239.
- br-элементов: 239; em-sesame: 27.
- Начальных отступов снято: 2110 символов в 1982 абзацах; нестандартных случаев подробно перечислено: 32.
- CSS-классов в XHTML: 39 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 45; уникальных ресурсов в маркерах: 14.
- Изображений manifest без маркера в spine XHTML: 0.
- Расхождений текстового слоя абзацев: 0; расхождений порядка ruby-чтений: 0; ruby warnings: 0.
- Неизвестных элементов: 0; XML-комментариев: 15; processing instructions: 0.
- Литеральных символов 〔〕 вне rt: 0; предупреждений: 0.

### Расхождения текстового слоя

Не обнаружены.

### Профиль начальных отступов

Для компактности стандартный отступ из одного U+3000 агрегирован по количеству. Все абзацы без отступа, не похожие на реплики/заголовки, перечислены по номерам; все удалённые отступы нестандартной длины приведены в подробной таблице ниже.

| XHTML | Категория | Количество p | Номера p (для потенциальных исключений) |
|---|---|---:|---|
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 5 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 5 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 45 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 75 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 5 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 297 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 560 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | empty/whitespace-only | 67 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | heading/style heading | 6 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | no indent / dialogue-like | 482 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | one U+3000 | 536 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 87 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 6 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 267 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 626 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 27 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | heading/style heading | 2 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 103 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 158 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | empty/whitespace-only | 2 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | no indent / dialogue-like | 12 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | one U+3000 | 42 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | empty/whitespace-only | 4 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | no indent / other | 2 | 21-22 |
| <code>xhtml/p-013.xhtml</code> | one U+3000 | 15 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 3 | 1, 3-4 |
| <code>xhtml/p-colophon.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 12 | 1-12 |
| <code>xhtml/p-colophon2.xhtml</code> | no indent / other | 3 | 1-3 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-004.xhtml</code> | 11 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 16 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 124 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 156 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 214 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 318 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 348 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 355 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 585 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 630 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 135 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 282 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 334 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 415 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 425 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 642 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 886 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 959 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 1023 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 8 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 37 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 198 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 309 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 427 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 615 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 673 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 682 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 805 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 951 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 97 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 120 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 212 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 1 |
| book-title | div | 1 |
| book-title-main | div | 1 |
| copyright | div | 1 |
| em-sesame | span | 27 |
| font-0em80 | div | 1 |
| font-1em10 | p | 19 |
| font-1em10 | span | 7 |
| font-1em30 | p | 1 |
| font-1em30 | span | 1 |
| gaiji | img | 33 |
| gfont | div | 1 |
| h-indent-2em | p | 19 |
| hltr | html | 2 |
| label | div | 1 |
| label-name | p | 1 |
| main | div | 24 |
| mfont | div | 1 |
| mfont | p | 20 |
| mfont | span | 9 |
| original-books | div | 1 |
| original-first-edition | p | 1 |
| original-title | p | 1 |
| p-caution | body | 1 |
| p-colophon | body | 1 |
| p-colophon2 | body | 1 |
| p-text | body | 8 |
| p-toc | body | 1 |
| publish-company | p | 1 |
| publish-person | p | 1 |
| publisher-data | div | 1 |
| release-date | div | 1 |
| start-1em | div | 1 |
| start-2em | div | 2 |
| start-3em | div | 19 |
| support | div | 1 |
| support-contact | p | 1 |
| support-desk | p | 1 |
| support-note | p | 1 |
| tcy | span | 78 |
| vrtl | html | 10 |
| word-break-break-all | span | 14 |

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
- `standard.opf` /*/comment():  g412db0 
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |
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
| <code>xhtml/p-titlepage.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-titlepage.xhtml</code> | <code>../image/titlepage.jpg</code> | <code>image/titlepage.jpg</code> | OK |
| <code>xhtml/p-caution.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../image/toc-001.jpg</code> | <code>image/toc-001.jpg</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../image/p004-005.jpg</code> | <code>image/p004-005.jpg</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../image/p012-013.jpg</code> | <code>image/p012-013.jpg</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid7699-m-v.png</code> | <code>image/gaiji-cid7699-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/p104-105.jpg</code> | <code>image/p104-105.jpg</code> | OK |
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
| <code>xhtml/p-007.xhtml</code> | <code>../image/p216-217.jpg</code> | <code>image/p216-217.jpg</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../image/p340-341.jpg</code> | <code>image/p340-341.jpg</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-013.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-allcover-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-allcover-001.xhtml</code> | <code>../image/allcover-001.jpg</code> | <code>image/allcover-001.jpg</code> | OK |
| <code>xhtml/p-colophon.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-colophon2.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |

## Карта размещений изображений

Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.

| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |
|---:|---|---|---|---|---|---|
| 1 | <code>[[EPUB_IMAGE:v7:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/7/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/cover.jpg) | [<code>raw/7/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v7:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/7/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/kuchie-001.jpg) | [<code>raw/7/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1598", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v7:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/7/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/kuchie-002.jpg) | [<code>raw/7/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1598", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v7:xhtml/p-titlepage.xhtml:titlepage.jpg:occ-01]]</code> | [<code>raw/7/item/image/titlepage.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/titlepage.jpg) | [<code>raw/7/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/titlepage.jpg"}</code> |
| 5 | <code>[[EPUB_IMAGE:v7:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/7/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/toc-001.jpg) | [<code>raw/7/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1453", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v7:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/7/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/p004-005.jpg) | [<code>raw/7/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1475", "href": "../image/p004-005.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v7:xhtml/p-003.xhtml:p012-013.jpg:occ-01]]</code> | [<code>raw/7/item/image/p012-013.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/p012-013.jpg) | [<code>raw/7/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1475", "href": "../image/p012-013.jpg"}</code> |
| 8 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 9 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 10 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 11 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 12 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid7699-m-v.png:occ-07]]</code> | [<code>raw/7/item/image/gaiji-cid7699-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid7699-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | 未曽有の危機を前に、英雄はついに、己の矜持を捨てた。衆目の前にその姿を現し、 [IMAGE] 光に照らされた戦場で宿敵と剣を交え、そして──打ち倒した。 | <code>{"class": "gaiji", "src": "../image/gaiji-cid7699-m-v.png", "alt": "曙"}</code> |
| 15 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 17 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-10]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 18 | <code>[[EPUB_IMAGE:v7:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-11]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 19 | <code>[[EPUB_IMAGE:v7:xhtml/p-005.xhtml:p104-105.jpg:occ-01]]</code> | [<code>raw/7/item/image/p104-105.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/p104-105.jpg) | [<code>raw/7/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1475", "href": "../image/p104-105.jpg"}</code> |
| 20 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 22 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 25 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 28 | <code>[[EPUB_IMAGE:v7:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 29 | <code>[[EPUB_IMAGE:v7:xhtml/p-007.xhtml:p216-217.jpg:occ-01]]</code> | [<code>raw/7/item/image/p216-217.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/p216-217.jpg) | [<code>raw/7/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-007.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1475", "href": "../image/p216-217.jpg"}</code> |
| 30 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 31 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 32 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 33 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 34 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 35 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 36 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 37 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 38 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 39 | <code>[[EPUB_IMAGE:v7:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-10]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 40 | <code>[[EPUB_IMAGE:v7:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 41 | <code>[[EPUB_IMAGE:v7:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 42 | <code>[[EPUB_IMAGE:v7:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/7/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/gaiji-cid776-m-v.png) | [<code>raw/7/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 43 | <code>[[EPUB_IMAGE:v7:xhtml/p-011.xhtml:p340-341.jpg:occ-01]]</code> | [<code>raw/7/item/image/p340-341.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/p340-341.jpg) | [<code>raw/7/item/xhtml/p-011.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-011.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1475", "href": "../image/p340-341.jpg"}</code> |
| 44 | <code>[[EPUB_IMAGE:v7:xhtml/p-allcover-001.xhtml:allcover-001.jpg:occ-01]]</code> | [<code>raw/7/item/image/allcover-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/allcover-001.jpg) | [<code>raw/7/item/xhtml/p-allcover-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-allcover-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "811", "href": "../image/allcover-001.jpg"}</code> |
| 45 | <code>[[EPUB_IMAGE:v7:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/7/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/image/i-bookwalker.jpg) | [<code>raw/7/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/7/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『おばけが目覚めた話』 - through the dark nights -](p-001.xhtml#toc-001)

[『翠緑の英雄譚』 - braves' story -](p-003.xhtml#toc-002)

[『終末の箱庭』 - approaching worldend -](p-005.xhtml#toc-003)

[『隣に立つ者、結ばれる手と手』 - bond of morn -](p-007.xhtml#toc-004)

[『雨烟る夜』 - masked deadman -](p-011.xhtml#toc-005)

[あとがき／と推測されている何か](p-013.xhtml#toc-006)
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
