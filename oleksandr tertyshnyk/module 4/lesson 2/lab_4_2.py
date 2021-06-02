# *************************ЗАДАЧА №1******************************
# Вывести на экран числа от 0 до 100 включительно используя цикл for.
import random
import string


for i in range(100):
    print(i)

# *************************ЗАДАЧА №2******************************
# Найти сумму ряда чисел от 1 до 100, результат высести на экран (решить двумя способами,
# первый - for, второй - while).

myNum = range(100)
mySum = 0

for i in range(100):
    mySum += i
print(mySum)

mySum = 0
l = len(myNum)
while l > 0:
    l -= 1
    mySum += myNum[l]
print(mySum)

# *************************ЗАДАЧА №3******************************
# 1. Попросиль пользователя ввести 2 числа, первое в промежутке
# от 1 до 10, второе от 100 до 1000.
# 2. Создать 2 списка, первый состоящий только из четных чисел в промежутке
# от первого введенного пользователем числа до второго, второй список из нечетных чисел.
# (Решить задачу двумя способами:
# 	цикл for,
# 	list comprehension)

userNum_1 = int(input('Enter the number between 1 and 10 .......'))
userNum_2 = int(input('Enter the number between 100 and 1000 ...'))

listNum_1 = []
listNum_2 = []

for i in range(userNum_1, userNum_2):
    if i % 2:
        listNum_2.append(i)
    else:
        listNum_1.append(i)

print(listNum_1)
print(listNum_2)

listNum_1 = [i for i in range(userNum_1, userNum_2) if not i % 2]
listNum_2 = [i for i in range(userNum_1, userNum_2) if i % 2]
print(listNum_1)
print(listNum_2)

# *************************ЗАДАЧА №4******************************
# Вывести на экран циклом десять строк из 10 нулей, каждая строка
# должна быть пронумерована.

for i in range(11):
    print(i, 10 * '0')

# *************************ЗАДАЧА №5******************************
# 1. Попросить пользоватедя ввести число.
# 2. Найти факториал этого числа и вывести его на экран.

userNum = int(input('Enter the number .......'))
factorial = 1
for i in range(2, userNum):
    factorial *= i

print(factorial)
# *************************ЗАДАЧА №6******************************
# 1. Попросить пользоватедя ввести число.
# 2. Создать словарь, в котором ключем будет число, а значением будет квадрат
# этого числа (числа в ключе должны быть в промежутке от 2 до числа введенного пользователем).

userNum = int(input('Enter the number .......'))
myDict = {i: i ** 2 for i in range(2, userNum + 1)}
print(myDict)

myDict2 = {}
for i in range(2, userNum + 1):
    myDict2[i] =  i ** 2
print(myDict2)

# *************************ЗАДАЧА №7******************************
# 1. Создать словарь, в котором ключем будет порядковый номер буквы в алфавите, а значением сама буква.
# (Решить задачу двумя способами:
# 	цикл for,
# 	dict comprehension)
# 2. Создать новый словарь, в котором ключ и значение помменяются местами.

dict_s = {}
for s in string.ascii_lowercase:
    dict_s[string.ascii_lowercase.find(s)] = s
print(dict_s)

dict_s = {string.ascii_lowercase.find(s): s for s in string.ascii_lowercase}
print(dict_s)

dict_r = {}
for k, v in enumerate(dict_s.values()):
    dict_r[v] = k
print(dict_r)

# *************************ЗАДАЧА №8******************************
# Климатическая лаборатория отслеживает высокую температуру в пяти разных городах в течение
# первой недели июля. Идеальной структурой данных для хранения этих данных может быть
# представление списка вложенное в представление словаря:
#
# {
#     'Kiev': [0, 0, 0, 0, 0, 0, 0],
#     'Odessa': [0, 0, 0, 0, 0, 0, 0],
#     'Lviv': [0, 0, 0, 0, 0, 0, 0],
#     'Chernihiv': [0, 0, 0, 0, 0, 0, 0],
#     'Kharkiv': [0, 0, 0, 0, 0, 0, 0]
# }
#
# 1. Создать такой словарь имея список городов cities = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
# 2. Температура во вложенных списках должна быть случайной.
# (Решить задачу двумя способами:
# 	цикл for,
# 	dict comprehension)

cities = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
temp_cities = {}

for c in cities:
    temp_cities[c] = []
    for t in range(8):
        temp_cities[c].append(random.randint(-30, 50))
print(temp_cities)

temp_cities = {c: [random.randint(-30, 50) for t in range(8)] for c in cities}
print(temp_cities)
