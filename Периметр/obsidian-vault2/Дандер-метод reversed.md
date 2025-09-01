Это [[Магические методы(Dunder-методы)|дандер метод]], который возращает итерируемый объект в обратном порядке.

```python
class Test:  
    def __init__(self, ls):  
        self.ls = ls  
  
    def __reversed__(self):  
        return list(reversed(self.ls))  
  
a = Test([45, 34, 56])  
print(reversed(a))
```