# Отчёт об извлечении японского исходника — том 9

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/allcover-001.jpg</code> | 302771 | <code>4415e829354a5970678297892c84a5d742d81eae10dcb011f2319212fe63ce7f</code> |
| <code>image/cover.jpg</code> | 779908 | <code>71a7f7070b08dcba4179145ee7fbb477484cd9eab17a8e9924e6dc6d3c21567c</code> |
| <code>image/i-bookwalker.jpg</code> | 342205 | <code>7cd722f5a19b77ac2c3b9e336a39ecc9803b7a4263dd236f4e8253f15adf2a4a</code> |
| <code>image/img-p003.jpg</code> | 593230 | <code>139b8a131cac9454dc48ed4110b61c5c362eb078edaa5d65a796efb34df140b1</code> |
| <code>image/img-p004.jpg</code> | 497504 | <code>c9a9f6b392a6e2da6a0f7149fe292e7f967122b4a973e89898753a545aed642a</code> |
| <code>image/img-p012.jpg</code> | 456705 | <code>227b4a81f94ee87613a58590f94e329651cdeb75c65866b1e0ede7542e885119</code> |
| <code>image/img-p136.jpg</code> | 374797 | <code>ee9ec238a0bb2802f75ef793457fc9899acc5d94d04eb4a5a58d5e86fe09903e</code> |
| <code>image/img-p146.jpg</code> | 410887 | <code>43d2927ba2429d42e662f95d93926079d6d59fb0a6d1d2075550ad2034f779cc</code> |
| <code>image/img-p248.jpg</code> | 354962 | <code>358f516366a6c4c4be002038f9d69df5a2c49ceee6bb09d7397ea5d7a00834d2</code> |
| <code>image/kuchie-001.jpg</code> | 731399 | <code>ce253c5420564363a0fd071b59c3814c34b1eeb9662cd30c35eb6db3e197ca00</code> |
| <code>image/kuchie-002.jpg</code> | 784514 | <code>545183c03f3ef904e401b4f410715970465924be0ec5229321a6ee74de4577b5</code> |
| <code>image/titlepage.jpg</code> | 105388 | <code>3fd854cf3c0492af326a2dac2dd85a7d27eb6024047781e9bf9ac5ef3b38975f</code> |
| <code>image/toc-001.jpg</code> | 429582 | <code>bdd7637927519ec6a4d95f920483c2fe872d575c4497e1ebf9832de44ed37b40</code> |
| <code>navigation-documents.xhtml</code> | 1443 | <code>e5614e8410577b9fd39e002429851728679a5c9e0428566b3e7e84d8f8a4e374</code> |
| <code>standard.opf</code> | 9341 | <code>e0117f0384b40e0d01c8414ea741adaf3124846476f6a65360e888147876148e</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 7766 | <code>067299fc4af21b7575f079b857255b78acce60ee04d503db8126d7723ef44d07</code> |
| <code>style/style-karc.css</code> | 1927 | <code>067ce6303605275a60389c7fb8cd59ef0ca47b6ba8eebe6f6438686f1f67552a</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 727 | <code>65fdfc2fe3bef28c004da9131601b26772912c20efd995b8a0bf2072b85a0254</code> |
| <code>xhtml/p-002.xhtml</code> | 808 | <code>0950c8a6262cb541dc1b6f7c89981f6d17630e4ad543fa7b0b0f281e80960e3e</code> |
| <code>xhtml/p-003.xhtml</code> | 8454 | <code>3066f25eaf135d33b4499e9d927ea97dd2a9093ced8cc9ec291639fbe054ce07</code> |
| <code>xhtml/p-004.xhtml</code> | 785 | <code>48408f9d23f09c1ac81d08d2dc3de61170086b39c4c9e9119b3c94525ad4f7c6</code> |
| <code>xhtml/p-005.xhtml</code> | 218050 | <code>eaf0802605ea5dcc6d4cbfa0484df0563b7a2e842392b031dc72ed9f07af06ec</code> |
| <code>xhtml/p-006.xhtml</code> | 808 | <code>8e8d3af2155d6666e895bb9a4a38b7c361ee4588c021a2187f0849b3446e7cc9</code> |
| <code>xhtml/p-007.xhtml</code> | 12752 | <code>b7320a9254223f0870a096c8a206da1d68de2bfbcb7d77809791967a09f9c3e3</code> |
| <code>xhtml/p-008.xhtml</code> | 810 | <code>af995a74105deef14fa3a57749562c7d7225f8b3881596bc5131792b4ae0dd38</code> |
| <code>xhtml/p-009.xhtml</code> | 167781 | <code>b82fb04633e373b7e6c8c264a4c40539071f41da47ba2d065ef07914ff105372</code> |
| <code>xhtml/p-010.xhtml</code> | 815 | <code>9777aee37e273adfd960436c8449201d38861308cdb99c5ef7a7272ccd04a893</code> |
| <code>xhtml/p-011.xhtml</code> | 4454 | <code>19431522140e8e9466463ded65dcf2bb427ea46e0082c1cf8e24112fcc2387c0</code> |
| <code>xhtml/p-012.xhtml</code> | 3918 | <code>63ec6b6cf7f3b6f9a01408309711031f5a334fe69c4ba009df1071eee22e7909</code> |
| <code>xhtml/p-allcover-001.xhtml</code> | 728 | <code>0072a5119849cd5fd54d3270702fa729c9e01fa19172a38e2a2ddf405502377c</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>65719179002ebb0468c3ba14986dda2049ad4c6a087daba3350b8c2189eeb97d</code> |
| <code>xhtml/p-caution.xhtml</code> | 789 | <code>49c6724be5fe694366b3fb9b9f34b5b4d575a047ee916c7093e807669a02ec67</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2324 | <code>a54713ef3f3e49ad76c606adcd2d572a9306214c2f8a3aa0c34ae7b1a7228105</code> |
| <code>xhtml/p-colophon2.xhtml</code> | 1056 | <code>0e07cdd13785a2cb6daaababadd4c6239eaf941451c94ca5706ec3f5b930f90d</code> |
| <code>xhtml/p-cover.xhtml</code> | 742 | <code>fcfa1f35ffbfda72f812fc5adac3ba14d58d7a02843beaeb9531e0b798eb46e8</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 729 | <code>3868db580525453ea3c0d963dad84ffc7c278053ff94deb436fb38ab2fa264bd</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 729 | <code>254d5c7dd275e28e2827745634e069667dbc907e9b7b8a30b051b213021c93a0</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 728 | <code>49a7f0ca38d94c2760556197af7c617bb7d262c07a41318e9e85eeb8c407ae36</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 726 | <code>e645997dce1af75de30ad619206d2c7569034e5458b90bdf6059fb647e58f00a</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1493 | <code>58920c875755a3523b67464e4fcbe5026dbc620ba1ad4f8ae7876472f6210df6</code> |

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
| img-p003 | <code>image/img-p003.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p004 | <code>image/img-p004.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p012 | <code>image/img-p012.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p136 | <code>image/img-p136.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p146 | <code>image/img-p146.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p248 | <code>image/img-p248.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-001 | <code>image/kuchie-001.jpg</code> | image/jpeg | да | локальная ссылка |
| kuchie-002 | <code>image/kuchie-002.jpg</code> | image/jpeg | да | локальная ссылка |
| toc-001 | <code>image/toc-001.jpg</code> | image/jpeg | да | локальная ссылка |
| p-cover | <code>xhtml/p-cover.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-001 | <code>xhtml/p-fmatter-001.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-002 | <code>xhtml/p-fmatter-002.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
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
| 9 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 10 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 53 | 39 | 59 | 0 |
| 11 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 12 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 1303 | 1454 | 2204 | 0 |
| 13 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 14 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 77 | 79 | 108 | 0 |
| 15 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 16 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 1122 | 971 | 1401 | 0 |
| 17 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 18 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 43 | 19 | 27 | 0 |
| 19 | <code>p-012</code> | <code>xhtml/p-012.xhtml</code> | parsed | 15 | 11 | 17 | 0 |
| 20 | <code>p-allcover-001</code> | <code>xhtml/p-allcover-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 21 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 17 | 5 | 8 | 0 |
| 22 | <code>p-colophon2</code> | <code>xhtml/p-colophon2.xhtml</code> | parsed | 3 | 0 | 0 | 0 |
| 23 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-012.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-allcover-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-colophon2.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#09 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| contents | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『あの日々の続きにいる』 - today was tomorrow - | <code>xhtml/p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> |
| 『青鷺の湖』 - a stolen veil - | <code>xhtml/p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> |
| 『時は止まりそして流れる』 - glints of lives - | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> |
| 『新品の天秤の右と左』 - where to go, what to be - | <code>xhtml/p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> |
| 『苦くて優しい夢の中』 - it will be a beautiful world - | <code>xhtml/p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> |
| あとがき／あれからどれくらい── | <code>xhtml/p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 23; сопоставлены с manifest: 23.
- Абзацы p в основном потоке: 2637; пустых p, отмеченных [пауза]: 172.
- br-элементов: 172; em-sesame: 35.
- Начальных отступов снято: 1463 символов в 1377 абзацах; нестандартных случаев подробно перечислено: 29.
- CSS-классов в XHTML: 44 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 13; уникальных ресурсов в маркерах: 13.
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
| <code>xhtml/p-003.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-003.xhtml</code> | no indent / dialogue-like | 24 | сводный учёт |
| <code>xhtml/p-003.xhtml</code> | one U+3000 | 26 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | empty/whitespace-only | 92 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | multiple U+3000 | 13 | 81, 232, 344, 368, 445, 581, 588, 595, 602, 759, 1060, 1238, 1243 |
| <code>xhtml/p-005.xhtml</code> | no indent / dialogue-like | 457 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | no indent / other | 11 | 1, 57, 219, 313, 439, 550, 700, 898, 996, 998, 1180 |
| <code>xhtml/p-005.xhtml</code> | one U+3000 | 730 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | multiple U+3000 | 1 | 27 |
| <code>xhtml/p-007.xhtml</code> | no indent / dialogue-like | 41 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | one U+3000 | 32 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | empty/whitespace-only | 67 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | multiple U+3000 | 13 | 22, 93, 176, 247, 378, 412, 557, 688, 723, 1020, 1064, 1070, 1117 |
| <code>xhtml/p-009.xhtml</code> | no indent / dialogue-like | 515 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | no indent / other | 7 | 1, 98, 281, 490, 635, 819, 967 |
| <code>xhtml/p-009.xhtml</code> | one U+3000 | 520 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 2 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | multiple U+3000 | 1 | 6 |
| <code>xhtml/p-011.xhtml</code> | no indent / dialogue-like | 8 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 32 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | empty/whitespace-only | 4 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | multiple U+3000 | 1 | 14 |
| <code>xhtml/p-012.xhtml</code> | no indent / other | 1 | 15 |
| <code>xhtml/p-012.xhtml</code> | one U+3000 | 8 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 3 | 1, 3-4 |
| <code>xhtml/p-colophon.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 16 | 1-13, 15-17 |
| <code>xhtml/p-colophon2.xhtml</code> | no indent / other | 3 | 1-3 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-005.xhtml</code> | 81 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 232 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 344 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 368 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 445 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 581 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 588 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 595 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 602 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 759 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 1060 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 1238 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 1243 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 27 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 22 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 93 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 176 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 247 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 378 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 412 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 557 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 688 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 723 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 1020 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 1064 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 1070 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 1117 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 6 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-012.xhtml</code> | 14 | <code>'\u3000\u3000\u3000'</code> | 3 | <code></code> | 二〇二〇年　夏 |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 1 |
| book-title | div | 1 |
| book-title-main | div | 1 |
| copyright | div | 1 |
| em-sesame | span | 35 |
| end-1em | div | 1 |
| font-0em80 | div | 1 |
| font-0em90 | span | 5 |
| font-1em10 | span | 7 |
| font-1em30 | p | 1 |
| font-1em30 | span | 18 |
| gfont | div | 2 |
| hltr | html | 2 |
| label | div | 1 |
| label-name | p | 1 |
| line-break-loose | p | 17 |
| line-break-loose | span | 17 |
| main | div | 23 |
| mfont | div | 1 |
| mfont | span | 1 |
| original-books | div | 1 |
| original-first-edition | p | 1 |
| original-title | p | 1 |
| p-caution | body | 1 |
| p-colophon | body | 1 |
| p-colophon2 | body | 1 |
| p-text | body | 6 |
| p-toc | body | 1 |
| publish-company | p | 1 |
| publish-person | p | 1 |
| publisher-data | div | 1 |
| release-date | div | 1 |
| release-version | div | 1 |
| start-1em | div | 1 |
| start-2em | div | 1 |
| start-3em | div | 17 |
| support | div | 1 |
| support-contact | p | 1 |
| support-desk | p | 1 |
| support-note-01 | p | 1 |
| support-note-02 | p | 1 |
| support-note-03 | p | 1 |
| support-note-04 | p | 1 |
| tcy | span | 43 |
| vrtl | html | 8 |
| word-break-break-all | span | 17 |

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
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../image/img-p003.jpg</code> | <code>image/img-p003.jpg</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../image/img-p004.jpg</code> | <code>image/img-p004.jpg</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/img-p012.jpg</code> | <code>image/img-p012.jpg</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/img-p136.jpg</code> | <code>image/img-p136.jpg</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/img-p146.jpg</code> | <code>image/img-p146.jpg</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/img-p248.jpg</code> | <code>image/img-p248.jpg</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
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

## Карта размещений изображений

Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.

| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |
|---:|---|---|---|---|---|---|
| 1 | <code>[[EPUB_IMAGE:v9:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/9/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/cover.jpg) | [<code>raw/9/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v9:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/9/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/kuchie-001.jpg) | [<code>raw/9/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1624", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v9:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/9/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/kuchie-002.jpg) | [<code>raw/9/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1624", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v9:xhtml/p-titlepage.xhtml:titlepage.jpg:occ-01]]</code> | [<code>raw/9/item/image/titlepage.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/titlepage.jpg) | [<code>raw/9/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/titlepage.jpg"}</code> |
| 5 | <code>[[EPUB_IMAGE:v9:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/9/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/toc-001.jpg) | [<code>raw/9/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v9:xhtml/p-001.xhtml:img-p003.jpg:occ-01]]</code> | [<code>raw/9/item/image/img-p003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/img-p003.jpg) | [<code>raw/9/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/img-p003.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v9:xhtml/p-002.xhtml:img-p004.jpg:occ-01]]</code> | [<code>raw/9/item/image/img-p004.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/img-p004.jpg) | [<code>raw/9/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p004.jpg"}</code> |
| 8 | <code>[[EPUB_IMAGE:v9:xhtml/p-004.xhtml:img-p012.jpg:occ-01]]</code> | [<code>raw/9/item/image/img-p012.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/img-p012.jpg) | [<code>raw/9/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-004.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p012.jpg"}</code> |
| 9 | <code>[[EPUB_IMAGE:v9:xhtml/p-006.xhtml:img-p136.jpg:occ-01]]</code> | [<code>raw/9/item/image/img-p136.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/img-p136.jpg) | [<code>raw/9/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-006.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p136.jpg"}</code> |
| 10 | <code>[[EPUB_IMAGE:v9:xhtml/p-008.xhtml:img-p146.jpg:occ-01]]</code> | [<code>raw/9/item/image/img-p146.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/img-p146.jpg) | [<code>raw/9/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-008.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p146.jpg"}</code> |
| 11 | <code>[[EPUB_IMAGE:v9:xhtml/p-010.xhtml:img-p248.jpg:occ-01]]</code> | [<code>raw/9/item/image/img-p248.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/img-p248.jpg) | [<code>raw/9/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-010.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p248.jpg"}</code> |
| 12 | <code>[[EPUB_IMAGE:v9:xhtml/p-allcover-001.xhtml:allcover-001.jpg:occ-01]]</code> | [<code>raw/9/item/image/allcover-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/allcover-001.jpg) | [<code>raw/9/item/xhtml/p-allcover-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-allcover-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "829", "href": "../image/allcover-001.jpg"}</code> |
| 13 | <code>[[EPUB_IMAGE:v9:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/9/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/image/i-bookwalker.jpg) | [<code>raw/9/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/9/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　contents

[empty paragraph]

[empty paragraph]

[『あの日々の続きにいる』 - today was tomorrow -](p-002.xhtml#toc-001)

[『青鷺の湖』 - a stolen veil -](p-004.xhtml#toc-002)

[『時は止まりそして流れる』 - glints of lives -](p-006.xhtml#toc-003)

[『新品の天秤の右と左』 - where to go, what to be -](p-008.xhtml#toc-004)

[『苦くて優しい夢の中』 - it will be a beautiful world -](p-010.xhtml#toc-005)

[あとがき／あれからどれくらい──](p-012.xhtml#toc-006)
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
