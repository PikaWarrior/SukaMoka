# Отчёт об извлечении японского исходника — том 6

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/cover.jpg</code> | 969772 | <code>238f3b0842ca9faa7d685db4e0945aabed2f5e900b8cf767184d6813d5a6d875</code> |
| <code>image/gaiji-cid776-m-v.png</code> | 4828 | <code>f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf</code> |
| <code>image/i-bookwalker.jpg</code> | 116828 | <code>93da8cbcf35fc14c16188ff6e325669b90ced56a14d72ce495631c76c76b6b75</code> |
| <code>image/kuchie-001.jpg</code> | 1093846 | <code>bfe12d8d8e9764f3656acc36fe18cdb3776127af9ae1eddc8f291bd5bf5e974d</code> |
| <code>image/kuchie-002.jpg</code> | 1710585 | <code>dc12bd262d1829a50f0529a4a82f515ff0cffa603078f9c57cce1bf7192b71da</code> |
| <code>image/logo-sneaker.png</code> | 4267 | <code>3c68cdfe60118126cac64e2efc73d20294a63b7c1cece9c1adfb59553fa93f88</code> |
| <code>image/p004-005.jpg</code> | 1539893 | <code>aa9ae057f31d45de8afe795b370ff65da08d6d1104c9ba25a0668c805bde51a3</code> |
| <code>image/p016-017.jpg</code> | 1689691 | <code>34a8710f0146ed913d8f283c4a572a3d191e1d975c3b856e40350d55a9a08c52</code> |
| <code>image/p104-105.jpg</code> | 1510333 | <code>6e0530e0f5d5d0d8d66b32e6063f37693edbb78301923f3740822a0aa034ed01</code> |
| <code>image/p206-207.jpg</code> | 1250285 | <code>512466dd66bfeee22f91dbf0cc8c6e05d37173ce590b78b533eca401310c822f</code> |
| <code>image/p274-275.jpg</code> | 1938028 | <code>0522b556ad7c7ccabee97a7845df3ae8ae5ebb3c2a235ab530cb146f414837bf</code> |
| <code>image/toc-001.jpg</code> | 1406208 | <code>07b6e490344e5cb8558c00fabe731af95e9979b7864b182cd76013b1eb075836</code> |
| <code>navigation-documents.xhtml</code> | 1459 | <code>4a5803ae2d81dc3addae9fc49c53cc533ebd3cbc915b3688a56e258e919fe680</code> |
| <code>standard.opf</code> | 9209 | <code>44e8ec09c5ad2fc773589b346b2f3288b63801f4af8b0aca1d6d34890f3fb3bb</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 7024 | <code>b740df19e7fb68db8d4e55c2b0bbf9e640444a0f72bd1105e67005518cca3c5c</code> |
| <code>style/style-karc.css</code> | 1569 | <code>4c16008a60f369029d740186aa957b960f317382331c3bb582f08fbd854051f9</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 800 | <code>aa63a67aa56cb3f4982c2c88abf3624c0ea565d87d412ed9ae8e8425e6bf7eed</code> |
| <code>xhtml/p-002.xhtml</code> | 21552 | <code>c08f7cbffef87e04caaaa9f59ee7b208da13712f24828f60ffe26f9049bdb172</code> |
| <code>xhtml/p-003.xhtml</code> | 807 | <code>65ee53735e61d52d9bf44cdc1cd3ac339f61cff6660f314dde0af0deb7e6d1c9</code> |
| <code>xhtml/p-004.xhtml</code> | 83435 | <code>d613f0d694ef44851ca045c262066892023ac966b0fb68141ab69456ba9429a4</code> |
| <code>xhtml/p-005.xhtml</code> | 79846 | <code>0dca8aabedb3a9c463132fef76e371ade0339b1074c9520e86ceaea0011d3e65</code> |
| <code>xhtml/p-006.xhtml</code> | 800 | <code>1a933f83dfa37bc0a275b2d80ea37be45502da23abb5c31ee556f09841405ce5</code> |
| <code>xhtml/p-007.xhtml</code> | 118394 | <code>0a9688d64eb8cf48ac9bb1dd2c7f49c5bfc3f257f8e9444395a862f10251642c</code> |
| <code>xhtml/p-008.xhtml</code> | 67382 | <code>aeb529f25044239a39e596bc2b93fbbc4f513a0f630753aa68aae730d494133c</code> |
| <code>xhtml/p-009.xhtml</code> | 811 | <code>80864318c463bc79e6377741e9cda3247bb83dfd727d1909a3f91f35ad784c26</code> |
| <code>xhtml/p-010.xhtml</code> | 118350 | <code>f89636631a13734d2797b6ba3a7f79746def213e402bf59bbe8343d6bd9d8a71</code> |
| <code>xhtml/p-011.xhtml</code> | 796 | <code>8c2765847b019ba4aa40a9fdca77ff1d458fd6ba64172246570072e8b4d1f803</code> |
| <code>xhtml/p-012.xhtml</code> | 54436 | <code>5dd24fd8d1fa81ea1356b4f312e9c7dae833e39f2d935c2688343eb3e4dadc7e</code> |
| <code>xhtml/p-013.xhtml</code> | 15346 | <code>ab5f2b803d0e26075e2cf309fc41bbd8e9cb91d26a3a1c9441edd82a336132f7</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>1757004b8dd65a767fbba5fce482c063c27d14aa4225e6dc46e91621cc1ca879</code> |
| <code>xhtml/p-caution.xhtml</code> | 1305 | <code>d347da7e33e919e5d44526455b30e16549fc00d8f35fb373f12788f4539fed52</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2032 | <code>2582652cb8aeec6385408fe0218d8c2683cc2846cf66e7bfbac1a115fe8a3575</code> |
| <code>xhtml/p-cover.xhtml</code> | 739 | <code>c6de50133c73464fadfbf2cce7747c20ffcc59973f17bc14ca38751a0c0d9b75</code> |
| <code>xhtml/p-credit.xhtml</code> | 615 | <code>f1b0d6e7ce17d7b3067458cdf3a5d46ac2d0aedcb19612181b24b0873d108076</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 726 | <code>0c2017741bc507d249d2550c4dd175e154ad54fd7ddfeb7efc65dd5abcc00d2d</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 726 | <code>c32771956b7dadd52a716ad7f75001f8a618e1deff617207ff285b3c64699925</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 1004 | <code>01987ba476ec17d8e79ec50c82662905de165a9f54be82b4558e4b50c82a589b</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 723 | <code>622d2a550a6f06199ab0ab44e3fd901d9935b114ea9d507ab87ad0d666f0fe91</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1399 | <code>d155045d13a84a20ef808c8e9e3f5bb8532bab2763d44ec054f9013476c85b28</code> |

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
| p104-105 | <code>image/p104-105.jpg</code> | image/jpeg | да | локальная ссылка |
| p206-207 | <code>image/p206-207.jpg</code> | image/jpeg | да | локальная ссылка |
| p274-275 | <code>image/p274-275.jpg</code> | image/jpeg | да | локальная ссылка |
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
| p-005 | <code>xhtml/p-005.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-006 | <code>xhtml/p-006.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-007 | <code>xhtml/p-007.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-008 | <code>xhtml/p-008.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-009 | <code>xhtml/p-009.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-010 | <code>xhtml/p-010.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-011 | <code>xhtml/p-011.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-012 | <code>xhtml/p-012.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-013 | <code>xhtml/p-013.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
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
| 9 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 95 | 195 | 262 | 3 |
| 10 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 11 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 461 | 624 | 924 | 5 |
| 12 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 433 | 573 | 856 | 2 |
| 13 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 14 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 617 | 870 | 1295 | 8 |
| 15 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 380 | 442 | 658 | 1 |
| 16 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 17 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 730 | 912 | 1322 | 12 |
| 18 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 19 | <code>p-012</code> | <code>xhtml/p-012.xhtml</code> | parsed | 334 | 340 | 481 | 3 |
| 20 | <code>p-013</code> | <code>xhtml/p-013.xhtml</code> | parsed | 71 | 90 | 142 | 0 |
| 21 | <code>p-credit</code> | <code>xhtml/p-credit.xhtml</code> | parsed | 5 | 0 | 0 | 0 |
| 22 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 13 | 5 | 8 | 1 |
| 23 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-012.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-013.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-credit.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか? もう一度だけ、会えますか? #06 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『手を取り合えなくて』 - hearts to hearts - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『振り返れど過去は遠く』 - age of scarlet scars - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『仰ぎ見れど明日は眩く』 - sword of morn - | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> |
| 『誰かを幸せにするということ』 - scam of cowards - | <code>xhtml/p-009.xhtml#toc-004</code> | <code>xhtml/p-009.xhtml</code> |
| 『おばけが出た話』 - always in my heart - | <code>xhtml/p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> |
| あとがき／と見せかけた違う何か | <code>xhtml/p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 23; сопоставлены с manifest: 23.
- Абзацы p в основном потоке: 3150; пустых p, отмеченных [пауза]: 262.
- br-элементов: 262; em-sesame: 29.
- Начальных отступов снято: 2052 символов в 1916 абзацах; нестандартных случаев подробно перечислено: 34.
- CSS-классов в XHTML: 40 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 46; уникальных ресурсов в маркерах: 12.
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
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 12 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 20 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 63 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 48 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 2 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 105 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 306 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | empty/whitespace-only | 29 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | heading/style heading | 2 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | no indent / dialogue-like | 133 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | one U+3000 | 269 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | empty/whitespace-only | 48 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | heading/style heading | 5 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | no indent / dialogue-like | 196 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | one U+3000 | 368 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 16 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 2 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 157 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 205 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 87 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | heading/style heading | 5 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 197 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / other | 2 | 688, 717 |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 439 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | empty/whitespace-only | 31 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | no indent / dialogue-like | 70 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | one U+3000 | 233 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | empty/whitespace-only | 21 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | no indent / other | 15 | 16, 19, 22, 25, 29, 32, 35, 38, 41, 44, 48, 51, 54, 70-71 |
| <code>xhtml/p-013.xhtml</code> | one U+3000 | 33 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 6 | 1-4, 6-7 |
| <code>xhtml/p-colophon.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 11 | 1-2, 4-12 |
| <code>xhtml/p-credit.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-credit.xhtml</code> | no indent / other | 2 | 4-5 |
| <code>xhtml/p-titlepage.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-titlepage.xhtml</code> | no indent / other | 3 | 1-2, 4 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-002.xhtml</code> | 4 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-002.xhtml</code> | 81 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-002.xhtml</code> | 89 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 37 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 53 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 214 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 219 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 453 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-005.xhtml</code> | 12 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-005.xhtml</code> | 216 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 25 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 30 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 94 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 105 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 281 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 347 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 406 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-007.xhtml</code> | 600 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 278 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 65 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 143 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 181 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 336 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 342 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 363 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 427 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 541 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 549 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 558 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 573 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 591 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-012.xhtml</code> | 122 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-012.xhtml</code> | 199 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-012.xhtml</code> | 288 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 2 |
| bold | span | 14 |
| book-title | div | 2 |
| book-title-main | div | 2 |
| copyright | div | 1 |
| em-sesame | span | 29 |
| end-1em | div | 1 |
| font-0em90 | span | 1 |
| font-1em10 | p | 16 |
| font-1em10 | span | 6 |
| font-1em30 | p | 1 |
| font-1em30 | span | 1 |
| gaiji | img | 34 |
| gfont | div | 4 |
| gfont | span | 8 |
| hltr | html | 2 |
| label | div | 2 |
| label-logo | p | 2 |
| label-name | p | 1 |
| main | div | 23 |
| mfont | div | 1 |
| mfont | p | 17 |
| mfont | span | 1 |
| original-books | div | 1 |
| original-first-edition | p | 1 |
| original-title | p | 1 |
| p-caution | body | 1 |
| p-colophon | body | 1 |
| p-text | body | 9 |
| p-titlepage | body | 1 |
| p-toc | body | 1 |
| publish-company | p | 1 |
| publish-person | p | 1 |
| publisher-data | div | 1 |
| release-date | div | 1 |
| start-1em | div | 1 |
| start-2em | div | 19 |
| support | div | 1 |
| support-contact | p | 1 |
| support-desk | p | 1 |
| support-note | p | 1 |
| tcy | span | 57 |
| vrtl | html | 11 |
| word-break-break-all | span | 15 |

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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-009.xhtml#toc-004</code> | <code>xhtml/p-009.xhtml</code> | OK |
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
| <code>xhtml/p-titlepage.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-titlepage.xhtml</code> | <code>../image/logo-sneaker.png</code> | <code>image/logo-sneaker.png</code> | OK |
| <code>xhtml/p-caution.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../image/toc-001.jpg</code> | <code>image/toc-001.jpg</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-009.xhtml#toc-004</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |
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
| <code>xhtml/p-005.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/p104-105.jpg</code> | <code>image/p104-105.jpg</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../image/p206-207.jpg</code> | <code>image/p206-207.jpg</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../image/p274-275.jpg</code> | <code>image/p274-275.jpg</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-013.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-009.xhtml#toc-004</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-009.xhtml#toc-004</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-011.xhtml#toc-005</code> | <code>xhtml/p-011.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |

## Карта размещений изображений

Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.

| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |
|---:|---|---|---|---|---|---|
| 1 | <code>[[EPUB_IMAGE:v6:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/6/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/cover.jpg) | [<code>raw/6/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v6:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/6/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/kuchie-001.jpg) | [<code>raw/6/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2040", "height": "1600", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v6:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/6/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/kuchie-002.jpg) | [<code>raw/6/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2040", "height": "1600", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v6:xhtml/p-titlepage.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/6/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/logo-sneaker.png) | [<code>raw/6/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 5 | <code>[[EPUB_IMAGE:v6:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/6/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/toc-001.jpg) | [<code>raw/6/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2255", "height": "1600", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v6:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/6/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/p004-005.jpg) | [<code>raw/6/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p004-005.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v6:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 8 | <code>[[EPUB_IMAGE:v6:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 9 | <code>[[EPUB_IMAGE:v6:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 10 | <code>[[EPUB_IMAGE:v6:xhtml/p-003.xhtml:p016-017.jpg:occ-01]]</code> | [<code>raw/6/item/image/p016-017.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/p016-017.jpg) | [<code>raw/6/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p016-017.jpg"}</code> |
| 11 | <code>[[EPUB_IMAGE:v6:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 12 | <code>[[EPUB_IMAGE:v6:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v6:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v6:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 15 | <code>[[EPUB_IMAGE:v6:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v6:xhtml/p-005.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-005.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 17 | <code>[[EPUB_IMAGE:v6:xhtml/p-005.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-005.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 18 | <code>[[EPUB_IMAGE:v6:xhtml/p-006.xhtml:p104-105.jpg:occ-01]]</code> | [<code>raw/6/item/image/p104-105.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/p104-105.jpg) | [<code>raw/6/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-006.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p104-105.jpg"}</code> |
| 19 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 20 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 22 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 25 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v6:xhtml/p-007.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-007.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v6:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 28 | <code>[[EPUB_IMAGE:v6:xhtml/p-009.xhtml:p206-207.jpg:occ-01]]</code> | [<code>raw/6/item/image/p206-207.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/p206-207.jpg) | [<code>raw/6/item/xhtml/p-009.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-009.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p206-207.jpg"}</code> |
| 29 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 30 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 31 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 32 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 33 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 34 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 35 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 36 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 37 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 38 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-10]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 39 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-11]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 40 | <code>[[EPUB_IMAGE:v6:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-12]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 41 | <code>[[EPUB_IMAGE:v6:xhtml/p-011.xhtml:p274-275.jpg:occ-01]]</code> | [<code>raw/6/item/image/p274-275.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/p274-275.jpg) | [<code>raw/6/item/xhtml/p-011.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-011.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p274-275.jpg"}</code> |
| 42 | <code>[[EPUB_IMAGE:v6:xhtml/p-012.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-012.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-012.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 43 | <code>[[EPUB_IMAGE:v6:xhtml/p-012.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-012.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-012.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 44 | <code>[[EPUB_IMAGE:v6:xhtml/p-012.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/6/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/gaiji-cid776-m-v.png) | [<code>raw/6/item/xhtml/p-012.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-012.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 45 | <code>[[EPUB_IMAGE:v6:xhtml/p-colophon.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/6/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/logo-sneaker.png) | [<code>raw/6/item/xhtml/p-colophon.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-colophon.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 46 | <code>[[EPUB_IMAGE:v6:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/6/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/image/i-bookwalker.jpg) | [<code>raw/6/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/6/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『手を取り合えなくて』 - hearts to hearts -](p-001.xhtml#toc-001)

[『振り返れど過去は遠く』 - age of scarlet scars -](p-003.xhtml#toc-002)

[『仰ぎ見れど明日は眩く』 - sword of morn -](p-006.xhtml#toc-003)

[『誰かを幸せにするということ』 - scam of cowards -](p-009.xhtml#toc-004)

[『おばけが出た話』 - always in my heart -](p-011.xhtml#toc-005)

[empty paragraph]

　[あとがき／と見せかけた違う何か](p-013.xhtml#toc-006)
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
