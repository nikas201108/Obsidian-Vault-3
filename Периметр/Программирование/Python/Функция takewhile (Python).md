`takewhile` из модуля `itertools` позволяет брать значения из словаря в потоке, пока выполняется определенное условие:

```python
import itertools  
  
mine = [1, 1, 1, 2, 3, 4, 1]  
  
print(list(itertools.takewhile(lambda x: x == 1, mine))) #[1, 1, 1]
```
