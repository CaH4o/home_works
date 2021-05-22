#
# # *************************ЗАДАЧА №1******************************
# # 1. Создать 2 кортежа используя разные методы (внутри кортежа храните что угодно, но
# # некоторые элементы должны повторятся в обеех кортежах);
# # 2. Создать кортеж состоящий из пересечения кортежей выше;
# # 3. Создать союз этих кортежей;
# # 4. Создать новый кортеж, который будет состоять лишь из тех элементов, которые отличаю данные кортежи;
# # 5. Создать обратный кортеж из получившегося кортежа в 3-ем пункте (развернуть задома на перед);
# # 6. Преобразовать получившейся выше кортеж в список.
#
# #1
# tupleFirst = (1, 2, 3, 4, 5)
# tupleSecond = tuple(['a', 'b', 'c', 3, 4])
# print(tupleFirst, tupleSecond)
#
# #2
# tupleInner = tuple(set(tupleFirst) & set(tupleSecond))
# print(tupleInner)
#
# #3
# tupleUnion = tuple(set(tupleFirst) | set(tupleSecond))
# print(tupleUnion)
#
# #4
# tupleLeftInner = tuple(set(tupleFirst) - set(tupleSecond))
# tupleRightInner = tuple(set(tupleSecond) - set(tupleFirst))
# tupleExclude = tupleLeftInner + tupleRightInner
# print(tupleExclude)
#
# #5
# tupleRevers = tupleUnion[::-1]
# print(tupleRevers)
#
# #6
# print(list(tupleRevers))
#
#
# # *************************ЗАДАЧА №2******************************
# # 1. Взять ввод от пользователя (его имя, фамилию и возраст);
# # 2. В файл new_file.txt записать строку 'Имя Фамилия - возраст';
# # 3. Перезаписать файл таким образом, чтобы изменить в нем лишь возраст.
#
# #1
# # userFirstName = input('Please enter your first name ....')
# # userFamilyName = input('Please enter your family name ...')
# # userAge = int(input('Please enter your age ...........'))
# userFirstName = 'Alex'
# userFamilyName = 'James'
# userAge = 32
#
# #2
# with open('new_file.txt', 'w') as new_file:
#     new_file.write(f'{userFirstName} {userFamilyName} - {userAge}')
#
# #3
# with open('new_file.txt', 'r+') as new_file:
#     # new_file.write(f'{userFirstName} {userFamilyName} - {userAge + 10}')
#     new_file.seek(len(userFirstName) + len(userFamilyName) + 4)
#     new_file.write(str(userAge + 10))
#
# # *************************ЗАДАЧА №3******************************
# # 1. Открыть тот же файл и перезаписать его содержимое на эту же строку в обратном порядке (задом на перед).
# with open('new_file.txt', 'r+') as new_file:
#      reversString = new_file.read()
#      new_file.write(reversString[::-1])

# *************************ЗАДАЧА №4******************************
# Содержимое файл:
#
# Рудковский К.
# Иванов О.
# Петров И.
# Дмитриев Н.
# Смирнова О.
# Керченских В.
# Котов Д.
# Иванов О.
# Бирюкова Н.
# Данилов П.
# Аранских В.
# Лемонов Ю.
# Олегова К.
# Данилов П.
# Смирнова О.
# Керченских В.
# Петров И.
# Стадкевич О.
# Васюченко А.
# Рудковский К.
# Пацук И.
#
# 1. Считать данные с файла и сохранить только уникальные значения;
# 2. Записать их в новый файл в алфавитном порядке (каждый элемент в новой строке).

#1
names = ''

with open('names.txt', 'r', encoding='utf-8') as new_file:
    # print(new_file)
    names = new_file.readlines()
    names = set(names)
    # print(names)

#2
names = list(names)
names.sort()
names = ''.join(names)
# print(names)

with open('names_sort.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(names)