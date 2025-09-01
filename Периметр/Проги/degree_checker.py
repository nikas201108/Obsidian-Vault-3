import random

def squton():
    number = random.randint(17, 50)
    print(number**2)
    try:
        if int(input()) == number:
            print("Ok")
        else:
            print("Fail")
    except:
        pass

def ntosqu():
    number = random.randint(17, 50)
    print(number)
    try:
        if int(input()) == number**2:
            print("Ok")
        else:
            print("Fail")
            print(number**2)
    except:
        pass

for x in range(30):
    random.choice([squton(), ntosqu()])

print("Произвольный квадрат:", random.choice([x**2 for x in range(90, 10000)]))
print("Произвольный куб:", random.choice([x**3 for x in range(11, 99)]))
