import random
from rich.console import Console
from words import word_groups
import os

console = Console()

def quiz_user(group):
    words = list(group.keys())
    selected_words = random.sample(words, min(7, len(words)))
    
    score = 0
    for word in selected_words:
        user_translation = input(f"{word}\n").strip().lower()
        correct_translations = [translation.lower() for translation in group[word]["translations"]]
        l = 1
        if user_translation in correct_translations:
            console.print("Правильно!", style="bold green")
            score += 1
            if "examples" in group[word]:
                for example in group[word]["examples"]:
                    console.print(f"{l}. {example}", style="bold cyan")
                    l += 1
            elif "example" in group[word]:
                print(f"{group[word]['example']}")
        else:
            console.print(f"Неправильно! {', '.join(correct_translations)}", style="bold red")
            if "examples" in group[word]:
                for example in group[word]["examples"]:
                    console.print(f"{l}. {example}", style="bold cyan")
                    l += 1
            elif "example" in group[word]:
                print(f"{group[word]['example']}")
        print()
    print(f"Вы набрали {score} из {len(selected_words)} в этой группе.\n")

def select_random_group(groups):
    return random.choice(list(word_groups.keys()))
    
def main():
    groups = list(word_groups.keys())
    num_cycles = 10
    
    for cycle in range(num_cycles):
        print("=============================")
        print(f"\nЦикл {cycle + 1}/{num_cycles}:")
        
        # Выбираем случайную группу
        selected_group = select_random_group(groups)
        print(f"Группа: {selected_group}\n")
        
        # Запускаем тестирование для выбранной группы
        quiz_user(word_groups[selected_group])
        print("=============================")
    print("Тестирование завершено!")

main()

print("\n\n\n\n\n\n=================================================")
category = random.choice(list(word_groups.keys()))
words = [random.choice([list(x.values())[0] for x in word_groups[category].values()]) for x in range(8)] if len(word_groups[category]) >= 2 else [list(x.values())[0] for x in word_groups[category].values()]
words = [item for sublist in words for item in sublist]
message = f"""Создай тест из 10 предложений с пропусками для проверки знания английского языка. Каждое предложение должно содержать один пропуск, который нужно заполнить одним словом. Включите разные части речи (существительные, глаголы, прилагательные, наречия и т.д.) и различные времена глаголов. Также добавьте ответы в конце теста. Слова: {', '.join(words)}"""
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


maximums = (23, 17)
choice = random.randint(1, 3)
if choice == 1:
    print("Synonyms: ", random.randint(1, maximums[0]))
elif choice == 2:
    print("Usage")
else:
    print("FNIf: ", random.randint(1, maximums[1]))
    
while True:
    ls = os.listdir(r"C:\Users\user\OneDrive\main-obsidian-vault-2\EnglishVault\Правила")
    name = random.choice(ls)
    print(name)
    if input() == "0":
        break
input()
print("=================================================\n\n\n\n\n\n")


input()
