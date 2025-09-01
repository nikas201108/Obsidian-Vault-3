#Python

>[!task] 
>The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
>
>Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
>
>### Examples (input --> output):
>
>```
>255, 255, 255 --> "FFFFFF"
>255, 255, 300 --> "FFFFFF"
>0, 0, 0       --> "000000"
>148, 0, 211   --> "9400D3"
>```


-------------

## Решения 
Здесь можно выделить две основных интересных момента:
1) Здесь пристальное внимание стоит уделить функции format
2) Здесь рамки хитрым образом реализованы через минимум и максимум

```python
def rgb(r, g, b):  
    round = lambda x: min(255, max(x, 0))  
    return ("{:02X}" * 3).format(round(r), round(g), round(b))  
  
print(rgb(3, 4, 5))
```


---------
## Комментарий
Задача у меня самого не решилось, но реализация красивая)
Надо повторять format и взять на заметку трюк с границами через минимум и максимум

***Codewars, [URL](https://www.codewars.com/kata/513e08acc600c94f01000001)***
