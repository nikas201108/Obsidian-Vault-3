Библиотека rich языка [[Python]] — это инструмент для разметки в консоли.

Чтобы получить полный контроль мы должны использовать класс [[Класс Console|Console]]. 
Чтобы выводить текст используем функцию [[Функция Console.print|Console.print]]. Чтобы задать стиль есть два способа:
```python
Console.print([/bold red]hello world![/bold red])
```
```python
style = "bold red"
Console.print(hello world, style=style)
```
