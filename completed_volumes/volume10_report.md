# Отчёт об извлечении японского исходника — том 10

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/allcover-001.jpg</code> | 303073 | <code>898df8628f1aa081a360c4f9952c3bbb2765c755d45de4955f7f39613c7ce365</code> |
| <code>image/cover.jpg</code> | 728784 | <code>072fe933512bc83bbdd0605d25a781e184befcf11d9a6f3d13746aa4b0c2c7f9</code> |
| <code>image/i-bookwalker.jpg</code> | 342205 | <code>7cd722f5a19b77ac2c3b9e336a39ecc9803b7a4263dd236f4e8253f15adf2a4a</code> |
| <code>image/img-p003.jpg</code> | 566867 | <code>453a79c35487c213815309d6721fbee612e3bd565fcc6fab01667a9ea1cbc707</code> |
| <code>image/img-p004-005.jpg</code> | 675349 | <code>5e339ed48502d36be7d3817bcc975038a1afa001182d27058f7de261e3eb65aa</code> |
| <code>image/img-p014-015.jpg</code> | 365555 | <code>a45eb18e164afd773eeab6cec8145bdfa3b85c8695df26eb72ce8159a3f01215</code> |
| <code>image/img-p122-123.jpg</code> | 478449 | <code>3c79b5b7877225c226d4a02a4ade1869832ee597c28b2819206f67ba9d984b08</code> |
| <code>image/img-p202-203.jpg</code> | 440038 | <code>a05413db1bc17c568b91740e57aa07da91fccec8da3b5e324fe9584a1ebe59fa</code> |
| <code>image/img-p304-305.jpg</code> | 590482 | <code>44458f9cdc3ad0d2f6ef92f5c030888a8ee3171ef15cfaf1171a80fd31070913</code> |
| <code>image/kuchie-001.jpg</code> | 1290247 | <code>f4c2fe28602cc21aac2217853037e85cb446ee1332d015ed832723431dc7163a</code> |
| <code>image/kuchie-002.jpg</code> | 783907 | <code>32097e4e8855ff3f319b600610211b72bae07ca656849f393a9a18b3993a6c06</code> |
| <code>image/titlepage.jpg</code> | 104443 | <code>90a2dcc1f599b18cd6b89235a3dbd04378d63fcab35343f0becd807eac2928e7</code> |
| <code>image/toc-001.jpg</code> | 411079 | <code>8d98548e2238edcac72bacbc6d560852681c4ea827b6a2e9bb0a49e7f0f3da6b</code> |
| <code>navigation-documents.xhtml</code> | 1469 | <code>52be5ab91af5d531fa36e32e89de41617b45c7a257e8908d71ec8e6b705b8c7e</code> |
| <code>standard.opf</code> | 9385 | <code>2f934a8f33020e8fe181be5ddc9dc51fc0404c781ae562c86e9550d30995d972</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 7766 | <code>067299fc4af21b7575f079b857255b78acce60ee04d503db8126d7723ef44d07</code> |
| <code>style/style-karc.css</code> | 1927 | <code>067ce6303605275a60389c7fb8cd59ef0ca47b6ba8eebe6f6438686f1f67552a</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 727 | <code>325c069e254a0973ef2514e63439667fedfd8316f120b18f241dca6a757d385a</code> |
| <code>xhtml/p-002.xhtml</code> | 812 | <code>bf8522c7b9c743b4050973ed71d9611ee1e5f1b42bd9ce7c3347bf933079954f</code> |
| <code>xhtml/p-003.xhtml</code> | 15527 | <code>eaa535fc68097571a28ba178ca02bcc8e33f80c1934eccb9030e35af5a94a896</code> |
| <code>xhtml/p-004.xhtml</code> | 834 | <code>ca8b99823cd46c7651feeef17a06871040483c64b4b483246d4bbee0e3d1f3e1</code> |
| <code>xhtml/p-005.xhtml</code> | 185586 | <code>e08e30debe152ef3758ee65bcbbf86f22fd4015c0cae7d16ab3e9d601ceb9816</code> |
| <code>xhtml/p-006.xhtml</code> | 816 | <code>3edb505a015b34a498e859384b2be709f14a7edcd107ab6b4131ad1e9ecc9780</code> |
| <code>xhtml/p-007.xhtml</code> | 133999 | <code>d0c50e1553b0f15a0fd2eb5e4b625b891b91a5f2d02b634d2713bb1d86cf44ee</code> |
| <code>xhtml/p-008.xhtml</code> | 825 | <code>48550a8fc2708d410e507aa44fca9bf879500394f2f6a35f82bac514d92a656e</code> |
| <code>xhtml/p-009.xhtml</code> | 166217 | <code>22928e84172515ff0ebd3611da10fd5f595a7735b2c8d8cf83a8714b5cba6ce0</code> |
| <code>xhtml/p-010.xhtml</code> | 793 | <code>abb91c0efbff14dc4433691d0a696d15fc850d93e9386b8c8d2341ca991ebda5</code> |
| <code>xhtml/p-011.xhtml</code> | 16774 | <code>6039613949a942ff030546d57e1bcfad2920b1cec32a646e41410e6a7b16a9c2</code> |
| <code>xhtml/p-012.xhtml</code> | 6704 | <code>f6a35bf682efc38f5a7d5015b194f70fae7166dd8004a14ead5f15d05ee15286</code> |
| <code>xhtml/p-allcover-001.xhtml</code> | 728 | <code>4d12b0cabaaf16cbe99692e1c04b51b95c6916b4c150e685b50ebdcba0570d81</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 671 | <code>65719179002ebb0468c3ba14986dda2049ad4c6a087daba3350b8c2189eeb97d</code> |
| <code>xhtml/p-caution.xhtml</code> | 789 | <code>49c6724be5fe694366b3fb9b9f34b5b4d575a047ee916c7093e807669a02ec67</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2322 | <code>4c3842330dc698d7bb1f10698ec2efecd91fe49f24809a4ddd940cf684be2a4d</code> |
| <code>xhtml/p-colophon2.xhtml</code> | 1056 | <code>d858dacb5685ad157a36037f8ee3654e90de536e4b964edd367b2d0c833c7218</code> |
| <code>xhtml/p-cover.xhtml</code> | 742 | <code>6a83b25f561167a1afcc8b43db057f9fdeef8a1de5cad50b86b88b610a9ff8f4</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 729 | <code>4cc0f0662dbc73bda283a6fd69def1d381514e6b8addfdc170746fe7f8eda94d</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 729 | <code>0d580e6d52755dacb26b944dc0d67cf767162b0dc6c55ff19910391456cc0a93</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 728 | <code>839aec2e486a46239b65d186dfb2105c7eba1e0127a70d6bc8038e70dbd0dc1d</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 726 | <code>312f65a09127dcc1489cf355c91bd312fc755639541c9379cb82a9934ee3f158</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1519 | <code>a6f2df078d603a6b7be4687884d05b291992d0d72b20f9f06ac23d3a0a8e91af</code> |

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
| img-p003 | <code>image/img-p003.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p004-005 | <code>image/img-p004-005.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p014-015 | <code>image/img-p014-015.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p122-123 | <code>image/img-p122-123.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p202-203 | <code>image/img-p202-203.jpg</code> | image/jpeg | да | локальная ссылка |
| img-p304-305 | <code>image/img-p304-305.jpg</code> | image/jpeg | да | локальная ссылка |
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
| 10 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 82 | 112 | 165 | 0 |
| 11 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 12 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 1109 | 1172 | 1647 | 0 |
| 13 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 14 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 871 | 923 | 1253 | 0 |
| 15 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 16 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 1169 | 1124 | 1565 | 0 |
| 17 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 18 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 87 | 100 | 148 | 0 |
| 19 | <code>p-012</code> | <code>xhtml/p-012.xhtml</code> | parsed | 28 | 30 | 43 | 0 |
| 20 | <code>p-allcover-001</code> | <code>xhtml/p-allcover-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 21 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 17 | 5 | 8 | 0 |
| 22 | <code>p-colophon2</code> | <code>xhtml/p-colophon2.xhtml</code> | parsed | 3 | 0 | 0 | 0 |
| 23 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-012.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-allcover-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-colophon2.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？ もう一度だけ、会えますか？#10 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| contents | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『そして、この空に至る』 - through the breach - | <code>xhtml/p-002.xhtml#toc-001</code> | <code>xhtml/p-002.xhtml</code> |
| 『存在を許されない揺籃の世界（上）』 - what a beautiful world - | <code>xhtml/p-004.xhtml#toc-002</code> | <code>xhtml/p-004.xhtml</code> |
| 『世界を壊す五羽の妖精（上）』 - cracked stage - | <code>xhtml/p-006.xhtml#toc-003</code> | <code>xhtml/p-006.xhtml</code> |
| 『その選択肢は問いかける（上）』 - worldend emissaries - | <code>xhtml/p-008.xhtml#toc-004</code> | <code>xhtml/p-008.xhtml</code> |
| 『世界の果て』 - world's edge - | <code>xhtml/p-010.xhtml#toc-005</code> | <code>xhtml/p-010.xhtml</code> |
| あとがき／あともうすこしだけ | <code>xhtml/p-012.xhtml#toc-006</code> | <code>xhtml/p-012.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 23; сопоставлены с manifest: 23.
- Абзацы p в основном потоке: 3370; пустых p, отмеченных [пауза]: 208.
- br-элементов: 208; em-sesame: 71.
- Начальных отступов снято: 1984 символов в 1894 абзацах; нестандартных случаев подробно перечислено: 30.
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
| <code>xhtml/p-003.xhtml</code> | empty/whitespace-only | 4 | сводный учёт |
| <code>xhtml/p-003.xhtml</code> | no indent / dialogue-like | 34 | сводный учёт |
| <code>xhtml/p-003.xhtml</code> | one U+3000 | 44 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | empty/whitespace-only | 70 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | multiple U+3000 | 10 | 48, 208, 345, 411, 617, 654, 683, 791, 898, 994 |
| <code>xhtml/p-005.xhtml</code> | no indent / dialogue-like | 351 | сводный учёт |
| <code>xhtml/p-005.xhtml</code> | no indent / other | 8 | 1, 40, 143, 328, 431, 604, 709, 971 |
| <code>xhtml/p-005.xhtml</code> | one U+3000 | 670 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | empty/whitespace-only | 55 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | multiple U+3000 | 9 | 27, 111, 126, 243, 383, 388, 485, 620, 788 |
| <code>xhtml/p-007.xhtml</code> | no indent / dialogue-like | 315 | сводный учёт |
| <code>xhtml/p-007.xhtml</code> | no indent / other | 7 | 1, 82, 202, 350, 468, 662, 778 |
| <code>xhtml/p-007.xhtml</code> | one U+3000 | 485 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | empty/whitespace-only | 63 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | multiple U+3000 | 10 | 13, 120, 206, 338, 480, 506, 633, 816, 899, 1108 |
| <code>xhtml/p-009.xhtml</code> | no indent / dialogue-like | 495 | сводный учёт |
| <code>xhtml/p-009.xhtml</code> | no indent / other | 8 | 1, 86, 295, 459, 560, 763, 879, 1040 |
| <code>xhtml/p-009.xhtml</code> | one U+3000 | 593 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 8 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | multiple U+3000 | 1 | 36 |
| <code>xhtml/p-011.xhtml</code> | no indent / dialogue-like | 24 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 54 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | empty/whitespace-only | 7 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-012.xhtml</code> | no indent / other | 2 | 27-28 |
| <code>xhtml/p-012.xhtml</code> | one U+3000 | 18 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | empty/whitespace-only | 1 | сводный учёт |
| <code>xhtml/p-caution.xhtml</code> | no indent / other | 3 | 1, 3-4 |
| <code>xhtml/p-colophon.xhtml</code> | no indent / dialogue-like | 1 | сводный учёт |
| <code>xhtml/p-colophon.xhtml</code> | no indent / other | 16 | 1-13, 15-17 |
| <code>xhtml/p-colophon2.xhtml</code> | no indent / other | 3 | 1-3 |

### Подробности нестандартных удалённых отступов

| XHTML | p № | Начальный отступ (repr) | Удалено символов | Классы | Фрагмент после удаления |
|---|---:|---|---:|---|---|
| <code>xhtml/p-005.xhtml</code> | 48 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 208 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 345 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 411 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 617 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 654 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 683 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 791 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 898 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-005.xhtml</code> | 994 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 27 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 111 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 126 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 243 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 383 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 388 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 485 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 620 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-007.xhtml</code> | 788 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 13 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 120 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 206 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 338 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 480 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 506 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 633 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 816 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 899 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-009.xhtml</code> | 1108 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |
| <code>xhtml/p-011.xhtml</code> | 36 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> | † |


### Использование CSS-классов в XHTML

Классы перечислены даже если их оформление не переносится в Markdown; это позволяет заметить потенциально значимые классы.

| Класс | Элемент | Количество |
|---|---|---:|
| align-end | div | 1 |
| author | div | 1 |
| book-title | div | 1 |
| book-title-main | div | 1 |
| copyright | div | 1 |
| em-sesame | span | 71 |
| end-1em | div | 1 |
| font-0em80 | div | 1 |
| font-0em90 | span | 5 |
| font-1em10 | span | 7 |
| font-1em30 | p | 1 |
| font-1em30 | span | 24 |
| gfont | div | 2 |
| hltr | html | 2 |
| label | div | 1 |
| label-name | p | 1 |
| line-break-loose | p | 19 |
| line-break-loose | span | 19 |
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
| start-3em | div | 24 |
| support | div | 1 |
| support-contact | p | 1 |
| support-desk | p | 1 |
| support-note-01 | p | 1 |
| support-note-02 | p | 1 |
| support-note-03 | p | 1 |
| support-note-04 | p | 1 |
| tcy | span | 81 |
| vrtl | html | 8 |
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
| <code>xhtml/p-002.xhtml</code> | <code>../image/img-p004-005.jpg</code> | <code>image/img-p004-005.jpg</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/img-p014-015.jpg</code> | <code>image/img-p014-015.jpg</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/img-p122-123.jpg</code> | <code>image/img-p122-123.jpg</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/img-p202-203.jpg</code> | <code>image/img-p202-203.jpg</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../image/img-p304-305.jpg</code> | <code>image/img-p304-305.jpg</code> | OK |
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
| 1 | <code>[[EPUB_IMAGE:v10:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/10/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/cover.jpg) | [<code>raw/10/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v10:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/10/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/kuchie-001.jpg) | [<code>raw/10/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1624", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v10:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/10/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/kuchie-002.jpg) | [<code>raw/10/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1624", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v10:xhtml/p-titlepage.xhtml:titlepage.jpg:occ-01]]</code> | [<code>raw/10/item/image/titlepage.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/titlepage.jpg) | [<code>raw/10/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/titlepage.jpg"}</code> |
| 5 | <code>[[EPUB_IMAGE:v10:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/10/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/toc-001.jpg) | [<code>raw/10/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/toc-001.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v10:xhtml/p-001.xhtml:img-p003.jpg:occ-01]]</code> | [<code>raw/10/item/image/img-p003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/img-p003.jpg) | [<code>raw/10/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/img-p003.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v10:xhtml/p-002.xhtml:img-p004-005.jpg:occ-01]]</code> | [<code>raw/10/item/image/img-p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/img-p004-005.jpg) | [<code>raw/10/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p004-005.jpg"}</code> |
| 8 | <code>[[EPUB_IMAGE:v10:xhtml/p-004.xhtml:img-p014-015.jpg:occ-01]]</code> | [<code>raw/10/item/image/img-p014-015.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/img-p014-015.jpg) | [<code>raw/10/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-004.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p014-015.jpg"}</code> |
| 9 | <code>[[EPUB_IMAGE:v10:xhtml/p-006.xhtml:img-p122-123.jpg:occ-01]]</code> | [<code>raw/10/item/image/img-p122-123.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/img-p122-123.jpg) | [<code>raw/10/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-006.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p122-123.jpg"}</code> |
| 10 | <code>[[EPUB_IMAGE:v10:xhtml/p-008.xhtml:img-p202-203.jpg:occ-01]]</code> | [<code>raw/10/item/image/img-p202-203.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/img-p202-203.jpg) | [<code>raw/10/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-008.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p202-203.jpg"}</code> |
| 11 | <code>[[EPUB_IMAGE:v10:xhtml/p-010.xhtml:img-p304-305.jpg:occ-01]]</code> | [<code>raw/10/item/image/img-p304-305.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/img-p304-305.jpg) | [<code>raw/10/item/xhtml/p-010.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-010.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "1474", "href": "../image/img-p304-305.jpg"}</code> |
| 12 | <code>[[EPUB_IMAGE:v10:xhtml/p-allcover-001.xhtml:allcover-001.jpg:occ-01]]</code> | [<code>raw/10/item/image/allcover-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/allcover-001.jpg) | [<code>raw/10/item/xhtml/p-allcover-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-allcover-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2048", "height": "829", "href": "../image/allcover-001.jpg"}</code> |
| 13 | <code>[[EPUB_IMAGE:v10:xhtml/p-bookwalker.xhtml:i-bookwalker.jpg:occ-01]]</code> | [<code>raw/10/item/image/i-bookwalker.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/image/i-bookwalker.jpg) | [<code>raw/10/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/10/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1443", "height": "2048", "href": "../image/i-bookwalker.jpg"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　contents

[empty paragraph]

[empty paragraph]

[『そして、この空に至る』 - through the breach -](p-002.xhtml#toc-001)

[『存在を許されない揺籃の世界（上）』 - what a beautiful world -](p-004.xhtml#toc-002)

[『世界を壊す五羽の妖精（上）』 - cracked stage -](p-006.xhtml#toc-003)

[『その選択肢は問いかける（上）』 - worldend emissaries -](p-008.xhtml#toc-004)

[『世界の果て』 - world's edge -](p-010.xhtml#toc-005)

[あとがき／あともうすこしだけ](p-012.xhtml#toc-006)
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
