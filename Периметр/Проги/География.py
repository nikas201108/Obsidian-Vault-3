import random

tree = {"Россия": [("Административное деление", "https://maptomind.ru/test/nP5iIDA"),
                     ("Острова и другое", "https://maptomind.ru/test/8Y9mMmi"),
                     ("Горы", "https://maptomind.ru/test/yYFZV2H"),
                     ("Равнины", "https://maptomind.ru/test/nZH3ZqW"),
                     ("Моря, заливы, проливы", "https://maptomind.ru/test/OgclJVU"),
                     ("Реки, озера, каналы", "https://maptomind.ru/test/b6HmwYk"),
                     ("Республики", "https://maptomind.ru/test/x6Cf1Pq"),
                     ("Реки и адм. центры", "https://maptomind.ru/test/7p7kbvB")],
        "Европа": [("Моря, заливы, проливы", "https://maptomind.ru/test/F9cuQjQ"),
                   ("Острова и другое", "https://maptomind.ru/test/9dDSZ2v"),
                    ("Ландшафт", "https://maptomind.ru/test/6j4baMC"),
                    ("Реки, озера", "https://maptomind.ru/test/JL9YdsV")],
        "Азия": [("Моря, заливы, проливы", "https://maptomind.ru/test/Lgfi6j5"),
                 ("Реки, озера", "https://maptomind.ru/test/4WAgjFr"),
                 ("Ландшафт", "https://maptomind.ru/test/es3u7Oz"),
                 ("Страны, столицы", "https://maptomind.ru/test/ZnxwoU5"),
                ("Острова", "https://maptomind.ru/test/K4OhpFR")],      
            }

region = random.choice(list(tree.keys()))
print("Регион:", region)
topic = random.randint(0, len(tree[region])-1)
print("Тема:", tree[region][topic][0])
print("Ссылка:", tree[region][topic][1]) 


