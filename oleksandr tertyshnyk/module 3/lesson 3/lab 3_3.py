# *************************ЗАДАЧА №1******************************
# 1. Создать список состоящий из последовательности чисел от 10 до 20 включительно;
# 2. Перевернуть этот список задом на перед;
# 3. Вставить в начало списка число 21, в конец списка 9;
# 4. Удалить из списка любое число используя известный вам метод;
# 5. Удалить из списка любое число используя инструкцию del;
# 6. Отсортировать список по возрастанию;
# 7. Найти сумму элементов списка.

#1
import random
import math

list_1 = list_1 = list(range(10, 21))
print(list_1)

#2
list_1.reverse()
print(list_1)

#3
list_1.insert(0, 21)
list_1.append(9)
print(list_1)

#4
list_1.remove(random.randint(9, 21))
print(list_1)

#5
del list_1[random.randint(0, 11)]
print(list_1)

#6
list_1.sort()
print(list_1)

#7
print(sum(list_1))

# *************************ЗАДАЧА №2******************************
# 1. Попросить у пользователя ввести случайное число от 10 до 30;
# 2. Создать список состоящий из первых 10 букв алфавита (каждый элемент списка отдельная буква), результат записать в переменную;
# 3. Создать список состоящий из оставшихся букв алфавита (каждый элемент списка отдельная буква), результат записать в переменную;
# 4. Создать список состоящий из цифр от 0 до 9 (каждый элемент списка отдельная цифра), результат записать в переменную;
# 5. Расширить первый список вторым и третим (результат должен быть одним списком);
# 6. Используя расширенный список создать случайный ключ длиной, которую нам ввел пользователь в первом пункте (результат должен быть строкой).
import string

#1
userValue = int(input('Please enter number from 10 to 30...'))

#2
list_2 = list(string.ascii_letters[:10])
print(list_2)

#3
list_3 = list(string.ascii_letters[10:])
print(list_3)

#4
list_4 = list(string.digits)
print(list_4)

#5
list_2.extend(list_3)
list_2.extend(list_4)
print(list_2)

#6
keySample = ''.join(random.sample(list_2, userValue))
print(keySample)

# *************************ЗАДАЧА №3******************************
# 1. Попросить пользователя ввести дату своего рождения в формате дд.ММ.гггг, текущий рост и вес;
# 2. Попросить пользователя ввести дату рождения одного из родственников в формате дд-ММ-гггг;
# 3. Создать пустой список и поместить в него рост и вес, а дата рождения пользователя должна быть вложенным списком и разбита по элементно (разбить дату по .);
# 4. Расширть вложенный список с датой рождения пользователя второй датой разбитой аналогичным методом;
# 5. Вырезать из созданного списка вложеный список и сохранить в отдельной переменной, при этом вложенный список должен удалиться из основного списка.

#1
userBirthDate = input('Please enter your date of birth (dd.mm.yyyy)...')
userHigh = int(input('Please enter your high (cm).........................'))
userWight = int(input('Please enter your wight (kg).......................'))

#2
userBirthDate_2 = input('Please enter date of birth your relative (dd-mm-yyyy)...')

#3
userList = []
userList.append(userHigh)
userList.append(userWight)
userList.append(userBirthDate.split('.'))
print(userList)

#4
userList[2].extend(userBirthDate_2.split('-'))
print(userList)

#5
userBirthDate_3 = userList.pop(2)
print(userList)
print(userBirthDate_3)

# *************************ЗАДАЧА №4******************************
# 1. Попросить пользователя ввести двузначное число;
# 2. Попросить пользователя ввести четырёхзначное число;
# 3. Создать список состоящий из 10 случайных чисел в промежутке от двузначного числа до четырёхзначного;
# 4. Поменять местами максимальный и минимальный елементы списка.

#1
user2DNumbers = int(input('Please enter a two-digit number....'))

#2
user4DNumbers = int(input('Please enter a four-digit number...'))

#3
list_random = list(random.sample(range(user2DNumbers, user4DNumbers), 10))
print(list_random)

#4
list_random[list_random.index(max(list_random))], list_random[list_random.index(min(list_random))] = \
    list_random[list_random.index(min(list_random))], list_random[list_random.index(max(list_random))]
print(list_random)

# *************************ЗАДАЧА №5******************************
# 1. Создать список с тремя вложенными случайными списками (каждый вложенный список должен состоять из 10 элементов);
# 2. Сделать так чтобы первые три элемента первого вложенного списка были равны последним трем элементам третьего вложенного списка и наоборот
# (значения должны поменяться местами);
# 3. Заменить второй вложенный список на список в котором первая половина значений будут взяты из первого вложенного списка, а вторая часть из третьего;
# 4. Объединить все три вложенных списка в один в один целый.

#1
super_list = []
super_list.append(list(random.sample(range(1, 1000), 10)))
super_list.append(list(random.sample(range(1, 1000), 10)))
super_list.append(list(random.sample(range(1, 1000), 10)))
print(super_list)

#2
super_list[0][0], super_list[-1][-1] = super_list[-1][-1], super_list[0][0]
super_list[0][1], super_list[-1][-2] = super_list[-1][-2], super_list[0][1]
super_list[0][2], super_list[-1][-3] = super_list[-1][-3], super_list[0][2]
print(super_list)

#3
super_list[1][:5] = super_list[0][:5]
super_list[1][5:] = super_list[-1][5:]
print(super_list)

#4
super_list.extend(super_list.pop(0))
super_list.extend(super_list.pop(0))
super_list.extend(super_list.pop(0))
print(super_list)