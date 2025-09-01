\__mul\__ — это [[Магические методы(Dunder-методы)|дандер-метод]], который обозначает умножение. При его использовании создается новый объект.

```python
class Vector:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
  
    def __str__(self):  
        return 'Vector(%r, %r)' % (self.x, self.y)  
  
    def __mul__(self, scalar):  
        return Vector(self.x * scalar, self.y * scalar)  
  
a = Vector(3, 5)  
print(a * 3) # Vector(9, 15)
```