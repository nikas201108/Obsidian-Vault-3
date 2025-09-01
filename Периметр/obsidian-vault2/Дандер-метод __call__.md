---
language:0 "python"
tags:0 "magic_methods", "python", "programming", "python_libraries"
---
### [[Python]]
В Python дандер-метод "call" нужен, чтобы можно было так обратиться к классу A().
```python
class A:
	def __call__(self, some):
		print(some)

a = A()
a('someValue') #Вывод 'someValue'
```