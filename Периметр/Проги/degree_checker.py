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
    
r = random.randint(0, 1)
if r == 0:        
    for x in range(30):
        random.choice([squton(), ntosqu()])
else:
    for x in range(11, 13):
        for y in range(10, 20):
            print(f"{x}x{y}=?")
            try:
                if int(input()) != x*y:
                    print("Нет!", x*y)
            except:
                pass
    for x in range(10):
        a, b = random.randint(11, 19), random.randint(11, 19)
        print(f"{a}x{b}")
        try:
            if int(input()) != a*b:
                print("Нет!", a*b)
        except:
            pass

            

print("Произвольный квадрат:", random.choice([x**2 for x in range(90, 10000)]))
print("Произвольный куб:", random.choice([x**3 for x in range(11, 99)]))
