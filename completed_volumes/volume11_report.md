# Отчёт об извлечении японского исходника — том 11

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/allcover-001.jpg</code> | 233612 | <code>61d2120d99a68e6e6615941b091f7284e3920a713ae37272c39f50bfad1c3b59</code> |
| <code>image/cover.jpg</code> | 650760 | <code>10d89f4a733494e7eac8d3646146d356d50473f41fcfca36e706f37652823046</code> |
| <code>image/i-bookwalker.jpg</code> | 342205 | <code>7cd722f5a19b77ac2c3b9e336a39ecc9803b7a4263dd236f4e8253f15adf2a4a</code> |
| <code>image/kuchie-001.jpg</code> | 461381 | <code>27233f354d2af1c149dd956fc36d558213fc671e21c7dd26df42756c8e7ee8d9</code> |
| <code>image/kuchie-002.jpg</code> | 370644 | <code>28426d941f0e9b8342eb29e497d4a606df7cbb8aa921ff4ed67f21b5f2b1581b</code> |
| <code>image/kuchie-003.jpg</code> | 566252 | <code>4fe48470cf3532f9ca4b432910ad760bf9a668dc64635da811d78197c1781734</code> |
| <code>image/kuchie-004.jpg</code> | 425310 | <code>4e8558102f31e1114d4aa96dd69d29eb3c8d180d2bf3f7c078211e830fb9bc44</code> |
| <code>image/p003.jpg</code> | 510086 | <code>81051edcc7b90d1c729a5a7a0c9fbc52c12332dbc8bfeae3b98fa2c059c8eec5</code> |
| <code>image/p316.jpg</code> | 247365 | <code>df6e153f5f18d8245cd41086e0042c36f8ad34a1f8dd47625989ddc183652a98</code> |
| <code>image/t001.jpg</code> | 333811 | <code>556424fd3b5bc96b9ba4d64054dcf77eb16ad65cad419e088d81ad6e1d25f0d7</code> |
| <code>image/t002.jpg</code> | 304358 | <code>d3af5cf8271267d2ef76af2184d34b4295823fb9da808fae21e7bbea6709abee</code> |
| <code>image/t003.jpg</code> | 446447 | <code>ee85a168f6fa355106ce97d5bd6c8e4b99f6c96aeda86b8dc3df16a301165246</code> |
| <code>image/t004.jpg</code> | 305966 | <code>547487fa1c3b154cff207b11d2882bbb6d3b503a1951efcf4de940db2848d744</code> |
| <code>image/t005.jpg</code> | 384723 | <code>7c71b8b58215e7621d5d357edceb08b596c383aaafa9af55b34d74fb9028f4b9</code> |
| <code>image/t006.jpg</code> | 167933 | <code>63971d534944296fd2dc5fdc8085eec29630a1d79f938cab13269068a5987c12</code> |
| <code>image/titlepage.jpg</code> | 147993 | <code>f8482cb72f8d4632d4448b6edf01436af6f2c6608bd20c1bdf1846e468080736</code> |
| <code>image/toc-001.jpg</code> | 347133 | <code>5d780c0a5e3b3f9ad2335c595820c51236d3a64935ab8fd9dea09bfd190c0a69</code> |
| <code>navigation-documents.xhtml</code> | 1582 | <code>9a668e87037311658235e289ed1eaaab02bf572eada580668591ff101ef61a16</code> |
| <code>standard.opf</code> | 10631 | <code>d4acade9ff33fcd27277fc77a2f78e6cb7792a0de19a45b82735b502aaa2c2ff</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 7766 | <code>067299fc4af21b7575f079b857255b78acce60ee04d503db8126d7723ef44d07</code> |
| <code>style/style-karc.css</code> | 1927 | <code>067ce6303605275a60389c7fb8cd59ef0ca47b6ba8eebe6f6438686f1f67552a</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 723 | <code>d25d6d235e30074f6af5b162670576c8aa3823f53010386aab0eb1a38144cd5b</code> |
| <code>xhtml/p-002.xhtml</code> | 787 | <code>2e7a42ad145d2673685694623bd8e38dd0c6b0c3f77debf491b0535d6a4c23a2</code> |
| <code>xhtml/p-003.xhtml</code> | 16040 | <code>9295619f2226c492bfb37def33cd025bf99987c4610811af6d22d3f7b51f8e9c</code> |
| <code>xhtml/p-004.xhtml</code> | 826 | <code>be524222cb80216f1768915163a06205c4b27611edbdffc3fc0a231a347b3140</code> |
| <code>xhtml/p-005.xhtml</code> | 150402 | <code>12f7c3db5c778d4af80c0bd17152e0d2f9677b34e91301fb06cf8405d5e9c4c6</code> |
| <code>xhtml/p-006.xhtml</code> | 822 | <code>d424560afab0de3d07b5ec6dce9df6e13c54d60e204bff57b06567df206809ff</code> |
| <code>xhtml/p-007.xhtml</code> | 169013 | <code>8747d0992b1b1cca0d2b5cbd024ed2165f14193085aa93b4c9481c936e164bd1</code> |
| <code>xhtml/p-008.xhtml</code> | 822 | <code>4d140918ef3730f532d4385017a97be70ccded7ee2b637d895f95787ee0ff678</code> |
| <code>xhtml/p-009.xhtml</code> | 88093 | <code>4a087be609b3425fdf9bef06eed729a8fa6dccd3259fc2a34399c93dbc058075</code> |
| <code>xhtml/p-010.xhtml</code> | 813 | <code>58e87972bf8a8e8d5fe4ba1c8bea5f1a8c7422882175d0c1c0ff3c9b5decae90</code> |
| <code>xhtml/p-011.xhtml</code> | 67797 | <code>ecf7852f1ecb2d43407dbb4d2f1f7d74f15b8d5fdb832221988cdea9305328fb</code> |
| <code>xhtml/p-012.xhtml</code> | 805 | <code>819c4d46fc6eadd8b83bbab0bee85bdfb8d24be92f130c9cf08e76b3fcb15db2</code> |
| <code>xhtml/p-013.xhtml</code> | 18861 | <code>8409fca90ea3fcee74396076d2b9136f4b48f9fe60d319997a67a50522ff416e</code> |
| <code>xhtml/p-014.xhtml</code> | 5324 | <code>7a558e70df426b078d11e09db7e943233c382eb35113f54b3a6216e6fba20592</code> |
| <code>xhtml/p-allcover-001.xhtml</code> | 728 | <code>6135e243f781bceaccffb40f030a44b4ed048e1cfad1b97bc51d1da3aa460013</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>65719179002ebb0468c3ba14986dda2049ad4c6a087daba3350b8c2189eeb97d</code> |
| <code>xhtml/p-caution.xhtml</code> | 789 | <code>49c6724be5fe694366b3fb9b9f34b5b4d575a047ee916c7093e807669a02ec67</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2323 | <code>6eb0c9d6d7980c26faabdbdc5bafdaa25e695b3c9bbee373854b652c984316c9</code> |
| <code>xhtml/p-colophon2.xhtml</code> | 1056 | <code>71efcca9cf3ffd9a0c8a90532c3e78b693e48a7ae190492dbf6b4f9a0ad4dfa2</code> |
| <code>xhtml/p-cover.xhtml</code> | 742 | <code>56ea513e6cfac5ed6eeb7ac94c20bf2d38990e2128c016e6a4254d4e090b36b7</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 729 | <code>af40cb6b005a09e1fb4db1b4d53b4fecad61363e816d29ed297b78a8ab2ea816</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 729 | <code>9191436db343b2c77c820846ea37213835bbb4180460d7b4f31c966c309911a3</code> |
| <code>xhtml/p-fmatter-003.xhtml</code> | 729 | <code>5f7c2a136d04a6f062a90cfcdcea656223f54ad8d2b568c7ee2c2fd87f15b3cf</code> |
| <code>xhtml/p-fmatter-004.xhtml</code> | 729 | <code>7ef4dbff177e3df6889f52342261554e0ab1bafc0d4ea370c1581b7088aea95e</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 728 | <code>2fe367cec44bdf002f256c0df0f3f7c31e6978d19b75577e28a8970996395020</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 726 | <code>8dd2beba90b36d312b1cb026266e5fce3881c470e2559ce82ce2a3054b156370</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1688 | <code>60f29632f834040b7db9975527e425c214f035ea0bb3251adc3960e599afe0f4</code> |

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
| i-bookwalker | <code>image/i-bookwalker.jpg</code> | image/jpeg | да | локальная ссылка |
| titlepage | <code>image/titlepage.jpg</code> | image/jpeg | да | локальная ссылка |
| allcover-001 | <code>image/allcover-001.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-001 | <code>image/kuchie-001.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-002 | <code>image/kuchie-002.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-003 | <code>image/kuchie-003.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-004 | <code>image/kuchie-004.jpg</code> | image/jpeg | да | локальная ссылка |
| toc-001 | <code>image/toc-001.jpg</code> | image/jpeg | да | локальная ссылка |
| p003 | <code>image/p003.jpg</code> | image/jpeg | да | локальная ссылка |
| p316 | <code>image/p316.jpg</code> | image/jpeg | да | локальная ссылка |
| t001 | <code>image/t001.jpg</code> | image/jpeg | да | локальная ссылка |
| t002 | <code>image/t002.jpg</code> | image/jpeg | да | локальная ссылка |
| t003 | <code>image/t003.jpg</code> | image/jpeg | да | локальная ссылка |
| t004 | <code>image/t004.jpg</code> | image/jpeg | да | локальная ссылка |
| t005 | <code>image/t005.jpg</code> | image/jpeg | да | локальная ссылка |
| t006 | <code>image/t006.jpg</code> | image/jpeg | да | локальная ссылка |
| p-cover | <code>xhtml/p-cover.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-001 | <code>xhtml/p-fmatter-001.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-002 | <code>xhtml/p-fmatter-002.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-fmatter-003 | <code>xhtml/p-fmatter-003.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-fmatter-004 | <code>xhtml/p-fmatter-004.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-titlepage | <code>xhtml/p-titlepage.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-caution | <code>xhtml/p-caution.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-toc-001 | <code>xhtml/p-toc-001.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-toc-002 | <code>xhtml/p-toc-002.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-001 | <code>xhtml/p-001.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-002 | <code>xhtml/p-002.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-003 | <code>xhtml/p-003.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-004 | <code>xhtml/p-004.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-005 | <code>xhtml/p-005.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-006 | <code>xhtml/p-006.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-007 | <code>xhtml/p-007.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-008 | <code>xhtml/p-008.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-009 | <code>xhtml/p-009.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-010 | <code>xhtml/p-010.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-011 | <code>xhtml/p-011.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-012 | <code>xhtml/p-012.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-013 | <code>xhtml/p-013.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-014 | <code>xhtml/p-014.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
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
| 4 | <code>p-fmatter-003</code> | <code>xhtml/p-fmatter-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 5 | <code>p-fmatter-004</code> | <code>xhtml/p-fmatter-004.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 6 | <code>p-titlepage</code> | <code>xhtml/p-titlepage.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 7 | <code>p-caution</code> | <code>xhtml/p-caution.xhtml</code> | parsed | 4 | 0 | 0 | 0 |
| 8 | <code>p-toc-001</code> | <code>xhtml/p-toc-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 9 | <code>p-toc-002</code> | <code>xhtml/p-toc-002.xhtml</code> | TOC logged below, not repeated | 0 | 0 | 0 | 0 |
| 10 | <code>p-001</code> | <code>xhtml/p-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 11 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 12 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 87 | 128 | 174 | 0 |
| 13 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 14 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 1007 | 914 | 1261 | 0 |
| 15 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 16 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 1056 | 1181 | 1618 | 0 |
| 17 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 18 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 627 | 585 | 802 | 0 |
| 19 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 20 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 448 | 381 | 539 | 0 |
| 21 | <code>p-012</code> | <code>xhtml/p-012.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 22 | <code>p-013</code> | <code>xhtml/p-013.xhtml</code> | parsed | 146 | 108 | 154 | 1 |
| 23 | <code>p-014</code> | <code>xhtml/p-014.xhtml</code> | parsed | 33 | 19 | 31 | 0 |
| 24 | <code>p-allcover-001</code> | <code>xhtml/p-allcover-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 25 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 17 | 5 | 8 | 0 |
| 26 | <code>p-colophon2</code> | <code>xhtml/p-colophon2.xhtml</code> | parsed | 3 | 0 | 0 | 0 |
| 27 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-012.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-013.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-014.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-allcover-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-colophon2.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-003.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-004.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#11 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| contents | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『削れゆく空』 - as an intermedio - | <code>xhtml/p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> |
| 『存在を許されない揺籃の世界（下）』 - a watcher of the world - | <code>xhtml/p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> |
| 『世界を壊す五羽の妖精（下）』 - imagecraft miniature garden - | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> |
| 『その選択肢は問いかける（下）』 - something truly precious - | <code>xhtml/p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> |
| 『いつか、遠いあの空にも届く』 - from me to someone - | <code>xhtml/p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> |
| 『また、会えたね』 - his promise and their result - | <code>xhtml/p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> |
| あとがき | <code>xhtml/p-014.xhtml#toc-007</code> | <code>xhtml/p-014.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 27; сопоставлены с manifest: 27.
- Абзацы p в основном потоке: 3428; пустых p, отмеченных [пауза]: 258.
- br-элементов: 258; em-sesame: 50.
- Начальных отступов снято: 2087 символов в 1973 абзацах; нестандартных случаев подробно перечислено: 38.
- CSS-классов в XHTML: 44 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 20; проблемных: 0.
- Маркеров изображений: 17; уникальных ресурсов в маркерах: 17.
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
| <code>xhtml/p-003.xhtml</code> | empty/whitespace-only | 7 | сводный учёт |
| <code>xhtml/p-003.xhtml</code> | no indent / dialogue-like | 42 | сводный учёт |
| <code>xhtml/p-003.xhtml</code> | one U+3000 | 38 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | empty/whitespace-only | 70 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | heading/style heading | 7 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | multiple U+3000 | 13 | 29, 51, 99, 148, 205, 517, 533, 641, 681, 774, 812, 817, 924 |
| <code>xhtml/p-005.xhtml</code> | no indent / dialogue-like | 348 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | one U+3000 | 569 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | empty/whitespace-only | 75 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | heading/style heading | 9 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | multiple U+3000 | 9 | 252, 382, 461, 485, 637, 682, 720, 815, 903 |
| <code>xhtml/p-007.xhtml</code> | no indent / dialogue-like | 321 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | one U+3000 | 642 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | empty/whitespace-only | 46 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | heading/style heading | 6 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | multiple U+3000 | 4 | 15, 142, 150, 214 |
| <code>xhtml/p-009.xhtml</code> | no indent / dialogue-like | 245 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | one U+3000 | 326 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 31 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | multiple U+3000 | 6 | 9, 66, 111, 188, 248, 329 |
| <code>xhtml/p-011.xhtml</code> | no indent / dialogue-like | 173 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 238 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | empty/whitespace-only | 23 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | multiple U+3000 | 6 | 39, 43, 47, 51, 109, 121 |
| <code>xhtml/p-013.xhtml</code> | no indent / dialogue-like | 19 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | one U+3000 | 98 | сводный учёт |
| <code>xhtml/p-014.xhtml</code> | empty/whitespace-only | 6 | сводный учёт |
| <code>xhtml/p-014.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-014.xhtml</code> | no indent / other | 2 | 32-33 |
| <code>xhtml/p-014.xhtml</code> | one U+3000 | 24 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 3 | 1, 3-4 |
| <code>xhtml/p-colophon.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 16 | 1-13, 15-17 |
| <code>xhtml/p-colophon2.xhtml</code> | no indent / other | 3 | 1-3 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-005.xhtml</code> | 29 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 51 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 99 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 148 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 205 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 517 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 533 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 641 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 681 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 774 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 812 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 817 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 924 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 252 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 382 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 461 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 485 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 637 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 682 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 720 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 815 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 903 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 15 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 142 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 150 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 214 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 9 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 66 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 111 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 188 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 248 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 329 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-013.xhtml</code> | 39 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-013.xhtml</code> | 43 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-013.xhtml</code> | 47 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-013.xhtml</code> | 51 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-013.xhtml</code> | 109 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-013.xhtml</code> | 121 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 1 |
| book-title | div | 1 |
| book-title-main | div | 1 |
| copyright | div | 1 |
| em-sesame | span | 50 |
| fit | img | 1 |
| font-0em80 | div | 1 |
| font-0em90 | span | 6 |
| font-1em10 | span | 8 |
| font-1em30 | p | 23 |
| font-1em30 | span | 1 |
| gfont | div | 2 |
| hltr | html | 2 |
| label | div | 1 |
| label-name | p | 1 |
| line-break-loose | p | 38 |
| line-break-loose | span | 44 |
| main | div | 27 |
| mfont | div | 1 |
| mfont | span | 1 |
| original-books | div | 1 |
| original-first-edition | p | 1 |
| original-title | p | 1 |
| p-caution | body | 1 |
| p-colophon | body | 1 |
| p-colophon2 | body | 1 |
| p-text | body | 7 |
| p-toc | body | 1 |
| publish-company | p | 1 |
| publish-person | p | 1 |
| publisher-data | div | 1 |
| release-date | div | 1 |
| release-version | div | 1 |
| start-1em | div | 1 |
| start-2em | div | 1 |
| start-3em | div | 23 |
| support | div | 1 |
| support-contact | p | 1 |
| support-desk | p | 1 |
| support-note-01 | p | 1 |
| support-note-02 | p | 1 |
| support-note-03 | p | 1 |
| support-note-04 | p | 1 |
| tcy | span | 114 |
| vrtl | html | 9 |
| word-break-break-all | span | 44 |

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
- `standard.opf` /*/*[1]/comment()[7]:  レンダリング指定 
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-014.xhtml#toc-007</code> | <code>xhtml/p-014.xhtml</code> | OK |
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
| <code>xhtml/p-titlepage.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-titlepage.xhtml</code> | <code>../image/titlepage.jpg</code> | <code>image/titlepage.jpg</code> | OK |
| <code>xhtml/p-caution.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-toc-001.xhtml</code> | <code>../image/toc-001.jpg</code> | <code>image/toc-001.jpg</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-014.xhtml#toc-007</code> | <code>xhtml/p-014.xhtml</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../image/p003.jpg</code> | <code>image/p003.jpg</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../image/t001.jpg</code> | <code>image/t001.jpg</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/t002.jpg</code> | <code>image/t002.jpg</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/t003.jpg</code> | <code>image/t003.jpg</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/t004.jpg</code> | <code>image/t004.jpg</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/t005.jpg</code> | <code>image/t005.jpg</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../image/t006.jpg</code> | <code>image/t006.jpg</code> | OK |
| <code>xhtml/p-013.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-013.xhtml</code> | <code>../image/p316.jpg</code> | <code>image/p316.jpg</code> | OK |
| <code>xhtml/p-014.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-014.xhtml#toc-007</code> | <code>xhtml/p-014.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-014.xhtml#toc-007</code> | <code>xhtml/p-014.xhtml</code> | OK |

## Карта размещений изображений

Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.

| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |
|---:|---|---|---|---|---|---|
| 1 | <code>[[EPUB_IMAGE:v11:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/11/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/cover.jpg) | [<code>raw/11/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v11:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/11/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/kuchie-001.jpg) | [<code>raw/11/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v11:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/11/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/kuchie-002.jpg) | [<code>raw/11/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v11:xhtml/p-fmatter-003.xhtml:kuchie-003.jpg:occ-01]]</code> | [<code>raw/11/item/image/kuchie-003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/kuchie-003.jpg) | [<code>raw/11/item/xhtml/p-fmatter-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-fmatter-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1606", "href": "../image/kuchie-003.jpg"}</code> |
| 5 | <code>[[EPUB_IMAGE:v11:xhtml/p-fmatter-004.xhtml:kuchie-004.jpg:occ-01]]</code> | [<code>raw/11/item/image/kuchie-004.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/kuchie-004.jpg) | [<code>raw/11/item/xhtml/p-fmatter-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-fmatter-004.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1606", "href": "../image/kuchie-004.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v11:xhtml/p-titlepage.xhtml:titlepage.jpg:occ-01]]</code> | [<code>raw/11/item/image/titlepage.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/titlepage.jpg) | [<code>raw/11/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/titlepage.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v11:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/11/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/toc-001.jpg) | [<code>raw/11/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/toc-001.jpg"}</code> |
| 8 | <code>[[EPUB_IMAGE:v11:xhtml/p-001.xhtml:p003.jpg:occ-01]]</code> | [<code>raw/11/item/image/p003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/p003.jpg) | [<code>raw/11/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/p003.jpg"}</code> |
| 9 | <code>[[EPUB_IMAGE:v11:xhtml/p-002.xhtml:t001.jpg:occ-01]]</code> | [<code>raw/11/item/image/t001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/t001.jpg) | [<code>raw/11/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/t001.jpg"}</code> |
| 10 | <code>[[EPUB_IMAGE:v11:xhtml/p-004.xhtml:t002.jpg:occ-01]]</code> | [<code>raw/11/item/image/t002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/t002.jpg) | [<code>raw/11/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-004.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/t002.jpg"}</code> |
| 11 | <code>[[EPUB_IMAGE:v11:xhtml/p-006.xhtml:t003.jpg:occ-01]]</code> | [<code>raw/11/item/image/t003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/t003.jpg) | [<code>raw/11/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-006.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/t003.jpg"}</code> |
| 12 | <code>[[EPUB_IMAGE:v11:xhtml/p-008.xhtml:t004.jpg:occ-01]]</code> | [<code>raw/11/item/image/t004.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/t004.jpg) | [<code>raw/11/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-008.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/t004.jpg"}</code> |
| 13 | <code>[[EPUB_IMAGE:v11:xhtml/p-010.xhtml:t005.jpg:occ-01]]</code> | [<code>raw/11/item/image/t005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/t005.jpg) | [<code>raw/11/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-010.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/t005.jpg"}</code> |
| 14 | <code>[[EPUB_IMAGE:v11:xhtml/p-012.xhtml:t006.jpg:occ-01]]</code> | [<code>raw/11/item/image/t006.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/t006.jpg) | [<code>raw/11/item/xhtml/p-012.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-012.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/t006.jpg"}</code> |
| 15 | <code>[[EPUB_IMAGE:v11:xhtml/p-013.xhtml:p316.jpg:occ-01]]</code> | [<code>raw/11/item/image/p316.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/p316.jpg) | [<code>raw/11/item/xhtml/p-013.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-013.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"class": "fit", "src": "../image/p316.jpg", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v11:xhtml/p-allcover-001.xhtml:allcover-001.jpg:occ-01]]</code> | [<code>raw/11/item/image/allcover-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/allcover-001.jpg) | [<code>raw/11/item/xhtml/p-allcover-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-allcover-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "829", "href": "../image/allcover-001.jpg"}</code> |
| 17 | <code>[[EPUB_IMAGE:v11:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/11/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/image/i-bookwalker.jpg) | [<code>raw/11/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/11/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　contents

[empty paragraph]

[empty paragraph]

[『削れゆく空』 - as an intermedio -](p-002.xhtml#toc-001)

[『存在を許されない揺籃の世界（下）』 - a watcher of the world -](p-004.xhtml#toc-002)

[『世界を壊す五羽の妖精（下）』 - imagecraft miniature garden -](p-006.xhtml#toc-003)

[『その選択肢は問いかける（下）』 - something truly precious -](p-008.xhtml#toc-004)

[『いつか、遠いあの空にも届く』 - from me to someone -](p-010.xhtml#toc-005)

[『また、会えたね』 - his promise and their result -](p-012.xhtml#toc-006)

[あとがき](p-014.xhtml#toc-007)
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
