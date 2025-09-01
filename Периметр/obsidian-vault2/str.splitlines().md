str.splitlines() в [[Python]] — это функция, которая работает наподобие [[str.split()]], но делит строку по '\\n'.
Принимает булевое значение: True — в строке будут отображаться спецсимволы, False — нет.
```python
my_str = 'ab c\n\nde fg\rkl\r\n'  
my_str.splitlines() # ['ab c', '', 'de fg', 'kl']
```
```python
my_str.splitlines() # ['ab', 'cd']  
my_str.split('\n') # ['ab', 'cd', '']
```