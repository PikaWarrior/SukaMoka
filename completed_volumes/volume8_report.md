# Отчёт об извлечении японского исходника — том 8

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/allcover-001.jpg</code> | 369514 | <code>e149f40cf27b8c5f7e4b2297da26dd9a3fb7b3c5451eb73e58ac9730e4695b63</code> |
| <code>image/cover.jpg</code> | 1354958 | <code>2474f289a3aab144b36413e6db291b623186c392d806fc95df08ff773c1a0e4a</code> |
| <code>image/gaiji-cid776-m-v.png</code> | 4828 | <code>f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf</code> |
| <code>image/i-bookwalker.jpg</code> | 342205 | <code>7cd722f5a19b77ac2c3b9e336a39ecc9803b7a4263dd236f4e8253f15adf2a4a</code> |
| <code>image/kuchie-001.jpg</code> | 1156494 | <code>7ab0cfccd1a8fa1fdbdd32ffeb05163812759a44896007804e29d683f877bb73</code> |
| <code>image/kuchie-002.jpg</code> | 1016417 | <code>9a7ee36e13d547cafbaa95a0d6717730a1049f8b18de784c21982b9d6b361e9c</code> |
| <code>image/p004-005.jpg</code> | 483166 | <code>67d07e5b51d1da2212268d6d90130c0981e591eef2a16a2fe3f706ae9753adfc</code> |
| <code>image/p016-017.jpg</code> | 795065 | <code>be32148b63f92b6cc176b133e5f7f66b7c4f5d582c1bc4b7313afaadba545043</code> |
| <code>image/p098-099.jpg</code> | 626859 | <code>d87564802b96f33d2b1a181373c6a18eeb9d900b1280e812483e60400cbd60c8</code> |
| <code>image/p196-197.jpg</code> | 918631 | <code>d616a66867aafbbdf7730b00db04204a8537248ba690d030b8c8ba6a1ef9a54d</code> |
| <code>image/p300-301.jpg</code> | 866514 | <code>0f557fb283a8e8c51b5bf792f44578662a39b7a5db1ae7fb2f16cc8bf1c160e2</code> |
| <code>image/titlepage.jpg</code> | 85840 | <code>3a1aa115e646d737ff0f58cfaafad4ea12333b540b88be3a3809063d80ef703c</code> |
| <code>image/toc-001.jpg</code> | 785383 | <code>83e87a5b68fcd243a97d2db5d3505025bcae4dff5fe79908a98a9b21c1474181</code> |
| <code>navigation-documents.xhtml</code> | 1482 | <code>2410447aa6b490c529b5a9f81c4dac4ede5d339db078bfb63321a1dbc5172edd</code> |
| <code>standard.opf</code> | 9674 | <code>05d1895bc7a6950a7d949d4b12e14abaaf94cd63ee96dad44167319baf3e2bbf</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 7766 | <code>067299fc4af21b7575f079b857255b78acce60ee04d503db8126d7723ef44d07</code> |
| <code>style/style-karc.css</code> | 1927 | <code>067ce6303605275a60389c7fb8cd59ef0ca47b6ba8eebe6f6438686f1f67552a</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 797 | <code>693d4bb47af790ba22711e4e04f282de31152cc90f86c7f42c4b3f3461885a09</code> |
| <code>xhtml/p-002.xhtml</code> | 18733 | <code>8045bfcd0982ca261dc17f922aad11f7aa8a1160a3f8653854e7f0bbe9d400ce</code> |
| <code>xhtml/p-003.xhtml</code> | 821 | <code>2377cbea75f7852f401c8fe25a080776b11254359bf0175d8128f10de5ba532b</code> |
| <code>xhtml/p-004.xhtml</code> | 148076 | <code>d88767dc84e2db8546976d0f7d0da9228d9d806a1fd059148bf5b7b246789b74</code> |
| <code>xhtml/p-005.xhtml</code> | 809 | <code>14944998be3cb767097131c21df69248cf0b99a15fd1e6683a9b32f778cde753</code> |
| <code>xhtml/p-006.xhtml</code> | 166774 | <code>09a4bea4f6b941bbf9e966769346e0987525f2e27e3ba89e4adbfc0d956fe7b8</code> |
| <code>xhtml/p-007.xhtml</code> | 818 | <code>6e10a317fd76a669d296c0b8de5d75928163394b4455530d12febbf6701d163e</code> |
| <code>xhtml/p-008.xhtml</code> | 174482 | <code>4856e247d4d5d0a14ff87d2de90525671fc71ae446115d9534f7c4a7ce6a5946</code> |
| <code>xhtml/p-009.xhtml</code> | 810 | <code>2c3b9d7aef0b01bdc58135155766c05f685c68f5a39a20b121453f8c5d0b17c7</code> |
| <code>xhtml/p-010.xhtml</code> | 11320 | <code>2026b375a8b3e40428fd5f7be09a17b13791226cf466bdfb095eaad3d3a0aba5</code> |
| <code>xhtml/p-011.xhtml</code> | 567 | <code>b11956711c132df0008703e601903c9db9643c06231a5d5515a1fea4c934520d</code> |
| <code>xhtml/p-012.xhtml</code> | 12649 | <code>66f641fdd01f7015d0132806b33ec50861e6cde9065d252f23531b4681f5f316</code> |
| <code>xhtml/p-013.xhtml</code> | 2336 | <code>947875651932c66bec818fe2f71c1df01a555461acdd7c0ac0bccc1dc9bc68a8</code> |
| <code>xhtml/p-allcover-001.xhtml</code> | 728 | <code>4faf70bca44a4df8dfd1bf9300106b6b3943bdf1fb24217106e5622767af6de0</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>65719179002ebb0468c3ba14986dda2049ad4c6a087daba3350b8c2189eeb97d</code> |
| <code>xhtml/p-caution.xhtml</code> | 789 | <code>49c6724be5fe694366b3fb9b9f34b5b4d575a047ee916c7093e807669a02ec67</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2324 | <code>0fbca188e1fbf6cc3c96f52c9a02e32e69c451cb9730b8e3cded3e2d76131f0c</code> |
| <code>xhtml/p-colophon2.xhtml</code> | 1056 | <code>90ee00a64dce42da1a628ec71700f105eb00622608a5cc1e33736f0439179c40</code> |
| <code>xhtml/p-cover.xhtml</code> | 742 | <code>4dd6aaa5e00170d503116e3b2571819adb977958082a3463aefddae95192cfd8</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 729 | <code>29ed9ec5f84cda4af6069be9ed28f3c12fa9376617cd559a4e45a7b7d2f5722d</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 729 | <code>04d648528a44a3031448108e1bad619ed62d640c9280131dc04667c2df6262fe</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 728 | <code>78aee6258a149243dcd20d0919bd9785949730786a7ab6d8b2b0eb9c4302fd10</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 726 | <code>63cd4854b08f6fc9dd0e1bc0c31670abeb4bd64e3c72770897000a832fb261fa</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1408 | <code>7d5b63a23bc8578a48608c9adbb43b2533499428fed89d56d37be5882b65e220</code> |

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
| p016-017 | <code>image/p016-017.jpg</code> | image/jpeg | да | локальная ссылка |
| p098-099 | <code>image/p098-099.jpg</code> | image/jpeg | да | локальная ссылка |
| p196-197 | <code>image/p196-197.jpg</code> | image/jpeg | да | локальная ссылка |
| p300-301 | <code>image/p300-301.jpg</code> | image/jpeg | да | локальная ссылка |
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
| p-009 | <code>xhtml/p-009.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-010 | <code>xhtml/p-010.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-011 | <code>xhtml/p-011.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
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
| 9 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 111 | 137 | 212 | 1 |
| 10 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 11 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 855 | 1027 | 1545 | 8 |
| 12 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 13 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 1047 | 1101 | 1640 | 9 |
| 14 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 15 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 1169 | 1150 | 1657 | 13 |
| 16 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 17 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 88 | 59 | 78 | 0 |
| 18 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 4 | 0 | 0 | 0 |
| 19 | <code>p-012</code> | <code>xhtml/p-012.xhtml</code> | parsed | 93 | 68 | 93 | 1 |
| 20 | <code>p-013</code> | <code>xhtml/p-013.xhtml</code> | parsed | 9 | 9 | 12 | 0 |
| 21 | <code>p-allcover-001</code> | <code>xhtml/p-allcover-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 22 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 17 | 5 | 8 | 0 |
| 23 | <code>p-colophon2</code> | <code>xhtml/p-colophon2.xhtml</code> | parsed | 3 | 0 | 0 | 0 |
| 24 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-012.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-013.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-allcover-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-colophon2.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#08 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『雨烟る夜、承前』 - unmasked deadman - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『残された日々と、残された人々』 - singing in the rain - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『雄弁な死者と、生きる理由』 - heartless man - | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> |
| 『その日々に手を伸ばして』 - weight of the weird world - | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> |
| 『もう一度だけ、会えますか？』 - starry dawn - | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> |
| あとがき／あとどれくらい── | <code>xhtml/p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 24; сопоставлены с manifest: 24.
- Абзацы p в основном потоке: 3400; пустых p, отмеченных [пауза]: 224.
- br-элементов: 224; em-sesame: 29.
- Начальных отступов снято: 2033 символов в 1905 абзацах; нестандартных случаев подробно перечислено: 32.
- CSS-классов в XHTML: 44 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 44; уникальных ресурсов в маркерах: 13.
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
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 7 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 34 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 70 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 68 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 6 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 296 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 485 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | empty/whitespace-only | 73 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | heading/style heading | 7 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | no indent / dialogue-like | 374 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | one U+3000 | 593 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 90 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 7 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 444 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 628 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 4 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 18 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 66 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 3 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 1 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | empty/whitespace-only | 8 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | no indent / dialogue-like | 27 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | one U+3000 | 58 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | empty/whitespace-only | 2 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-013.xhtml</code> | no indent / other | 2 | 8-9 |
| <code>xhtml/p-013.xhtml</code> | one U+3000 | 4 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 3 | 1, 3-4 |
| <code>xhtml/p-colophon.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 16 | 1-13, 15-17 |
| <code>xhtml/p-colophon2.xhtml</code> | no indent / other | 3 | 1-3 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-002.xhtml</code> | 15 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 37 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 112 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 151 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 398 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 534 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 620 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 707 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 789 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 37 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 102 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 108 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 255 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 332 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 444 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 506 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 588 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 681 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 20 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 87 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 309 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 349 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 459 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 565 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 638 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 749 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 835 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 988 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 998 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 1052 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 1132 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-012.xhtml</code> | 27 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 1 |
| book-title | div | 1 |
| book-title-main | div | 1 |
| copyright | div | 1 |
| em-sesame | span | 29 |
| font-0em80 | div | 1 |
| font-1em10 | p | 20 |
| font-1em10 | span | 7 |
| font-1em30 | p | 1 |
| font-1em30 | span | 1 |
| gaiji | img | 32 |
| gfont | div | 1 |
| gfont | span | 7 |
| h-indent-2em | p | 20 |
| hltr | html | 2 |
| label | div | 1 |
| label-name | p | 1 |
| line-break-loose | p | 28 |
| line-break-loose | span | 29 |
| main | div | 24 |
| mfont | div | 1 |
| mfont | p | 21 |
| mfont | span | 2 |
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
| release-version | div | 1 |
| start-1em | div | 1 |
| start-2em | div | 1 |
| start-3em | div | 21 |
| support | div | 1 |
| support-contact | p | 1 |
| support-desk | p | 1 |
| support-note-01 | p | 1 |
| support-note-02 | p | 1 |
| support-note-03 | p | 1 |
| support-note-04 | p | 1 |
| tcy | span | 72 |
| vrtl | html | 10 |
| word-break-break-all | span | 29 |

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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
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
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-001.xhtml</code> | <code>../image/p004-005.jpg</code> | <code>image/p004-005.jpg</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-002.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../image/p016-017.jpg</code> | <code>image/p016-017.jpg</code> | OK |
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
| <code>xhtml/p-005.xhtml</code> | <code>../image/p098-099.jpg</code> | <code>image/p098-099.jpg</code> | OK |
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
| <code>xhtml/p-007.xhtml</code> | <code>../image/p196-197.jpg</code> | <code>image/p196-197.jpg</code> | OK |
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
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../image/p300-301.jpg</code> | <code>image/p300-301.jpg</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-012.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
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
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> | OK |
| <code>navigation-documents.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> | OK |
| <code>xhtml/p-toc-002.xhtml</code> | <code>p-013.xhtml#toc-006</code> | <code>xhtml/p-013.xhtml</code> | OK |

## Карта размещений изображений

Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.

| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |
|---:|---|---|---|---|---|---|
| 1 | <code>[[EPUB_IMAGE:v8:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/8/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/cover.jpg) | [<code>raw/8/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v8:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/8/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/kuchie-001.jpg) | [<code>raw/8/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1624", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v8:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/8/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/kuchie-002.jpg) | [<code>raw/8/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1624", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v8:xhtml/p-titlepage.xhtml:titlepage.jpg:occ-01]]</code> | [<code>raw/8/item/image/titlepage.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/titlepage.jpg) | [<code>raw/8/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/titlepage.jpg"}</code> |
| 5 | <code>[[EPUB_IMAGE:v8:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/8/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/toc-001.jpg) | [<code>raw/8/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1453", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v8:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/8/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/p004-005.jpg) | [<code>raw/8/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/p004-005.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v8:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 8 | <code>[[EPUB_IMAGE:v8:xhtml/p-003.xhtml:p016-017.jpg:occ-01]]</code> | [<code>raw/8/item/image/p016-017.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/p016-017.jpg) | [<code>raw/8/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/p016-017.jpg"}</code> |
| 9 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 10 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 11 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 12 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 15 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v8:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 17 | <code>[[EPUB_IMAGE:v8:xhtml/p-005.xhtml:p098-099.jpg:occ-01]]</code> | [<code>raw/8/item/image/p098-099.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/p098-099.jpg) | [<code>raw/8/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/p098-099.jpg"}</code> |
| 18 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 19 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 20 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 22 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 25 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v8:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v8:xhtml/p-007.xhtml:p196-197.jpg:occ-01]]</code> | [<code>raw/8/item/image/p196-197.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/p196-197.jpg) | [<code>raw/8/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-007.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/p196-197.jpg"}</code> |
| 28 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 29 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 30 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 31 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 32 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 33 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 34 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 35 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 36 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 37 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-10]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 38 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-11]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 39 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-12]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 40 | <code>[[EPUB_IMAGE:v8:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-13]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 41 | <code>[[EPUB_IMAGE:v8:xhtml/p-009.xhtml:p300-301.jpg:occ-01]]</code> | [<code>raw/8/item/image/p300-301.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/p300-301.jpg) | [<code>raw/8/item/xhtml/p-009.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-009.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/p300-301.jpg"}</code> |
| 42 | <code>[[EPUB_IMAGE:v8:xhtml/p-012.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/8/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/gaiji-cid776-m-v.png) | [<code>raw/8/item/xhtml/p-012.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-012.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 43 | <code>[[EPUB_IMAGE:v8:xhtml/p-allcover-001.xhtml:allcover-001.jpg:occ-01]]</code> | [<code>raw/8/item/image/allcover-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/allcover-001.jpg) | [<code>raw/8/item/xhtml/p-allcover-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-allcover-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "829", "href": "../image/allcover-001.jpg"}</code> |
| 44 | <code>[[EPUB_IMAGE:v8:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/8/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/image/i-bookwalker.jpg) | [<code>raw/8/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/8/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『雨烟る夜、承前』 - unmasked deadman -](p-001.xhtml#toc-001)

[『残された日々と、残された人々』 - singing in the rain -](p-003.xhtml#toc-002)

[『雄弁な死者と、生きる理由』 - heartless man -](p-005.xhtml#toc-003)

[『その日々に手を伸ばして』 - weight of the weird world -](p-007.xhtml#toc-004)

[『もう一度だけ、会えますか？』 - starry dawn -](p-009.xhtml#toc-005)

[あとがき／あとどれくらい──](p-013.xhtml#toc-006)
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
