В [[Python]] — это функция, которая возвращает True, если все элементы в итерируемом объекте истинны, и False если все ложны.
```python
print(all([False, False, False])) # False
print(all([True, False, False])) # False
print(all([True, True, True])) # True
```
Отличается от [[Логическая операция and|логической операции and]] тем, что all() возвращает всегда True или False, а and:
	1)Ложно — первое ложное
	2)Истинное — последнее истинное
```python
print(8 and 3 and "Andrey") # Andrey  
print(3 and "" and "Hello" and 0) # ""
```
