# Отчёт об извлечении японского исходника — том 1

## Метод и ограничения

Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.
XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.

## Все файлы item/

| Путь | Байты | SHA-256 |
|---|---:|---|
| <code>image/bookwalker.png</code> | 17491 | <code>35e02cbc180a9e68fc3cf4040b00c2a48e8a70c6df9dd40b98178fbc03768bac</code> |
| <code>image/cover.jpg</code> | 1544080 | <code>6244635e99da1d0a31e5f84f45d1330f03bc10b9c95cc70235d7302f0d32c399</code> |
| <code>image/gaiji-cid15190-m-v.png</code> | 6498 | <code>1fb942d415b17f03a5e42efb69c1bf7ea056a46e19df6b2d695b46163e3ed881</code> |
| <code>image/gaiji-cid776-m-v.png</code> | 4828 | <code>f0cb553916bbc0bf12101951150e0b1fe55eaa1ae630981048f8d67317fe7cdf</code> |
| <code>image/kuchie-001.jpg</code> | 388473 | <code>d3688cad73b525419230203a2b4bc6129615616169d68fa5f2ebeb4152b4e6d0</code> |
| <code>image/kuchie-002.jpg</code> | 663984 | <code>fe40b086243a696b703659fa13d5e4da873df686e742699252e5a42935eed36a</code> |
| <code>image/kuchie-003.jpg</code> | 806265 | <code>b7a8429c71668a583b007ea77f54297674da6af35e7119bcefbefba766eb8015</code> |
| <code>image/kuchie-004.jpg</code> | 598829 | <code>418941c4a7ed7acd2e0ae84b5686c3df1c673005ce667234a9b9473a10285f14</code> |
| <code>image/kuchie-005.jpg</code> | 301003 | <code>0ead950754e6d2764885294ebe7edfddbdc98b25643c975359195e7da053d00a</code> |
| <code>image/logo-sneaker.png</code> | 4267 | <code>3c68cdfe60118126cac64e2efc73d20294a63b7c1cece9c1adfb59553fa93f88</code> |
| <code>image/p004-005.jpg</code> | 1126651 | <code>82bab79caac03650424d3ec73416f9c6939b130eda8a75b3f283c4a82e37d861</code> |
| <code>image/p018-019.jpg</code> | 895112 | <code>306c59dce7eb46f6ad5f0ecd773bf25c12ecf4818e79b247235b5349114f4b06</code> |
| <code>image/p106-107.jpg</code> | 783745 | <code>0e681bc04f2ecd0dd04dd4277235d21a5fcf6bb61565f7f9b8aca1eb4ea7450c</code> |
| <code>image/p190-191.jpg</code> | 884343 | <code>8b1a1b77dd8004e6144fb9fd1edf288dc9dadb099f4e807d08ad2b7116885e0d</code> |
| <code>image/p262-263.jpg</code> | 803733 | <code>7a2ecdc194c529df2da3306355fd0afe13124fce0dafe0c73f4a707d10af4beb</code> |
| <code>image/toc-001.jpg</code> | 716298 | <code>6b2b49f6c307662a1fef97389fc4cb34d4e1e20b0dad1120ecf47c4e11168c30</code> |
| <code>navigation-documents.xhtml</code> | 1498 | <code>97bb6aa0df99e03131f7cf8225270a7bea376470491978dc7eeb635dbe8dccda</code> |
| <code>standard.opf</code> | 10288 | <code>6f052f1200f4b802b3cde008d8c39f966706602dad1e057a1b40ed4d4b69135b</code> |
| <code>style/book-style.css</code> | 6265 | <code>8f79b97cdb18dbab2dbe585b8068361dd88dd0d579faeb76a28d5361468dcdfe</code> |
| <code>style/fixed-layout-jp.css</code> | 134 | <code>d59219401aba0594a765c38913cbad87caadae4b2e873c26b43f403f5a34f5e6</code> |
| <code>style/style-advance.css</code> | 84707 | <code>2be69e0603ce34cecce869896e37794379138b33dbf2cf7eee1459b52d0e1306</code> |
| <code>style/style-check.css</code> | 2656 | <code>d2b0c33ef50a4925baab9b7179aaa3c2845b5950682df255e40aa265e2de6b7a</code> |
| <code>style/style-kadokawa.css</code> | 5664 | <code>713e501d47d3c3ce2a53b16d16271e659ea9ef66e85083744c10297d3eb05234</code> |
| <code>style/style-karc.css</code> | 1569 | <code>4c16008a60f369029d740186aa957b960f317382331c3bb582f08fbd854051f9</code> |
| <code>style/style-reset.css</code> | 2366 | <code>105ade4b7e3d0a46e2c7abdad5bb6a8077b22895f5ed3f5024fd3d5bf7f8b899</code> |
| <code>style/style-standard.css</code> | 54465 | <code>89efe50fa7f8fe1a26776cc53d116e004b3b138faf9ef7e39ab489b92bab445a</code> |
| <code>xhtml/p-001.xhtml</code> | 791 | <code>4d02c11c03d7044160baa012f48aaf1e912d0d40b3b7bb0dd46357ac779b5a91</code> |
| <code>xhtml/p-002.xhtml</code> | 18928 | <code>7ccba195409d859cd3cacf6178e9834662b6ccf280330ef4a692da623d1fdecf</code> |
| <code>xhtml/p-003.xhtml</code> | 804 | <code>95695207c46f022d6e63f9d53f15e8d1ca4e2a29b96c5398e57364bd6be1d7ad</code> |
| <code>xhtml/p-004.xhtml</code> | 158421 | <code>ae63c82ca400708c2bca685cbf993915dd2ab590bf5e90e02f1da1788f863572</code> |
| <code>xhtml/p-005.xhtml</code> | 805 | <code>a2f3c87f1f587e62389faf436503610583a73deeb0f4b3a42eb03cb608588269</code> |
| <code>xhtml/p-006.xhtml</code> | 142227 | <code>170083ef9a41751ac2b94779da02ea650c505ce7cf850301875188de93ff4a2d</code> |
| <code>xhtml/p-007.xhtml</code> | 819 | <code>88736228710ad7787b74e1ba8066c83e0a48d0020490b691b19ef7ffb44f23cd</code> |
| <code>xhtml/p-008.xhtml</code> | 119539 | <code>7de9711cd0f8ed3c64bd4cc98870ea491a0773610c53f3c9895d5a1a4e099312</code> |
| <code>xhtml/p-009.xhtml</code> | 808 | <code>af81fe11f708a522a25a58babb3d7f2495e3b0db6b24de0f687fc4d469a838d7</code> |
| <code>xhtml/p-010.xhtml</code> | 7597 | <code>d470953418f4d38ef5fef5defc8edb5310e5ab48469e0982c3b3a701beaf4a57</code> |
| <code>xhtml/p-011.xhtml</code> | 6033 | <code>d6ee0cdabcdd8b5e00bcd25c6e41d76b2f6e400caa13c05de5f004e9c7f744ef</code> |
| <code>xhtml/p-bookwalker.xhtml</code> | 666 | <code>4d5bdead62ab679eb709e1b5b2a1aa532bb82bb2871f3a35dfd022ff0c218b3e</code> |
| <code>xhtml/p-caution.xhtml</code> | 2445 | <code>24a834c4cefa46feba2148fb926150981775ba476b8ed2002329fd7061ff5365</code> |
| <code>xhtml/p-colophon.xhtml</code> | 2122 | <code>e1e84f5a153fbacfa878538e53845ed0eeb4cf0eac72fb6cd05b334597a845e2</code> |
| <code>xhtml/p-cover.xhtml</code> | 744 | <code>a5d90f8ca8d2d411dedf306b926dc690d5f5b58607b79024119ab785212e6fae</code> |
| <code>xhtml/p-credit.xhtml</code> | 677 | <code>32d203c9dd82ddf152906eeedced48e0296bdb0542795c013c2fbdef0c854a12</code> |
| <code>xhtml/p-fmatter-001.xhtml</code> | 731 | <code>18d49882dc32fbe117795d11634b0a3ee8ac5f5480b2ed858f6b2a5afdf92cad</code> |
| <code>xhtml/p-fmatter-002.xhtml</code> | 731 | <code>c473a17846aaa38c207c51c3872f24f0a86e1fbce6a6fb566b3b429af0c365f7</code> |
| <code>xhtml/p-fmatter-003.xhtml</code> | 731 | <code>d3625c2e9d835a13e0f0f7b3fff0286b03b9b6c601367cca570fa9baf1d07d52</code> |
| <code>xhtml/p-fmatter-004.xhtml</code> | 731 | <code>581d355aa43473feb1b7e960232ad3845e16f87122f4d856bfcdb146e99b3e45</code> |
| <code>xhtml/p-fmatter-005.xhtml</code> | 731 | <code>96372795b11e5d0b6e3b9b17c636ae795afd8184150e7cb02adc44e039a87e02</code> |
| <code>xhtml/p-titlepage.xhtml</code> | 1009 | <code>b4d6999cc699d10b2717c792e75fb25f61098869811d0546407d1bc7fbd08af5</code> |
| <code>xhtml/p-toc-001.xhtml</code> | 728 | <code>388582d9b9499c664b10671e1048e84cc4b8271e3689340126311490a6947c8d</code> |
| <code>xhtml/p-toc-002.xhtml</code> | 1443 | <code>cafd734b52ea075bc9c024542020968559b39bc6086a5633b98f4aa82c947bc1</code> |

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
| kuchie-005 | <code>image/kuchie-005.jpg</code> | image/jpeg | да | локальная ссылка |
| toc-001 | <code>image/toc-001.jpg</code> | image/jpeg | да | локальная ссылка |
| p004-005 | <code>image/p004-005.jpg</code> | image/jpeg | да | локальная ссылка |
| p018-019 | <code>image/p018-019.jpg</code> | image/jpeg | да | локальная ссылка |
| p106-107 | <code>image/p106-107.jpg</code> | image/jpeg | да | локальная ссылка |
| p190-191 | <code>image/p190-191.jpg</code> | image/jpeg | да | локальная ссылка |
| p262-263 | <code>image/p262-263.jpg</code> | image/jpeg | да | локальная ссылка |
| gaiji-cid15190-m-v | <code>image/gaiji-cid15190-m-v.png</code> | image/png | да | локальная ссылка |
| gaiji-cid776-m-v | <code>image/gaiji-cid776-m-v.png</code> | image/png | да | локальная ссылка |
| logo-sneaker | <code>image/logo-sneaker.png</code> | image/png | да | локальная ссылка |
| bookwalker | <code>image/bookwalker.png</code> | image/png | да | локальная ссылка |
| p-cover | <code>xhtml/p-cover.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-001 | <code>xhtml/p-fmatter-001.xhtml</code> | application/xhtml+xml | да | локальная ссылка |
| p-fmatter-002 | <code>xhtml/p-fmatter-002.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-fmatter-003 | <code>xhtml/p-fmatter-003.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-fmatter-004 | <code>xhtml/p-fmatter-004.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
| p-fmatter-005 | <code>xhtml/p-fmatter-005.xhtml</code> | application/xhtml+xml | да | package metadata: spine |
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
| 4 | <code>p-fmatter-003</code> | <code>xhtml/p-fmatter-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 5 | <code>p-fmatter-004</code> | <code>xhtml/p-fmatter-004.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 6 | <code>p-fmatter-005</code> | <code>xhtml/p-fmatter-005.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 7 | <code>p-titlepage</code> | <code>xhtml/p-titlepage.xhtml</code> | parsed | 4 | 0 | 0 | 1 |
| 8 | <code>p-caution</code> | <code>xhtml/p-caution.xhtml</code> | parsed | 7 | 0 | 0 | 0 |
| 9 | <code>p-toc-001</code> | <code>xhtml/p-toc-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 10 | <code>p-toc-002</code> | <code>xhtml/p-toc-002.xhtml</code> | TOC logged below, not repeated | 0 | 0 | 0 | 0 |
| 11 | <code>p-001</code> | <code>xhtml/p-001.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 12 | <code>p-002</code> | <code>xhtml/p-002.xhtml</code> | parsed | 136 | 110 | 157 | 1 |
| 13 | <code>p-003</code> | <code>xhtml/p-003.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 14 | <code>p-004</code> | <code>xhtml/p-004.xhtml</code> | parsed | 945 | 1108 | 1632 | 9 |
| 15 | <code>p-005</code> | <code>xhtml/p-005.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 16 | <code>p-006</code> | <code>xhtml/p-006.xhtml</code> | parsed | 949 | 962 | 1410 | 7 |
| 17 | <code>p-007</code> | <code>xhtml/p-007.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 18 | <code>p-008</code> | <code>xhtml/p-008.xhtml</code> | parsed | 784 | 797 | 1178 | 6 |
| 19 | <code>p-009</code> | <code>xhtml/p-009.xhtml</code> | parsed | 0 | 0 | 0 | 1 |
| 20 | <code>p-010</code> | <code>xhtml/p-010.xhtml</code> | parsed | 46 | 45 | 62 | 0 |
| 21 | <code>p-011</code> | <code>xhtml/p-011.xhtml</code> | parsed | 26 | 30 | 47 | 0 |
| 22 | <code>p-credit</code> | <code>xhtml/p-credit.xhtml</code> | parsed | 5 | 0 | 0 | 0 |
| 23 | <code>p-colophon</code> | <code>xhtml/p-colophon.xhtml</code> | parsed | 14 | 5 | 8 | 1 |
| 24 | <code>p-bookwalker</code> | <code>xhtml/p-bookwalker.xhtml</code> | parsed | 0 | 0 | 0 | 1 |

## Аудит head/title

Заголовки XHTML из head — метаданные, а не автоматически видимый текст книги. Все title перечислены ниже; отличающиеся от названия тома, отсутствующие в body, не добавляются в художественный текст и получают поясняющий комментарий в основном Markdown, когда страница входит в spine.

| XHTML | Значение title | Решение |
|---|---|---|
| <code>navigation-documents.xhtml</code> | Navigation | значение встречается в body; сохраняется исходное содержимое body, title отдельно не добавляется |
| <code>xhtml/p-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-003.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-004.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-005.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-006.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-007.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-008.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-009.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-010.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-011.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-bookwalker.xhtml</code> | BOOK☆WALKER | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-caution.xhtml</code> | ご利用上の注意 | не вставлено в художественный текст; метаданные задокументированы |
| <code>xhtml/p-colophon.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-cover.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-credit.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-003.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-004.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-fmatter-005.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-titlepage.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-001.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |
| <code>xhtml/p-toc-002.xhtml</code> | 終末なにしてますか？　もう一度だけ、会えますか？#01 | совпадает с OPF-названием книги; не дублируется как текст страницы |

## Навигационные ссылки

| Текст | href | Целевой файл |
|---|---|---|
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| ｃｏｎｔｅｎｔｓ | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 『背中を追いかけて』 - next to you - | <code>xhtml/p-001.xhtml#toc-001</code> | <code>xhtml/p-001.xhtml</code> |
| 『終わりを待つ街』 - metalcraft miniature garden - | <code>xhtml/p-003.xhtml#toc-002</code> | <code>xhtml/p-003.xhtml</code> |
| 『壊れかけた天秤の右と左』 - expensive bullet - | <code>xhtml/p-005.xhtml#toc-003</code> | <code>xhtml/p-005.xhtml</code> |
| 『憧れた背中、追いかけて追いかけて』 - her blind alley - | <code>xhtml/p-007.xhtml#toc-004</code> | <code>xhtml/p-007.xhtml</code> |
| 『忙しくもないこの日々に』 - offstage of tragedy - | <code>xhtml/p-009.xhtml#toc-005</code> | <code>xhtml/p-009.xhtml</code> |
| あとがきという名のあとがき／すなわちあとがき | <code>xhtml/p-011.xhtml#toc-006</code> | <code>xhtml/p-011.xhtml</code> |
| 奥付 | <code>xhtml/p-colophon.xhtml</code> | <code>xhtml/p-colophon.xhtml</code> |
| 表紙 | <code>xhtml/p-cover.xhtml</code> | <code>xhtml/p-cover.xhtml</code> |
| 目次 | <code>xhtml/p-toc-002.xhtml</code> | <code>xhtml/p-toc-002.xhtml</code> |
| 本編 | <code>xhtml/p-fmatter-001.xhtml</code> | <code>xhtml/p-fmatter-001.xhtml</code> |

## Проверки

- XHTML parse errors: 0.
- Spine items: 24; сопоставлены с manifest: 24.
- Абзацы p в основном потоке: 2916; пустых p, отмеченных [пауза]: 191.
- br-элементов: 191; em-sesame: 6.
- Начальных отступов снято: 1730 символов в 1619 абзацах; нестандартных случаев подробно перечислено: 33.
- CSS-классов в XHTML: 38 уникальных имён; подробности приведены ниже.
- Проверено внутренних ссылок/фрагментов: 18; проблемных: 0.
- Маркеров изображений: 38; уникальных ресурсов в маркерах: 16.
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
| <code>xhtml/p-002.xhtml</code> | empty/whitespace-only | 10 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | no indent / dialogue-like | 36 | сводный учёт |
| <code>xhtml/p-002.xhtml</code> | one U+3000 | 90 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | empty/whitespace-only | 77 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | heading/style heading | 4 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | no indent / dialogue-like | 329 | сводный учёт |
| <code>xhtml/p-004.xhtml</code> | one U+3000 | 535 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | empty/whitespace-only | 64 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | heading/style heading | 4 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | no indent / dialogue-like | 357 | сводный учёт |
| <code>xhtml/p-006.xhtml</code> | one U+3000 | 524 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | empty/whitespace-only | 47 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | heading/style heading | 3 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | no indent / dialogue-like | 314 | сводный учёт |
| <code>xhtml/p-008.xhtml</code> | one U+3000 | 420 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | empty/whitespace-only | 4 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | no indent / dialogue-like | 8 | сводный учёт |
| <code>xhtml/p-010.xhtml</code> | one U+3000 | 34 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | empty/whitespace-only | 7 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | heading/style heading | 1 | сводный учёт |
| <code>xhtml/p-011.xhtml</code> | no indent / other | 2 | 25-26 |
| <code>xhtml/p-011.xhtml</code> | one U+3000 | 16 | сводный учёт |
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
| <code>xhtml/p-002.xhtml</code> | 124 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．若き四位武官 |
| <code>xhtml/p-004.xhtml</code> | 164 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 211 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．護翼軍第五師団 |
| <code>xhtml/p-004.xhtml</code> | 274 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 294 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 455 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．少女たち |
| <code>xhtml/p-004.xhtml</code> | 485 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 537 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 585 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 691 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．噂の四人 |
| <code>xhtml/p-004.xhtml</code> | 722 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 806 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-004.xhtml</code> | 889 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．使い捨ての兵器 |
| <code>xhtml/p-006.xhtml</code> | 50 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 198 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．遺跡兵装適合精霊 |
| <code>xhtml/p-006.xhtml</code> | 235 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 269 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 309 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．仲の悪い二人 |
| <code>xhtml/p-006.xhtml</code> | 370 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 532 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 558 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ４．素顔の少年 |
| <code>xhtml/p-006.xhtml</code> | 781 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-006.xhtml</code> | 908 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 2 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | １．真昼の夢 |
| <code>xhtml/p-008.xhtml</code> | 53 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ２．後継者たち |
| <code>xhtml/p-008.xhtml</code> | 71 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 324 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 344 | <code>'\u3000\u3000'</code> | 2 | <code>mfont font-1em10</code> | ３．勝者のない戦場 |
| <code>xhtml/p-008.xhtml</code> | 463 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 694 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |
| <code>xhtml/p-008.xhtml</code> | 739 | <code>'\u3000\u3000\u3000\u3000'</code> | 4 | <code></code> |  |


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
| em-sesame | span | 6 |
| font-0em90 | span | 1 |
| font-1em10 | p | 11 |
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
| main | div | 24 |
| mfont | div | 1 |
| mfont | p | 12 |
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
| tcy | span | 76 |
| vrtl | html | 9 |
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
| <code>xhtml/p-fmatter-005.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-fmatter-005.xhtml</code> | <code>../image/kuchie-005.jpg</code> | <code>image/kuchie-005.jpg</code> | OK |
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
| <code>xhtml/p-003.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-003.xhtml</code> | <code>../image/p018-019.jpg</code> | <code>image/p018-019.jpg</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-004.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-005.xhtml</code> | <code>../image/p106-107.jpg</code> | <code>image/p106-107.jpg</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-006.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-007.xhtml</code> | <code>../image/p190-191.jpg</code> | <code>image/p190-191.jpg</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid15190-m-v.png</code> | <code>image/gaiji-cid15190-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-008.xhtml</code> | <code>../image/gaiji-cid776-m-v.png</code> | <code>image/gaiji-cid776-m-v.png</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-009.xhtml</code> | <code>../image/p262-263.jpg</code> | <code>image/p262-263.jpg</code> | OK |
| <code>xhtml/p-010.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-011.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-credit.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-colophon.xhtml</code> | <code>../style/book-style.css</code> | <code>style/book-style.css</code> | OK |
| <code>xhtml/p-colophon.xhtml</code> | <code>../image/logo-sneaker.png</code> | <code>image/logo-sneaker.png</code> | OK |
| <code>xhtml/p-bookwalker.xhtml</code> | <code>../style/fixed-layout-jp.css</code> | <code>style/fixed-layout-jp.css</code> | OK |
| <code>xhtml/p-bookwalker.xhtml</code> | <code>../image/bookwalker.png</code> | <code>image/bookwalker.png</code> | OK |
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
| 1 | <code>[[EPUB_IMAGE:v1:xhtml/p-cover.xhtml:cover.jpg:occ-01]]</code> | [<code>raw/1/item/image/cover.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/cover.jpg) | [<code>raw/1/item/xhtml/p-cover.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-cover.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/cover.jpg"}</code> |
| 2 | <code>[[EPUB_IMAGE:v1:xhtml/p-fmatter-001.xhtml:kuchie-001.jpg:occ-01]]</code> | [<code>raw/1/item/image/kuchie-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/kuchie-001.jpg) | [<code>raw/1/item/xhtml/p-fmatter-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-fmatter-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/kuchie-001.jpg"}</code> |
| 3 | <code>[[EPUB_IMAGE:v1:xhtml/p-fmatter-002.xhtml:kuchie-002.jpg:occ-01]]</code> | [<code>raw/1/item/image/kuchie-002.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/kuchie-002.jpg) | [<code>raw/1/item/xhtml/p-fmatter-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-fmatter-002.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2258", "height": "1600", "href": "../image/kuchie-002.jpg"}</code> |
| 4 | <code>[[EPUB_IMAGE:v1:xhtml/p-fmatter-003.xhtml:kuchie-003.jpg:occ-01]]</code> | [<code>raw/1/item/image/kuchie-003.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/kuchie-003.jpg) | [<code>raw/1/item/xhtml/p-fmatter-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-fmatter-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2230", "height": "1600", "href": "../image/kuchie-003.jpg"}</code> |
| 5 | <code>[[EPUB_IMAGE:v1:xhtml/p-fmatter-004.xhtml:kuchie-004.jpg:occ-01]]</code> | [<code>raw/1/item/image/kuchie-004.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/kuchie-004.jpg) | [<code>raw/1/item/xhtml/p-fmatter-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-fmatter-004.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2219", "height": "1600", "href": "../image/kuchie-004.jpg"}</code> |
| 6 | <code>[[EPUB_IMAGE:v1:xhtml/p-fmatter-005.xhtml:kuchie-005.jpg:occ-01]]</code> | [<code>raw/1/item/image/kuchie-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/kuchie-005.jpg) | [<code>raw/1/item/xhtml/p-fmatter-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-fmatter-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "1127", "height": "1600", "href": "../image/kuchie-005.jpg"}</code> |
| 7 | <code>[[EPUB_IMAGE:v1:xhtml/p-titlepage.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/1/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/logo-sneaker.png) | [<code>raw/1/item/xhtml/p-titlepage.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-titlepage.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 8 | <code>[[EPUB_IMAGE:v1:xhtml/p-toc-001.xhtml:toc-001.jpg:occ-01]]</code> | [<code>raw/1/item/image/toc-001.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/toc-001.jpg) | [<code>raw/1/item/xhtml/p-toc-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-toc-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/toc-001.jpg"}</code> |
| 9 | <code>[[EPUB_IMAGE:v1:xhtml/p-001.xhtml:p004-005.jpg:occ-01]]</code> | [<code>raw/1/item/image/p004-005.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/p004-005.jpg) | [<code>raw/1/item/xhtml/p-001.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-001.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p004-005.jpg"}</code> |
| 10 | <code>[[EPUB_IMAGE:v1:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-002.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-002.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 11 | <code>[[EPUB_IMAGE:v1:xhtml/p-003.xhtml:p018-019.jpg:occ-01]]</code> | [<code>raw/1/item/image/p018-019.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/p018-019.jpg) | [<code>raw/1/item/xhtml/p-003.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-003.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p018-019.jpg"}</code> |
| 12 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 13 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 14 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 15 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 16 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 17 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 18 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 19 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-08]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 20 | <code>[[EPUB_IMAGE:v1:xhtml/p-004.xhtml:gaiji-cid776-m-v.png:occ-09]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-004.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-004.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 21 | <code>[[EPUB_IMAGE:v1:xhtml/p-005.xhtml:p106-107.jpg:occ-01]]</code> | [<code>raw/1/item/image/p106-107.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/p106-107.jpg) | [<code>raw/1/item/xhtml/p-005.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-005.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p106-107.jpg"}</code> |
| 22 | <code>[[EPUB_IMAGE:v1:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 23 | <code>[[EPUB_IMAGE:v1:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-02]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 24 | <code>[[EPUB_IMAGE:v1:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 25 | <code>[[EPUB_IMAGE:v1:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 26 | <code>[[EPUB_IMAGE:v1:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 27 | <code>[[EPUB_IMAGE:v1:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 28 | <code>[[EPUB_IMAGE:v1:xhtml/p-006.xhtml:gaiji-cid776-m-v.png:occ-07]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-006.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-006.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 29 | <code>[[EPUB_IMAGE:v1:xhtml/p-007.xhtml:p190-191.jpg:occ-01]]</code> | [<code>raw/1/item/image/p190-191.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/p190-191.jpg) | [<code>raw/1/item/xhtml/p-007.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-007.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p190-191.jpg"}</code> |
| 30 | <code>[[EPUB_IMAGE:v1:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-01]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 31 | <code>[[EPUB_IMAGE:v1:xhtml/p-008.xhtml:gaiji-cid15190-m-v.png:occ-02]]</code> | [<code>raw/1/item/image/gaiji-cid15190-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid15190-m-v.png) | [<code>raw/1/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | ではないのだろうということだけは理解できた。そして、ここでこのまま会話を続けていたら、その感情はすぐに抑えきれなくなって [IMAGE] るだろうということも。 | <code>{"class": "gaiji", "src": "../image/gaiji-cid15190-m-v.png", "alt": ""}</code> |
| 32 | <code>[[EPUB_IMAGE:v1:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-03]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 33 | <code>[[EPUB_IMAGE:v1:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-04]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 34 | <code>[[EPUB_IMAGE:v1:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-05]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 35 | <code>[[EPUB_IMAGE:v1:xhtml/p-008.xhtml:gaiji-cid776-m-v.png:occ-06]]</code> | [<code>raw/1/item/image/gaiji-cid776-m-v.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/gaiji-cid776-m-v.png) | [<code>raw/1/item/xhtml/p-008.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-008.xhtml) | gaiji (класс XHTML; глиф не проверен) | [IMAGE] | <code>{"class": "gaiji", "src": "../image/gaiji-cid776-m-v.png", "alt": ""}</code> |
| 36 | <code>[[EPUB_IMAGE:v1:xhtml/p-009.xhtml:p262-263.jpg:occ-01]]</code> | [<code>raw/1/item/image/p262-263.jpg</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/p262-263.jpg) | [<code>raw/1/item/xhtml/p-009.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-009.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "2223", "height": "1600", "href": "../image/p262-263.jpg"}</code> |
| 37 | <code>[[EPUB_IMAGE:v1:xhtml/p-colophon.xhtml:logo-sneaker.png:occ-01]]</code> | [<code>raw/1/item/image/logo-sneaker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/logo-sneaker.png) | [<code>raw/1/item/xhtml/p-colophon.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-colophon.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"src": "../image/logo-sneaker.png", "alt": ""}</code> |
| 38 | <code>[[EPUB_IMAGE:v1:xhtml/p-bookwalker.xhtml:bookwalker.png:occ-01]]</code> | [<code>raw/1/item/image/bookwalker.png</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/image/bookwalker.png) | [<code>raw/1/item/xhtml/p-bookwalker.xhtml</code>](https://github.com/PikaWarrior/SukaMoka/blob/main/raw/1/item/xhtml/p-bookwalker.xhtml) | изображение, визуально не проверено | [IMAGE] | <code>{"width": "840", "height": "1200", "href": "../image/bookwalker.png"}</code> |

## XHTML из manifest вне spine

Других XHTML, кроме navigation-документа, вне spine не найдено.

## XHTML spine, не повторённый в основном потоке

### `xhtml/p-toc-002.xhtml`

Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.

~~~text
　ｃｏｎｔｅｎｔｓ

[empty paragraph]

[empty paragraph]

[『背中を追いかけて』 - next to you -](p-001.xhtml#toc-001)

[『終わりを待つ街』 - metalcraft miniature garden -](p-003.xhtml#toc-002)

[『壊れかけた天秤の右と左』 - expensive bullet -](p-005.xhtml#toc-003)

[『憧れた背中、追いかけて追いかけて』 - her blind alley -](p-007.xhtml#toc-004)

[『忙しくもないこの日々に』 - offstage of tragedy -](p-009.xhtml#toc-005)

[empty paragraph]

　[あとがきという名のあとがき／すなわちあとがき](p-011.xhtml#toc-006)
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
