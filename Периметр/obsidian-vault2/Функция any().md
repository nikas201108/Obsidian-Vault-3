В [[Python]] — это функция, которая принимает итерируемый объект и если находит в нем хотя бы одно значение True, то возращает True. Иначе — False.
```python
print(any([False, False, False])) # False
print(any([True, False, False])) # True
```
Отличается от [[Логическая операция or|логической операции or]] тем, что во-первых, принимает итерируемое значение, а во-вторых, выводит не последний False элемент, а просто False
```python
print(any(['', '', ''])) # False  
print(False or False or '') # ''
```
