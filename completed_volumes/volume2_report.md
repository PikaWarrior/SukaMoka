# Отчёт об извлечении японского исходника — том 2

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/cover.jpg</code> | 471064 | <code>93485816080e65786c75da4745b39ef823760aa047f1664aafe1d8ddb652d7ea</code> |
| <code>image/gaiji-cid15190-m-v.png</code> | 6498 | <code>1fb942d415b17f03a5e42efb69c1bf7ea056a46e19df6b2d695b46163e3ed881</code> |
| <code>image/gaiji-cid776-m-v.png</code> | 4828 | <code>f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf</code> |
| <code>image/i-bookwalker.jpg</code> | 116828 | <code>93da8cbcf35fc14c16188ff6e325669b90ced56a14d72ce495631c76c76b6b75</code> |
| <code>image/kuchie-001.jpg</code> | 415606 | <code>db9a2c796e4276dfebdbc53b7f924d6d2d7b9de23372a9d90a1282a8dc0e45dd</code> |
| <code>image/kuchie-002.jpg</code> | 434631 | <code>1a7377e4dafeb214403612b663ae12e75383a9f526bcb7214a16de58f119c378</code> |
| <code>image/kuchie-003.jpg</code> | 829539 | <code>f1b0032d791048ff5384e646865ed82cd1f84fe436c65d80bc9a0264f902758e</code> |
| <code>image/kuchie-004.jpg</code> | 496653 | <code>e0ba6c2894be2a40e84a299bb12d51b6db99d706277823ebef8974742e9b0be8</code> |
| <code>image/logo-sneaker.png</code> | 4267 | <code>3c68cdfe60118126cac64e2efc73d20294a63b7c1cece9c1adfb59553fa93f88</code> |
| <code>image/p004-005.jpg</code> | 947176 | <code>58b948a4f68c2d9675a9a815090ed05f1f45596250b9969657cd2461f5bdd02b</code> |
| <code>image/p012-013.jpg</code> | 1717603 | <code>0415ae2383a53fee905d3953f00712ab771018931aba7798d656af4e4c21a2d7</code> |
| <code>image/p094-095.jpg</code> | 1595118 | <code>1a1c3278b66080e4cf4ef73cb1737714bb255a7bee6f111fe40634288cb5268d</code> |
| <code>image/p192-193.jpg</code> | 1524467 | <code>06d4de2e0702c6d441d772a9468ee9ad28394a5baa9b5ca1720b36df1fc4662c</code> |
| <code>image/p254-255.jpg</code> | 1510806 | <code>e34b148d55b13cf3fe66e45edfd266e203435befb407fe8cec4421d2bd602311</code> |
| <code>image/sp-001.jpg</code> | 400751 | <code>a895eb5336b92c8ede552d7ec4856d5d162b45b65a66ee140dd3d1c80e07d6bf</code> |
| <code>image/sp-002.jpg</code> | 425016 | <code>faba2a32f636c529419351548d48e955439e71c8307476f00d5030bfb772bb0b</code> |
| <code>image/sp-003.jpg</code> | 487520 | <code>b6af1bab36000f573ab45098c83cc4158b118f8c8571bce646086ad8e4239393</code> |
| <code>image/sp-004.jpg</code> | 346088 | <code>7eb076ec059c182bef159502aafac70a44efd5cf1b12c6cbf17c23e4c4e50d85</code> |
| <code>image/sp-005.jpg</code> | 590609 | <code>0f739293a6081d52f073559c8ccc4a9152a71650fb6ea12bb2b351f674cb5a15</code> |
| <code>image/toc-001.jpg</code> | 590886 | <code>417c8a42f56ceb724c92a0bb0dada338ca40bdafc866900fd0366307420b9e64</code> |
| <code>navigation-documents.xhtml</code> | 1693 | <code>c7cda55731211782f86385233d9aa636728685930e9fbc396613e6663c96c948</code> |
| <code>standard.opf</code> | 11739 | <code>44c227236cc3455178dcb93bbdb915567d5a04d01994fe5136a94e112856dbde</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 5664 | <code>713e501d47d3c3ce2a53b16d16271e659ea9ef66e85083744c10297d3eb05234</code> |
| <code>style/style-karc.css</code> | 1569 | <code>4c16008a60f369029d740186aa957b960f317382331c3bb582f08fbd854051f9</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 780 | <code>ab591b81f77c00a451f831671cc5e02d6a168494759ba103550c49316e9cfec4</code> |
| <code>xhtml/p-002.xhtml</code> | 10553 | <code>cd673f9163ad579d7dd98e55643cbe1851a68d48ee743acbc9f82067ca3cd376</code> |
| <code>xhtml/p-003.xhtml</code> | 790 | <code>0d55fac90e62ed8affea8df5c00e5ffe1ac437340b5ee8e63e6ecfe2c9e33a41</code> |
| <code>xhtml/p-004.xhtml</code> | 136411 | <code>6d26585f9593dd37ecb1a8363660225caeab7d876ec78bca14c76511eddbbf8a</code> |
| <code>xhtml/p-005.xhtml</code> | 810 | <code>073eee3c80d3823ee21dc58e03e2d8d16830f9bc112806d01c1609a149e91480</code> |
| <code>xhtml/p-006.xhtml</code> | 164773 | <code>b66abfc9a6e179b90d17e2e8f3b39fe396c4fe20cb6a9b77b03e110250beb7f1</code> |
| <code>xhtml/p-007.xhtml</code> | 810 | <code>9e6b193049dd1e3b56e120349f9e219e4e7c15db36571d54d79c02d902cdd618</code> |
| <code>xhtml/p-008.xhtml</code> | 99214 | <code>bae3ba01c81ab831dd9c65baadb835f7600fb5ac2895bdfa3c641b7d73e97798</code> |
| <code>xhtml/p-009.xhtml</code> | 783 | <code>90abc638b093f2d64e32df74ea4a19acb43d431631bfb94ac5929faa497bb903</code> |
| <code>xhtml/p-010.xhtml</code> | 20587 | <code>f86e79ffaf9f417ab9da799a58ea1ec20cd64690ad5c5783f5e1306fc3d1cd41</code> |
| <code>xhtml/p-011.xhtml</code> | 6312 | <code>0aa426a2cf8dffb2af32c9e65d616512c6bf26d9cae215fb05a61741766027f6</code> |
| <code>xhtml/p-012.xhtml</code> | 834 | <code>efc8b2fdb80f33d48a88191b3a3abac902bcd0f825acf4df5dff60a433ffa7b5</code> |
| <code>xhtml/p-013.xhtml</code> | 727 | <code>ee6e9a3ed80d91204d732e4cf809860475e61aeef80ff69e594beb3138a73c06</code> |
| <code>xhtml/p-014.xhtml</code> | 727 | <code>8635d3e32ecad181f0105eb86655ccef19660f60c141e415f3a7d5427de32cc7</code> |
| <code>xhtml/p-015.xhtml</code> | 727 | <code>0c8014c0cb39678b41b637c468c83bc16300954d6fe4062018e8df0f77dfb48d</code> |
| <code>xhtml/p-016.xhtml</code> | 727 | <code>fc81b792071de6ae9cbf45ec0f87a52bf4977234fc3728c079467859c8f55d03</code> |
| <code>xhtml/p-017.xhtml</code> | 727 | <code>2c3ee981bbf8fd31d88497ad75cb8ffbc335926d351d42265bc31f74688ee1ad</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>1757004b8dd65a767fbba5fce482c063c27d14aa4225e6dc46e91621cc1ca879</code> |
| <code>xhtml/p-caution.xhtml</code> | 2445 | <code>24a834c4cefa46feba2148fb926150981775ba476b8ed2002329fd7061ff5365</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2122 | <code>6606cf897732389b916d4c21075353978dcc2201a43ebb90b42bce174f2c0548</code> |
| <code>xhtml/p-cover.xhtml</code> | 744 | <code>4b4dcb1dea58ae0714ca09e4bd5cc849d38fa59a15edf409fa0ccf8b3d3d76ac</code> |
| <code>xhtml/p-credit.xhtml</code> | 677 | <code>7f6ddd8a370e35292b79d8f74bbc5f9dd058e7e7701f883a811e24ddfd624e6a</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 731 | <code>18a6222bfe498d4b907ce775324c3590aac57a591bd0b0c4d74bee8b50fec233</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 731 | <code>51f00a1eac179654732254e320f3903f312d5d3f7beae33359fc60cf31e3a6e3</code> |
| <code>xhtml/p-fmatter-003.xhtml</code> | 731 | <code>5da1d2d7efe902360be1c9fd9de4bb27ed3e4a0fa8982edd12d360f07ab39f75</code> |
| <code>xhtml/p-fmatter-004.xhtml</code> | 731 | <code>baf02ad29ff4b4f110ed7b161e29322fbb66676d2bc51a21bb42b43d71939e24</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 1009 | <code>a46b62a564f6308013ac01005acc5bbb28651a028237a0a6a8d21ccf6a04d6ad</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 728 | <code>25ce38956b4e378687b62e09d24520f818973899e657b9389dba2670af621c2c</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1850 | <code>fcb02c77eec734c84322e80653e3ebdad688298909fd39d65c62be7d1c3bce01</code> |

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
| kuchie-003 | <code>image/kuchie-003.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-004 | <code>image/kuchie-004.jpg</code> | image/jpeg | да | локальная ссылка |
| toc-001 | <code>image/toc-001.jpg</code> | image/jpeg | да | локальная ссылка |
| p004-005 | <code>image/p004-005.jpg</code> | image/jpeg | да | локальная ссылка |
| p012-013 | <code>image/p012-013.jpg</code> | image/jpeg | да | локальная ссылка |
| p094-095 | <code>image/p094-095.jpg</code> | image/jpeg | да | локальная ссылка |
| p192-193 | <code>image/p192-193.jpg</code> | image/jpeg | да | локальная ссылка |
| p254-255 | <code>image/p254-255.jpg</code> | image/jpeg | да | локальная ссылка |
| sp-001 | <code>image/sp-001.jpg</code> | image/jpeg | да | локальная ссылка |
| sp-002 | <code>image/sp-002.jpg</code> | image/jpeg | да | локальная ссылка |
| sp-003 | <code>image/sp-003.jpg</code> | image/jpeg | да | локальная ссылка |
| sp-004 | <code>image/sp-004.jpg</code> | image/jpeg | да | локальная ссылка |
| sp-005 | <code>image/sp-005.jpg</code> | image/jpeg | да | локальная ссылка |
| gaiji-cid15190-m-v | <code>image/gaiji-cid15190-m-v.png</code> | image/png | да | локальная ссылка |
| gaiji-cid776-m-v | <code>image/gaiji-cid776-m-v.png</code> | image/png | да | локальная ссылка |
| logo-sneaker | <code>image/logo-sneaker.png</code> | image/png | да | локальная ссылка |
| i-bookwalker | <code>image/i-bookwalker.jpg</code> | image/jpeg | да | локальная ссылка |
| p-cover | <code>xhtml/p-cover.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-001 | <code>xhtml/p-fmatter-001.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-002 | <code>xhtml/p-fmatter-002.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-fmatter-003 | <code>xhtml/p-fmatter-003.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-fmatter-004 | <code>xhtml/p-fmatter-004.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
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
| p-012 | <code>xhtml/p-012.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-013 | <code>xhtml/p-013.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-014 | <code>xhtml/p-014.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-015 | <code>xhtml/p-015.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-016 | <code>xhtml/p-016.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-017 | <code>xhtml/p-017.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-credit | <code>xhtml/p-credit.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-colophon | <code>xhtml/p-colophon.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-bookwalker | <code>xhtml/p-bookwalker.xhtml</code> | application/xhtml+xml | да | package metadata: spine |

## Spine

| № | idref | XHTML | Статус | p | ruby | rt | img/image |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | <code>p-cover</code> | <code>xhtml/p-cover.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 2 | <code>p-fmatter-001</code> | <code>xhtml/p-fmatter-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 3 | <code>p-fmatter-002</code> | <code>xhtml/p-fmatter-002.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 4 | <code>p-fmatter-003</code> | <code>xhtml/p-fmatter-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 5 | <code>p-fmatter-004</code> | <code>xhtml/p-fmatter-004.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 6 | <code>p-titlepage</code> | <code>xhtml/p-titlepage.xhtml</code> | parsed | 4 | 0 | 0 | 1 |
| 7 | <code>p-caution</code> | <code>xhtml/p-caution.xhtml</code> | parsed | 7 | 0 | 0 | 0 |
| 8 | <code>p-toc-001</code> | <code>xhtml/p-toc-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 9 | <code>p-toc-002</code> | <code>xhtml/p-toc-002.xhtml</code> | TOC logged below, not repeated | 0 | 0 | 0 | 0 |
| 10 | <code>p-001</code> | <code>xhtml/p-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 11 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 61 | 90 | 126 | 0 |
| 12 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 13 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 884 | 766 | 1118 | 8 |
| 14 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 15 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 1053 | 1021 | 1500 | 10 |
| 16 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 17 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 683 | 617 | 915 | 4 |
| 18 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 19 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 117 | 137 | 201 | 4 |
| 20 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 38 | 9 | 14 | 0 |
| 21 | <code>p-012</code> | <code>xhtml/p-012.xhtml</code> | parsed | 6 | 0 | 0 | 0 |
| 22 | <code>p-013</code> | <code>xhtml/p-013.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 23 | <code>p-014</code> | <code>xhtml/p-014.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 24 | <code>p-015</code> | <code>xhtml/p-015.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 25 | <code>p-016</code> | <code>xhtml/p-016.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 26 | <code>p-017</code> | <code>xhtml/p-017.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 27 | <code>p-credit</code> | <code>xhtml/p-credit.xhtml</code> | parsed | 5 | 0 | 0 | 0 |
| 28 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 14 | 5 | 8 | 1 |
| 29 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-012.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-013.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-014.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-015.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-016.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-017.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-credit.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-003.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-004.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#02 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『遠い背中』 - lost in dark - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『芽吹きの季節に』 - blurry border - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『全ての今日は、明日へと至る』 - bottle of elpis - | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> |
| 『大好きなもの、大嫌いなもの』 - reasons to live - | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> |
| 『死者の夢』 - fragile reunion - | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> |
| あとがきかもしれない／きっとあとがきだ | <code>xhtml/p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> |
| 電子書籍版付録　コミック版　終末なにしてますか？　忙しいですか？　救ってもらっていいですか？　コミックアライブ２０１６年８月号　プレ掲載話 | <code>xhtml/p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 29; сопоставлены с manifest: 29.
- Абзацы p в основном потоке: 2872; пустых p, отмеченных [пауза]: 188.
- br-элементов: 188; em-sesame: 8.
- Начальных отступов снято: 1709 символов в 1583 абзацах; нестандартных случаев подробно перечислено: 38.
- CSS-классов в XHTML: 42 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 22; проблемных: 0.
- Маркеров изображений: 45; уникальных ресурсов в маркерах: 20.
- Изображений manifest без маркера в spine XHTML: 0.
- Расхождений текстового слоя абзацев: 0; расхождений порядка ruby-чтений: 0; ruby warnings: 0.
- Неизвестных элементов: 0; XML-комментариев: 24; processing instructions: 0.
- Литеральных символов 〔〕 вне rt: 0; предупреждений: 0.

### Расхождения текстового слоя

Не обнаружены.

### Профиль начальных отступов

Для компактности стандартный отступ из одного U+3000 агрегирован по количеству. Все абзацы без отступа, не похожие на реплики/заголовки, перечислены по номерам; все удалённые отступы нестандартной длины приведены в подробной таблице ниже.

| XHTML | Категория | Количество p | Номера p (для потенциальных исключений) |
|---|---|---:|---|
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 16 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 42 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 59 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 5 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 325 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 495 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | empty/whitespace-only | 64 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | heading/style heading | 4 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | no indent / dialogue-like | 447 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | one U+3000 | 538 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 52 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 5 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 235 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 391 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 17 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 8 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 92 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 10 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | no indent / other | 2 | 37-38 |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 25 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | heading/style heading | 2 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | no indent / other | 1 | 4 |
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
| <code>xhtml/p-004.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．ある老人の死 |
| <code>xhtml/p-004.xhtml</code> | 22 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．逃走者と追跡者 |
| <code>xhtml/p-004.xhtml</code> | 112 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 130 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 196 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 212 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 243 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．林檎とマシュマロ |
| <code>xhtml/p-004.xhtml</code> | 289 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 412 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．ふぇどーる |
| <code>xhtml/p-004.xhtml</code> | 445 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 617 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ５．ティアット |
| <code>xhtml/p-004.xhtml</code> | 644 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 800 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．特殊任務 |
| <code>xhtml/p-006.xhtml</code> | 64 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 175 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．ひっくり返ったおもちゃ箱 |
| <code>xhtml/p-006.xhtml</code> | 184 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 298 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 638 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．特務チーム |
| <code>xhtml/p-006.xhtml</code> | 642 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 690 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 729 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 759 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．小さな家族 |
| <code>xhtml/p-006.xhtml</code> | 781 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 846 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 867 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．ティアット |
| <code>xhtml/p-008.xhtml</code> | 120 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．フェオドール |
| <code>xhtml/p-008.xhtml</code> | 176 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 239 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．マルゴ・メディシス |
| <code>xhtml/p-008.xhtml</code> | 355 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．闇の中へ |
| <code>xhtml/p-008.xhtml</code> | 575 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 579 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 629 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ５．闇の中を |
| <code>xhtml/p-010.xhtml</code> | 3 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 43 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 79 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-010.xhtml</code> | 83 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 2 |
| book-title | div | 2 |
| book-title-main | div | 2 |
| caution-vertical | p | 1 |
| copyright | div | 1 |
| em-sesame | span | 8 |
| font-0em75 | span | 1 |
| font-0em85 | p | 1 |
| font-0em90 | span | 3 |
| font-1em10 | p | 14 |
| font-1em10 | span | 6 |
| font-1em30 | p | 3 |
| font-1em30 | span | 1 |
| gaiji | img | 26 |
| gfont | div | 3 |
| gfont | span | 10 |
| hltr | html | 2 |
| label | div | 2 |
| label-logo | p | 2 |
| label-name | p | 1 |
| main | div | 29 |
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
| p-tobira | body | 1 |
| p-toc | body | 1 |
| publish-address | p | 1 |
| publish-company | p | 1 |
| publish-person | p | 1 |
| publish-phone | p | 1 |
| publish-reception | p | 1 |
| publish-url | p | 1 |
| publisher-data | div | 1 |
| release-date | div | 1 |
| start-1em | div | 1 |
| start-2em | div | 3 |
| tcy | span | 41 |
| vrtl | html | 10 |
| word-break-break-all | span | 19 |

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
- `xhtml/p-caution.xhtml` /*/*[2]/*/comment()[1]:  タテ書き文言／横組みの作品では要コメントアウト 
- `xhtml/p-caution.xhtml` /*/*[2]/*/comment()[2]:  ヨコ書き文言／縦組みの作品では要コメントアウト 
- `xhtml/p-caution.xhtml` /*/*[2]/*/comment()[3]:  ================================================================ <p class="caution-horizontal">本作品は横書きでレイアウトされています。</p> ================================================================= 
- `xhtml/p-caution.xhtml` /*/*[2]/*/comment()[4]:  注釈文言／注釈が不要な作品では要コメントアウト 
- `xhtml/p-caution.xhtml` /*/*[2]/*/comment()[5]:  ================================================================ <p><br/></p> <p class="caution-cyusyaku">本文中に「＊」が付されている箇所には注釈があります。その箇所を選択すると、該当する注釈が表示されます。</p> ================================================================= 
- `xhtml/p-caution.xhtml` /*/*[2]/*/comment()[6]:  その他、断り書き等／不要な作品では要コメントアウト 
- `xhtml/p-caution.xhtml` /*/*[2]/*/comment()[7]:  ================================================================ <p><br/></p> <div class="caution-etc"> <p></p> </div> ================================================================= 
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |
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
| <code>xhtml/p-fmatter-003.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-fmatter-003.xhtml</code> | <code>../image/kuchie-003.jpg</code> | <code>image/kuchie-003.jpg</code> | OK |
| <code>xhtml/p-fmatter-004.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-fmatter-004.xhtml</code> | <code>../image/kuchie-004.jpg</code> | <code>image/kuchie-004.jpg</code> | OK |
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
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |
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
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/p094-095.jpg</code> | <code>image/p094-095.jpg</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid15190-m-v.png</code> | <code>image/gaiji-cid15190-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/p192-193.jpg</code> | <code>image/p192-193.jpg</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid15190-m-v.png</code> | <code>image/gaiji-cid15190-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../image/p254-255.jpg</code> | <code>image/p254-255.jpg</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-013.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-013.xhtml</code> | <code>../image/sp-001.jpg</code> | <code>image/sp-001.jpg</code> | OK |
| <code>xhtml/p-014.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-014.xhtml</code> | <code>../image/sp-002.jpg</code> | <code>image/sp-002.jpg</code> | OK |
| <code>xhtml/p-015.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-015.xhtml</code> | <code>../image/sp-003.jpg</code> | <code>image/sp-003.jpg</code> | OK |
| <code>xhtml/p-016.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-016.xhtml</code> | <code>../image/sp-004.jpg</code> | <code>image/sp-004.jpg</code> | OK |
| <code>xhtml/p-017.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-017.xhtml</code> | <code>../image/sp-005.jpg</code> | <code>image/sp-005.jpg</code> | OK |
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |
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
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-007</code> | <code>xhtml/p-012.xhtml</code> | OK |

## Карта размещений изображений

Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.

| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |
|---:|---|---|---|---|---|---|
| 1 | <code>[[EPUB_IMAGE:v2:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/2/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/cover.jpg) | [<code>raw/2/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v2:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/2/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/kuchie-001.jpg) | [<code>raw/2/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v2:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/2/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/kuchie-002.jpg) | [<code>raw/2/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v2:xhtml/p-fmatter-003.xhtml:kuchie-003.jpg:occ-01]]</code> | [<code>raw/2/item/image/kuchie-003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/kuchie-003.jpg) | [<code>raw/2/item/xhtml/p-fmatter-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-fmatter-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2500", "height": "1308", "href": "../image/kuchie-003.jpg"}</code> |
| 5 | <code>[[EPUB_IMAGE:v2:xhtml/p-fmatter-004.xhtml:kuchie-004.jpg:occ-01]]</code> | [<code>raw/2/item/image/kuchie-004.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/kuchie-004.jpg) | [<code>raw/2/item/xhtml/p-fmatter-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-fmatter-004.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2500", "height": "1323", "href": "../image/kuchie-004.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v2:xhtml/p-titlepage.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/2/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/logo-sneaker.png) | [<code>raw/2/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 7 | <code>[[EPUB_IMAGE:v2:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/2/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/toc-001.jpg) | [<code>raw/2/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/toc-001.jpg"}</code> |
| 8 | <code>[[EPUB_IMAGE:v2:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/2/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/p004-005.jpg) | [<code>raw/2/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p004-005.jpg"}</code> |
| 9 | <code>[[EPUB_IMAGE:v2:xhtml/p-003.xhtml:p012-013.jpg:occ-01]]</code> | [<code>raw/2/item/image/p012-013.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/p012-013.jpg) | [<code>raw/2/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p012-013.jpg"}</code> |
| 10 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 11 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 12 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 15 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 17 | <code>[[EPUB_IMAGE:v2:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 18 | <code>[[EPUB_IMAGE:v2:xhtml/p-005.xhtml:p094-095.jpg:occ-01]]</code> | [<code>raw/2/item/image/p094-095.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/p094-095.jpg) | [<code>raw/2/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p094-095.jpg"}</code> |
| 19 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 20 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 22 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid15190-m-v.png:occ-05]]</code> | [<code>raw/2/item/image/gaiji-cid15190-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid15190-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | どろどろとした不安が、すぐに喉から [IMAGE] り出そうだ。唾の塊といっしょに、胃の奥に押し込める。壁の隙間に意識を集中する。 | <code>{"class": "gaiji", "src": "../image/gaiji-cid15190-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 25 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 28 | <code>[[EPUB_IMAGE:v2:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-10]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 29 | <code>[[EPUB_IMAGE:v2:xhtml/p-007.xhtml:p192-193.jpg:occ-01]]</code> | [<code>raw/2/item/image/p192-193.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/p192-193.jpg) | [<code>raw/2/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-007.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p192-193.jpg"}</code> |
| 30 | <code>[[EPUB_IMAGE:v2:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 31 | <code>[[EPUB_IMAGE:v2:xhtml/p-008.xhtml:gaiji-cid15190-m-v.png:occ-02]]</code> | [<code>raw/2/item/image/gaiji-cid15190-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid15190-m-v.png) | [<code>raw/2/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | 準備されていたあらゆる言葉を押しのけて、悲鳴が喉の奥から [IMAGE] った。 | <code>{"class": "gaiji", "src": "../image/gaiji-cid15190-m-v.png", "alt": ""}</code> |
| 32 | <code>[[EPUB_IMAGE:v2:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 33 | <code>[[EPUB_IMAGE:v2:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 34 | <code>[[EPUB_IMAGE:v2:xhtml/p-009.xhtml:p254-255.jpg:occ-01]]</code> | [<code>raw/2/item/image/p254-255.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/p254-255.jpg) | [<code>raw/2/item/xhtml/p-009.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-009.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p254-255.jpg"}</code> |
| 35 | <code>[[EPUB_IMAGE:v2:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 36 | <code>[[EPUB_IMAGE:v2:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 37 | <code>[[EPUB_IMAGE:v2:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 38 | <code>[[EPUB_IMAGE:v2:xhtml/p-010.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/2/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/gaiji-cid776-m-v.png) | [<code>raw/2/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-010.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 39 | <code>[[EPUB_IMAGE:v2:xhtml/p-013.xhtml:sp-001.jpg:occ-01]]</code> | [<code>raw/2/item/image/sp-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/sp-001.jpg) | [<code>raw/2/item/xhtml/p-013.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-013.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1114", "height": "1600", "href": "../image/sp-001.jpg"}</code> |
| 40 | <code>[[EPUB_IMAGE:v2:xhtml/p-014.xhtml:sp-002.jpg:occ-01]]</code> | [<code>raw/2/item/image/sp-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/sp-002.jpg) | [<code>raw/2/item/xhtml/p-014.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-014.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1114", "height": "1600", "href": "../image/sp-002.jpg"}</code> |
| 41 | <code>[[EPUB_IMAGE:v2:xhtml/p-015.xhtml:sp-003.jpg:occ-01]]</code> | [<code>raw/2/item/image/sp-003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/sp-003.jpg) | [<code>raw/2/item/xhtml/p-015.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-015.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1114", "height": "1600", "href": "../image/sp-003.jpg"}</code> |
| 42 | <code>[[EPUB_IMAGE:v2:xhtml/p-016.xhtml:sp-004.jpg:occ-01]]</code> | [<code>raw/2/item/image/sp-004.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/sp-004.jpg) | [<code>raw/2/item/xhtml/p-016.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-016.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1114", "height": "1600", "href": "../image/sp-004.jpg"}</code> |
| 43 | <code>[[EPUB_IMAGE:v2:xhtml/p-017.xhtml:sp-005.jpg:occ-01]]</code> | [<code>raw/2/item/image/sp-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/sp-005.jpg) | [<code>raw/2/item/xhtml/p-017.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-017.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1129", "height": "1600", "href": "../image/sp-005.jpg"}</code> |
| 44 | <code>[[EPUB_IMAGE:v2:xhtml/p-colophon.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/2/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/logo-sneaker.png) | [<code>raw/2/item/xhtml/p-colophon.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-colophon.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 45 | <code>[[EPUB_IMAGE:v2:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/2/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/image/i-bookwalker.jpg) | [<code>raw/2/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/2/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『遠い背中』 - lost in dark -](p-001.xhtml#toc-001)

[『芽吹きの季節に』 - blurry border -](p-003.xhtml#toc-002)

[『全ての今日は、明日へと至る』 - bottle of elpis -](p-005.xhtml#toc-003)

[『大好きなもの、大嫌いなもの』 - reasons to live -](p-007.xhtml#toc-004)

[『死者の夢』 - fragile reunion -](p-009.xhtml#toc-005)

[empty paragraph]

　[あとがきかもしれない／きっとあとがきだ](p-011.xhtml#toc-006)

[empty paragraph]

　[電子書籍版付録](p-012.xhtml#toc-007)

　[コミック版　終末なにしてますか？　忙しいですか？　救ってもらっていいですか？](p-012.xhtml#toc-007)

　[　コミックアライブ２０１６年８月号　プレ掲載話](p-012.xhtml#toc-007)
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
