#Python

>[!task]
>## Snail Sort
>
>Given an `n x n` array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
>
>```
>array = [[1,2,3],
  >       [4,5,6],
    >     [7,8,9]]
>snail(array) #=> [1,2,3,6,9,8,7,4,5]
>```
>
>For better understanding, please follow the numbers of the next array consecutively:
>
>```
>array = [[1,2,3],
  >       [8,9,4],
    >     [7,6,5]]
>snail(array) #=> [1,2,3,4,5,6,7,8,9]
>```
>
>This image will illustrate things more clearly: 

-----------
## Решения
##### Решение 1. Моё

```python
def snail(snail_map):  
  
    if len(snail_map) == 1:  
        return snail_map[0]  
    elif not snail_map:  
        return [[]]  
  
    right_to_left_diagonal = []  
    left_to_right_diagonal = []  
    right_to_left_diagonal.append(snail_map[0].pop(0))  
    left_to_right_diagonal.append(snail_map[len(snail_map) - 1].pop(len(snail_map) - 1))  
  
    for i in range(1, len(snail_map)):  
        right_to_left_diagonal.append(snail_map[0].pop(0))  
        left_to_right_diagonal.append(snail_map[i].pop(0))  
    for x in snail_map.pop(len(snail_map) - 1):  
        left_to_right_diagonal.append(x)  
    snail_map.pop(0)  
    for i in range(len(snail_map)):  
        right_to_left_diagonal.append(snail_map[i].pop(-1))  
    left_to_right_diagonal = [left_to_right_diagonal[0]] + left_to_right_diagonal[1:][::-1]  
    return [x for x in right_to_left_diagonal + left_to_right_diagonal + snail(snail_map) if x]
```

Это решение основывается на том, что мы идём по внешнему контуру. Когда он кончается, то мы входим в рекурсию, пока не придём к одному элементу. Стоит отметить, что здесь взятие с внешнего контура реализовано с помощю диагоналей (если элемент в `i, j`, то второй будет `j, i`)

##### Решение 2. С помощью zip

```python
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out
```

Основная суть этого решения заключается в том, что функция `zip` позволяет получить из строк матрицы столбцы и наоборот.

--------
## Комментарий 
Основные два момента, которые надо вынести из этой задачи:
- работа функции `zip` в матрицах
- диагонали как средство получения внешнего контура

***Codewars, [URL](https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/solutions/python)***
