---
language:0 "python"
tags:0 "magic_methods", "python", "programming", "python_libraries"
---
### [[Python]]
В Python assert используется для того, чтобы вызвать ошибку при поступлении False, и продолжить выполнение программы при True.
Это может использоваться:
- при отладке
- проверка значений функций, аргументов и т.п.
У функции assert такой синтаксис:
```python
assert <condition>, <message>:optional
```
Пример.
```python
assert a, "a не может быть False"  # Вывод: если а = True, то ничего не происходит; если a = False — ошибка.
```
Встроенная библиотека [[Библиотека unittest|unittest]] предлагает расширение функции assert.
