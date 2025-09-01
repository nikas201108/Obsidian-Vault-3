import random
import dictionary
import os

errors = []
dictionary = dictionary.dictionary
error_flag = False

while True:
    for x in range(0, 79):
        slice_start = random.randint(500, len(dictionary.values()) - 1)
        translation, words = random.choice(list(dictionary.items())[slice_start:])
        print(translation)
        if (answer := input()) in words:
            print("=====================")
            print("Молодец")
            if len(words) > 1:
                counter = 0
                for word in words:
                    counter += 1
                    print(str(counter) + ". " + word)
            print(79-x)
            print("=====================")
        elif answer == '0':
            print("=====================")
            print("очищено")
            errors[-1] = ''
            print("=====================")
        else:
            print("====================================")
            print("Неправильно, заново")
            errors.append((translation, words))
            if len(words) > 1:
                counter = 0
                for word in words:
                    counter += 1
                    print(str(counter) + ". " + word)
            else:
                print(words[0])
            print(79-x)
            print("====================================\n\n\n====================================")
    if error_flag == False:
        break
    else:
        error_flag = False


errors2 = []
for i in errors:
    if i not in errors2:
        errors2.append(i)
        
for x in errors2:
    print("------")
    for y in x:
        print(y)

input()       
for x in range(5):
    print(random.choice(list(dictionary)))

print("\n\n\n\n\n\n=================================================")
words = [random.choice(list(dictionary.items()))[1][0] for x in range(8)]
message = f"""Hello! Write please fill-gap exercises for all these words:
{words[0]},
{words[1]},
{words[2]},
{words[3]},
{words[4]},
{words[5]},
{words[6]},
{words[7]}.
Don't write other comments and answers, also I need only exercise
By the way you should mix that sentences, because It will be too boring if the word order in the task matches the order of the words to be inserted
"""
if random.randint(0, 1) == 0:
    print(message)
    for x in random.sample(words, 8):
        print(x, end=", ")
else:
    element = random.choice(os.listdir(r'C:\Users\user\OneDrive\main-obsidian-vault-2\EnglishVault\Правила'))
    print(f"Grammar: {element}")
print()
input()
print("=================================================\n\n\n\n\n\n")


while True:
    ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\EnglishVault\Правила")
    name = random.choice(ls)
    print(name)
    if input() == "0":
        break
input()
print("=================================================\n\n\n\n\n\n")

maximums = (23, 17)
choice = random.randint(1, 3)
if choice == 1:
    print("Synonyms: ", random.randint(1, maximums[0]))
elif choice == 2:
    print("Usage")
else:
    print("FNIf: ", random.randint(1, maximums[1]))
