# ***************************ЗАДАЧА 1********************************
# Запросите ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться
# конкатенация строк. В остальных случаях введенные числа суммируются.

try:
    value1 = input('Enter the first value ...')
    value2 = input('Enter the second value ..')
    print(int(value1) + int(value2))
except ValueError:
    print(value1 + value2)

# ***************************ЗАДАЧА 2********************************
# Возьмите ввод числа от пользователя.
# Если число отрицательное, вызвать исключение ValueError с сообщение,
# что число должно быть положительным.

value = int(input('Enter the first value ...'))
assert value >= 0, '< 0'
# if value < 0:
#     raise ValueError('< 0')

# ***************************ЗАДАЧА 3********************************
# Дано 2 списка:
# cities = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
# cities2 = ['Sumy', 'Kyiv', 'Odessa', 'Zhytomyr', 'Lviv', 'Chernihiv',
#  'Kharkiv', 'Ternopil\'', 'Mariupol\'']
# Создать словарь, в котором ключами будут города из списка cities,
# а значениями будет случайный год в промежутке от 1990 до 2021.
# Затем если в словаре нет города из списка cities2 вывести инормацию,
# что город не найдет, в ином случае вывести значение ключа города.
import random

cities = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
cities2 = ['Sumy', 'Kyiv', 'Odessa', 'Zhytomyr', 'Lviv', 'Chernihiv',
           'Kharkiv', 'Ternopil\'', 'Mariupol\'']

dictCities = {city: random.randint(1990, 2021) for city in cities}

print(dictCities)

for c in cities2:
    try:
        print(dictCities[c])
    except KeyError:
        print('{c} is not in Dictionary')

# ***************************ЗАДАЧА 4********************************
# Создать список из 20 случайных букв.
# Написать цикл while True, в котором будет поочередно выводится индекс элемента
# из списка и сам элемент.
# Когда элементы из списка закончатся, вывести сообщение Index out of range
# и завершить программу.
import string

List_1 = random.sample(string.ascii_lowercase, 20)
print(List_1)

i = 0
while True:
    try:
        print(f'Index: {i}, and element \'{List_1[i]}\'')
    except IndexError:
        print('Index out of range')
        break
    finally:
        i += 1

print('Exit')

# В файле ведущий загадал слово
# угадывают букву. Пользователь вводит букву.
# слово отображается в виде звездочек.
# если пользователь угодал то буква открывается.
# если ввел слово целиком то угадал или нет

print('Welcom in Field of Marical)')
with open('quiz.txt', 'r') as fine:
    wordGues = fine.read().strip()
    wordShow = list('*' * len(wordGues))

while True:
    print(f'The word \'' + ''.join(wordShow) + '\'.')
    userValue = str(input('Please enter a letter or your word ...'))
    if len(userValue) < 2:
        i = 0
        for d in wordGues:
            if d == userValue:
                wordShow[i] = wordGues[i]
            i += 1
    else:
        if userValue == wordGues:
            print(f'Word is \'{wordGues}\'.\nYou win!')
            break
        else:
            print(f'Word is \'{wordGues}\'.\nYou lose')
            break
    if len(wordGues) == wordShow.count('*') + len(wordShow):
        print(f'Word is \'{wordGues}\'.\nYou win!')
        break
