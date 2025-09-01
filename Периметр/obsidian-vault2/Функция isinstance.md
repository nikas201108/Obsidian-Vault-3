### [[Python]]
Функция isinstance(a, b) принимает аргумент a — экземпляр класса и b — класс, а на вывод выдает True или False. Это зависит от того, является ли a экземпляром класса b.
```python
class A:  
    ...  
  
class B:  
    ...  
  
c = A()  
print(isinstance(c, A))  # Вывод: True  
print(isinstance(c, B))  # Вывод: False
```