#Python

>[!task] 
>Нам даны RGB-компоненты различных цветов и их соответствующие названия (классы). Нужно обучить алгоритм k-ближайших соседей на этих данных, чтобы он мог классифицировать новые, неизвестные цвета по их RGB-компонентам.
>
>Например, данные могут выглядеть так:
>
>
>
>```
>| RGB           | Цвет    |
>| ------------- | ------- |
>| (255, 0, 0)   | Красный |
>| (0, 255, 0)   | Зеленый |
>| (0, 0, 255)   | Синий   |
>| (255, 255, 0) | Желтый  |
>| ...           | ...     |
>```
>
>Задача: по RGB-компонентам неизвестного цвета определить его название.
>

-----------
## Решения
##### Решение
Для решение данной задаче лучше всего использовать алгоритм $k$-ближайших соседей. Характеристики, на которые мы должны опираться, уже даны нам из условия. Было принято решение, что лучше всего в рамках задачи использовать обычную теорему Пифагора, так как углы могли выдавать некорректные результаты (127, 127, 127 лежит на одном углу с 254, 254, 254, а серый не очень похож на белый).

```python
colors = dict()  
colors["white"] = (255, 255, 255)  
colors["yellow"] = (255, 255, 0)  
colors["lime"] = (0, 255, 0)  
colors["olive"] = (128, 128, 0)  
colors["green"] = (0, 128, 0)  
colors["teal"] = (0, 128, 128)  
colors["navy"] = (0, 0, 128)  
colors["blue"] = (0, 0, 255)  
colors["aqua"] = (0, 255, 255)  
colors["fuchsia"] = (255,0, 255)  
colors["purple"] = (128, 0, 128)  
colors["red"] = (255, 0, 0)  
colors["maroon"] = (128, 0, 0)  
colors["black"] = (0, 0, 0)  
colors["gray"] = (128, 128, 128)  
colors["silver"] = (192, 192, 192)  
colors["orange"] = (255, 165, 0)  
colors["pink"] = (255, 192, 203)  
  
color = list(map(int, input().split(",")))  
inf = float("infinity")  
nearest_colors = [("None", inf), ("None", inf), ("None", inf)]  
for key, value in colors.items():  
    length = round(sum([(color[i] - value[i]) ** 2 for i in range(3)]) ** 0.5, 3)  
    if any([length < x[1] for x in nearest_colors]):  
        nearest_colors[[length < x[1] for x in nearest_colors].index(True)] = (key, length)  
  
if round(((nearest_colors[0][1] + nearest_colors[1][1] + nearest_colors[2][1]) / (nearest_colors[1][1] + nearest_colors[2][1]) / 2), 3) < 0.45:  
    print("It is {} with {}".format(nearest_colors[0][0], nearest_colors[0][1]))  
else:  
    print("It is {}-{}-{} with {}, {} and {}".format(nearest_colors[0][0], nearest_colors[1][0], nearest_colors[2][0], nearest_colors[0][1], nearest_colors[1][1], nearest_colors[2][1]))
```

--------
## Комментарий 
Очень прикольный алгоритм, который можно принимать для решения очень интересных задач

***Made by Neural***