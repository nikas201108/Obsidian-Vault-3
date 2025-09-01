import random

prwca = ["…десь", "…дание", "…доровье", "ни …ги", "и…подлобья", "ра…чёт", "и…чезнуть",
        "и…ябнуть", "ра…читать", "не…дешний", "…даться", "чере…полосье", "чере…чур",
        "и…коверканный", "чре…мерный", "бе…чувственный"]

prwc = ["здесь", "здание", "здоровье", "ни зги", "исподлобья", "расчёт", "исчезнуть",
        "иззябнуть", "рассчитать", "нездешний", "сдаться", "чересполосье", "чересчур",
        "исковерканный", "чрезмерный", "бесчувственный"]

words = {prwc[i]: prwca[i] for i in range(len(prwc))}

errors = []

for x in range(50):
    choose = 0
    if 0 == 0:
        choose = random.choice(list(words.keys()))
        print(words[choose])
        if choose == input():
            print("Молодец")
        else:
            print("Неправильно!\n" + choose)
        print("="*60)
        errors.append(choose)
errors = list(set(errors))
for x in errors:
    print(x)
