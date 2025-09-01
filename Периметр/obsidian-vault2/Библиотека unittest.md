unittest — это встроенная библиотека [[Python]], призванная автоматизировать и упростить откладку.

Концепции unittest:
1. Испытательный стенд(Test fixture) — подготовка для выполнения тестов
2. Тестовый случай(Test case) — проверяет ответы для разных наборов данных. [[Класс TestCase]]. 
3. Набор тестов(Test suite) — совокупность или объединения тестовых случаев.
4. Исполнитель тестов(test runner)  — выполняет тесты возращает результат 

Пример:
```python
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
```

В данном коде мы создаем тестовый случай с помощью наследования от класса [[Класс TestCase|unittest.TestCase]]. Испольнитель понимает, где находятся тесты с помощью первой приписки test_.  Вместо [[Функция assert|функции assert]], здесь используются её встроенный в модуль модификации, чтобы исполнитель мог составить отчёт. Здесь так же можно оставлять сообщения.

| Метод | Значение | 
| ---------- | --------- | 
| [[assertEqual(a, b)]] | `a == b` | 
| [[assertNotEqual(a, b)]] | `a != b` |
| [[assertTrue(x)]] | `bool(x) is true` |
| [[assertFalse(x)]] | `bool(x) is false` |
| [[assertIs(a, b) ]]| `a is b` |
| [[assertIsNot(a, b)]] | `a is not b` |
| [[assertIsNone(x)]] | `x is None` |
| [[assertIsNotNone]] | `x is not None` |
| [[assertIn(a, b)]] | `a in b` |
| [[assertNotIn(a, b)]] | `a not in b` |
| [[assertIsInstance(a, b)]] | `isinstance(a, b)` |
| [[assertNotIsInstance(a, b)]] | `not isinstance(a, b)` |
| [[assertRaises(exc, func)]]| `func() пораждает исключение exc` |
| [[assertRaisesRegex(exc, r, func)]] | `func() пораждает исключение exc, которое подходит под регулярное выражение` |
| [[assertWarns(warn, func)]] | `func() пораждает предупреждение` |
| [[assertWarnsRegex(warn, r, fun]] | `func() пораждает предупреждение, которое подходит под регулярное выражение` |
| [[assertAlmostEqual(a, b)]] | `round(a-b, 7) == 0` |
| [[assertNotAlmostEqual(a, b)]]| `round(a-b, 7) != 0` |
| [[assertGreater(a, b)]] | `a > b` |
| [[assertGreaterEqual(a, b)]] | `a >= b` |
| [[assertLess(a, b)]] | `a < b` |
| [[assertLessEqual(a, b)]] | `a <= b` |
| [[assertRegex(s, r)]] | `r.search(s)` |
| [[assertNotRegex(s, r)]] | `not r.search(s)`|
| [[assertCountEqual(a, b)]] | `a и b содержат одинаковые элементы в том же количестве` |
*[[Функция isinstance]]
[[re.search()]]

-----------------
### Отчеты.
[[Функция unittest.main()]] — выводит отчёт в командную строку.
Но здесь надо отметить, что проводить тестирование можно прямиком из консоли. Для этого надо написать: 
`python -m unittest (путь до файла).класс{опционально}.метод(опционально) ...`
Флаги полезные флаги после unittest:
1. [[Флаг -v|-v]] — выводит более подробный отчет
2. [[Флаг -b|-b]] — вывод программы при провальном тесте будет показан
3. [[Флаг -c|-c]] — при нажатии ctrl+c ожидает завершение текущего теста, а потом выводит результаты уже пройденных тестов.
4. [[Флаг -f|-f]] — выход после первого неудачного теста
5. [[Флаг --locals|--locals]] — показывает локальные переменные провалившихся тестов.
-----------------
Стоит учитывать, что тестирующий код(в нашем случае функции на test_) должен быть самостоятельным.

С помощью мы можем добавлять к тестам декораторы: 
1. [[unittest.skip()]] — пропускает тест. Может быть передан параметр reason 
2. [[unittest.skipif()]] — пропускает тест, если условие истинно. Принимает условие и reason
3. [[unittest.skipUnless()]] — пропускает тест, если условие ложно. Принимает условие и reason
4. [[unittest.expectedFailure]]  — помечает тест как ожидаемая ошибка и возращает True, если он провальный.

Легко можно и создать свои декораторы:
```python
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
```
С помощью [[setUp()]] и [[tearDown()]] можно определить поведение перед каждым тестом(как в первом случае) или после каждого(как во втором)(например заносить все в какую-то базу, чтобы не повторять одинаковые строчки кода каждый раз).
```python
import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```

Тесту можно добавлять подтесты, если они очень похожи друг на другу. Ведь гораздо проще будет определить ошибку при работе с большими данными, зная в каких случаях происходила ошибка.
```python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
	    Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```