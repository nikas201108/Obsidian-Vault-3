Чтобы [[LaTex]] сам сгенерировал [[Титульный лист|титульный лист]] надо передать ему несколько аргументов в преамбуле:
-  [[author{name}|\author{name}]]
- [[title{name}|\title{name}]]
- [[date{text}\date{text}]]
Потом надо написать команду [[maketitle|\maketitle]] в самом тексте.
```latex
\documentclass[a4paper, 12pt]{article}
\author{Андрей вершинский}
\title{Создание межгалакстической установки}
\date{12 июня 1941 г.}

\begin{document}
    \maketitle
\end{document}
```
