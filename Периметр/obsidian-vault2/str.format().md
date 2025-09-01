в [[Python]] str.format() заполняет заполнители в строке, представленные {}, переданными аргументами.
```python
print("Hello {}".format(input())) # Hello name
```
```python
print("{0} {1} {2}".format("Hello", "my", "Friend")) # Hello my friend
```
```python
place = {"city": "Samara", "street": "Poltavskay", "house": 11}  
print("He lived in {city}, {street}, {house}".format(**place))
```
Множество дополнительных аргументов смотреть в документацию.

Есть второй тип замены конструкция:  'Vector(%[здесь я должен поставить тип %i, %f, %s, %r], %r)' % (self.x, self.y)