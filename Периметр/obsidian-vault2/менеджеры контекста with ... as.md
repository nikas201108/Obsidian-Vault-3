### [[Python]]
В Python конструкция with ... as является очень удобным инструментом. Её суть заключается в том, что до и после выполнения блока with .. as будут автоматически вызваны заранее прописанные действия(а в случае после, даже если в блоке случится ошибка, то python все равно исполнит его). За действия входа и выхода ответственны магические методы в классе: [[Дандер-метод __enter__|дандер-метод __enter__]] и [[Дандер-метод __exit__|дандер-метод __exit__]] 
```python
with <class> as <name>:...
```

Пример:
```python
class TextDivider:  
    def __init__(self, string):  
        self.string = string  
  
    def __enter__(self):  
        print("Okay, let's start")  
        self.total = []  
        return self  
  
    def __exit__(self, exc_type, exc_val, exc_tb):  
        print(self.total)  
        print(exc_type)  
        print(exc_val)  
        print(exc_tb)  
  
    def divide_text(self):  
        self.total = self.string.split()  
```
Случай 1:
```python
with TextDivider('Hello my friend') as td:  
    td.divide_text()
```
Вывод: 
```python
>>>Okay, let's start
>>>['Hello', 'my', 'friend']
>>>None
>>>None
>>>None
```
Случай 2:
```python
with TextDivider(123) as td:  
    td.divide_text()
```
Вывод:
```python
>>>Okay, let's start
>>>[]
>>><class 'AttributeError'>
>>>'int' object has no attribute 'split'
>>><traceback object at 0x000001DBA7B76A40>
>>>Traceback (most recent call last):
  File "D:\Sets\with_test.py", line 21, in <module>
    td.divide_text()
  File "D:\Sets\with_test.py", line 17, in divide_text
    self.total = self.string.split()
AttributeError: 'int' object has no attribute 'split'
```