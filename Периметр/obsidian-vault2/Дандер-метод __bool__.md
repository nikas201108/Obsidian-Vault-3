\__bool\__ — это [[Магические методы(Dunder-методы)|дандер-метод]], который определяет истину и ложь для объекта.
```python
class Vector:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
  
    def __str__(self):  
        return 'Vector(%r, %r)' % (self.x, self.y)  
  
    def __bool__(self):  
        if  abs(self.x) != 0 and abs(self.y) != 0:  
            return True  
        else:  
            return False  
  
  
a = Vector(3, 5)  
print(bool(a)) # True
print(bool(Vector(0, 0))) # False
```