# quiz.py

import random
import re
from vocabulary import common_words, special_words

def generate_forms(base_word):
    """Генерирует возможные формы слова для замены."""
    base = base_word.lower()
    forms = {
        base,
        base + 's',
        base + 'ed',
        base + 'ing',
    }
    return forms

def hide_word_in_example(example, base_words):
    """Заменяет все формы слов из base_words в примере на '_____'."""
    all_forms = set()
    for word in base_words:
        all_forms.update(generate_forms(word.lower()))
    
    sorted_forms = sorted(all_forms, key=len, reverse=True)
    text = example
    for form in sorted_forms:
        pattern = r'\b' + re.escape(form) + r'\b'
        text = re.sub(pattern, '_____', text, flags=re.IGNORECASE)
    return text

def quiz():
    # Подготавливаем общие слова (без метки)
    common_items = [(defn, data, False) for defn, data in common_words.items()]
    random.shuffle(common_items)
    selected_common = common_items[:60]

    # Подготавливаем специальные слова (с меткой True)
    special_items = [(defn, data, True) for defn, data in special_words.items()]
    random.shuffle(special_items)
    selected_special = special_items[:20]

    # Объединяем: сначала общие, потом специальные
    all_items = selected_common + selected_special

    correct = 0
    total = len(all_items)

    for definition, data, is_special in all_items:
        prefix = "[СПЕЦ] " if is_special else ""
        print(f"Определение: {prefix}{definition}")
        print("Пример(ы):")
        for ex in data["examples"]:
            hidden_ex = hide_word_in_example(ex, data["translations"])
            print(f"  - {hidden_ex}")

        user_answer = input("Ваш ответ: ").strip().lower()
        correct_answers = [ans.lower() for ans in data["translations"]]

        if user_answer in correct_answers:
            print("✅ Верно!")
            print(", ".join(correct_answers), "\n")
            correct += 1
        else:
            print(f"❌ Неверно. Правильный ответ: {', '.join(data['translations'])}\n")

    print(f"Тест завершён! Ваш результат: {correct} из {total}")
    if total > 0:
        percentage = (correct / total) * 100
        print(f"Процент правильных ответов: {percentage:.1f}%")

if __name__ == "__main__":
    quiz()
