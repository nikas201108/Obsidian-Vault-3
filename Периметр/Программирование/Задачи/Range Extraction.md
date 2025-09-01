#Python

>[!task] 
>A format for expressing an ordered list of integers is to use a comma separated list of either
>
>- individual integers
>- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
>
>Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
>
>**Example:**
>
>```python
>solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
># returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
>```

-----------
## Решения
##### Решение 
Я решал, грубо говоря, через каретку или что-то типа того
```python
def solution(args):
    i_start = 0
    i_end = 1
    result = []
    for x in range(len(args) - 1):
        if args[x] + 1 != args[x+1]:
            result.append(list(map(str, args[i_start:i_end])))
            i_start = x + 1
            i_end += 1
        else:
            i_end += 1
    result.append(list(map(str, args[i_start:i_end])))
    return ",".join(["{}-{}".format(el[0], el[-1]) if len(el) > 2 else ",".join(el) for el in result])
```
--------
## Комментарий 
Задача прикольная, мне понравилась.
***Codewars, [URL](https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python)***