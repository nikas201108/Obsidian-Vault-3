---
language:0 "python"
tags:0 "annotations", "python", "programming", "python_libraries"
---
typing — это встроенная в [[Python]] библиотека, котоая расширяет возможности [[Аннотации|аннотирования]].
#### Встроенные типы
1. [[Встроенный тип Optional(typing)|Optional]] — тип, который принимает либо None, либо указанный пользователем.
```python
from typing import Optional

a: Optional[int]
```
2. [[Встроенный тип Any(typing)|Any]]  — тип, который принимает все. Он используется, когда разработчик лично обрабатывает все типы или это не важно.
```python
from typing import Any

a: Any
```
3. [[Встроенный тип Union(typing)|Union]]  — тип, который принимает список строго определенных типов.
```python
from typing import Union

a: Union[int, str]
```
4. [[Встроенный тип List(typing)|List]] — тип, который конкретизирует класс [[list]]. Наподобие работаюют и [[set]], [[frozenset]]
```python
from typing import List

a: List[int]
```
5. [[Встроенный тип Tuple(typing)|Tuple]] — тип, который конкретизирует класс [[tuple]]. Синтаксис как у [[List]], но здесь указывается тип каждого отдельного элемента. Если точная длина кортежа неизвестно, то используем ...(тип Any).
```python
from typing import Tuple  
  
a: Tuple[int, ..., str]  
a = (1, 'f', 'ds') #correct  
a = ('1', 2, 'ds') #incorrect  
a = (1, 'a', 2) #incorrect  
a = (1, 'a', 'ds', 'df') #incorrect
```
6. [[Встроенный тип Dict(typing)|Dict]], [[Встроенный тип DefaultDict(typing)|DefaultDict]], [[[[Встроенный тип OrderedDict(typing)|OrderedDict]] — нужны для оформления словарей. Здесь отдельно указывается тип ключа и значения.
```python
from typing import Dict  
soviet_military_equipment: Dict[str, int]
soviet_military_equipment['bmp'] = 4 # correct
soviet_military_equipment['Mig'] = 'twenty nine' # incorrect
```
7. Чтобы аннотировать вызываемые типы, мы используем Callable, где список — типы аргументов(многоточие без скобочек, если типы функции не определены), значение — вывод функции.
```python
from typing import Callable  
  
  
def get_input() -> str:  
    return input()  
  
  
def print_something(a: str) -> None:  
    print(a)  
  
  
def aggregate(u_input: Callable[[], str], u_output: Callable[[str], None]) -> None:  
    a = u_input()  
    u_output(a)
```
### Дженерики
Иногда нам надо определить тип, не фиксирую его жестко. Как, например, в однотипных list. Для этого используются [[Встроенный тип TypeVar(typing)|TypeVar]], который сначала должен попасть в переменную, а потом непосредственно объявиться.
```python
import typing  
  
a = typing.TypeVar("a", int, str) #only int and str  
  
  
class Test(typing.Generic[a]):  
    data: a  
  
    def __init__(self, data: a):  
        self.data = data  
  
  
class_instance_1: Test[int] = Test(1) #ok  
class_instance_1.data += 1 #ok  
class_instance_1.data.replace('0', '1') #error  
  
class_instance_2: Test[str] = Test('1') #ok
```

[[Функция cast]] используется, чтобы вручную утвердить тип. Использовать крайне осторожно!
```python
from typing import cast, List
value = [130]
value_float = cast(List[float], value)
reveal_type(value_float) # Тип выведен как List[float]  
value_float == [130] # Но это выражение по-прежнему верно
```
Атрибуты объектов для доступа к аннотациям:
- object.`__annotations__`
- object.`get_type_hints`(как прошлое, но затрагивает и родительские объекты)