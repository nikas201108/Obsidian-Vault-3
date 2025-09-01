import os
import random

ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\obsidian-vault2")

for x in range(3): 
    print(random.choice(ls))


print("=====")
ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Dictionary")
for x in range(5): 
    print(random.choice(ls))
print("=====")
print("книги")
if random.randint(0, 1) == 1:
    ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Журнал чтения")  
else:
    ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Журнал чтения\Отчёты")  
print(random.choice(ls))
print("=====")
for x in range(5):
    print("математика")
    if random.randint(0, 1) == 1:
        ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Математика")  
    else:
        ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Математика\Задачи") 
    print(random.choice(ls))
print("=====")
print("Русский")
for x in range(2):
    ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\ЕГЭ русский")  
    print(random.choice(ls))

print("Информатика")
choice = random.randint(0, 2)
for x in range(2):
    if choice == 0:
        ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Программирование\Python")  
    elif choice == 1:
        ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Программирование")  
    else:
        ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\Программирование\Задачи")
    print(random.choice(ls))


print("=====")
choice = ".obsidian"
while choice in [".obsidian", "Шаблоны", "Медиа", "Media"]:
    choice = random.choice(os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\{}".format(random.choice(os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2")))))
print(choice)
print("=====")
print("Комбайн")
choice = ".obsidian"
while choice in [".obsidian", "Шаблоны", "Медиа", "Media"]:
    choice = random.choice(os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\{}".format(random.choice(os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2")))))
print(choice)

while True:
    try:
        choice = ".obsidian"
        while choice in [".obsidian", "Шаблоны", "Медиа", "Media"]:
            choice = random.choice(os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\{}".format(random.choice(os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2")))))
        print(choice)
    except:
        pass
    input()
