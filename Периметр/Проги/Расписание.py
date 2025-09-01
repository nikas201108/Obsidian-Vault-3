import plotly.figure_factory as ff
import pandas as pd
from random import shuffle
types = ["I", "II", "II", "I", "II", "I", "III"]
shuffle(types)

df = pd.DataFrame()
df["День"] = ["Воскресенье",  "Понедельник","Вторник", "Среда", "Четверг", "Пятница", "Суббота", ]
df["Тип"] = types

fig = ff.create_table(df)
fig.update_layout(
    autosize=False,
    width=1024,
    height=720,
       font=dict(
        family="Courier New, bold",
        size=18,
        color="RebeccaPurple"
    )
)
print("ok")
fig.show()
