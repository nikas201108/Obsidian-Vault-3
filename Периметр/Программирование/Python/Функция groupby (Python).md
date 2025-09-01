Функция позволяет группировать значения по ключам (предварительно использовать сортировку, так как он группирует только подряд идущие)

```python
import itertools  
  
strings = sorted(['apple', 'banana', 'apricot', 'orange', 'avocado'])  
  
for key, group in itertools.groupby(strings, key=lambda x: x[0]):  
    print(key, list(group))

"""
a ['apple', 'apricot', 'avocado']
b ['banana']
o ['orange']
"""
```