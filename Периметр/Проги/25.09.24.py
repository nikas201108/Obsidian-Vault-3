
import random

words = """
аэропОрты
граждАнство
дефИс
дОнизу
дОсуха
зАгнутый
зАсветло
знАчимый
красИвее
ловкА
мЕстностей
мозаИчный
мусоропровОд
наделИт
надОлго
нАчали
недУг
новостЕй
обзвонИл
обострЕнный
озлОбить
облегчИт
поднЯв
придАное
призЫв
принялА
прИнятый
прозорлИва
сверлИшь
слИвовый
снятА
созЫв
тОртов
укрепИт
цепОчка
чЕрпать
шАрф
""".split("\n")
temp = []
for x in range(70): 
    print(x)
    ind = random.randint(1, len(words)-1)
    print(words[ind].lower())
    if (word := input()) == words[ind]:
        print("Ok")
    elif word == "0":
        temp[-1] = ""
    else:
        print("======")
        print("Fail")
        print(words[ind])
        temp.append(words[ind])
        print("======")

for x in temp:
    print(x)
