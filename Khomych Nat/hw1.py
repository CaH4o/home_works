# 1. Взять ввод от пользователя узнав имя, возраст и пол, результат сохранить в переменных.

user_name = input('Input your name, please! ')
user_age = input('Input your age, please! ')
user_gender = input('Input your gender, please! ')


# 2. Использовав созданные переменные создать строку 'Hello! My name is имя. I'm возраст and I'm a пол.'
# используя метод конкатенации, результат сохранить в переменной.

text = 'Hello! My name is ' + user_name + '. I\'m ' + user_age + ' and I\'m a ' + user_gender + '.'
print(text)


# 3. Создать такую же строку с помощью форматирования '%', результат записать в переменную.

text2 = 'Hello! My name is %s. I\'m %s and I\'m a %s.' % (user_name, user_age, user_gender)
print(text2)


# 4. Создать такую же строку с помощью метода format, результат записать в переменную.

text3 = 'Hello! My name is {}. I\'m {} and I\'m a {}.'.format(user_name, user_age, user_gender)
print(text3)


# 5. Создать такую же строку с помощью F-строки, результат записать в переменную about_me_fstring.

about_me_fstring = f'Hello! My name is {user_name}. I\'m {user_age} and I\'m a {user_gender}.'
print(about_me_fstring)


# 6. Под каждое предложение из about_me_fstring создать отдельную переменную с помощь возможностей
# языка, а не копипаста (первое предложение в первой переменной и тд.).

end_sent1 = about_me_fstring.index('!')
end_sent2 = about_me_fstring.index('.')
sentence1 = about_me_fstring[:end_sent1 + 1]
sentence2 = about_me_fstring[end_sent1 + 2:end_sent2 + 1]
sentence3 = about_me_fstring[end_sent2 + 2:]
print(sentence1)
print(sentence2)
print(sentence3)


# 7. Оперируя переменной about_me_fstring создать строку о вашем друге/подруге,
# подставив соответствующие значения о нем/ней.

friend_name = input('Input your friend name, please! ')
friend_age = input('Input your friend age, please! ')
friend_gender = input('Input your friend gender, please! ')

about_friend = about_me_fstring.replace(user_name, friend_name).replace(user_age, friend_age).replace(
    user_gender, friend_gender)
print(about_friend)

# 8. Из about_me_fstring создать список и сохранить в переменной list_from_str.

list_from_str = list(about_me_fstring)
print(list_from_str)


# 9. Узнать тип list_from_str.

print(type(list_from_str))


# 10. list_from_str склеить обратно в строку и записать в переменную str_from_list.

str_from_list = ''.join(list_from_str)
print(str_from_list)


# 11. Использовав about_me_fstring создать новую строку,
# где литеры в верхнем регистре будут преобразованы в нижний регистр, а литеры в
# нижнем регистре будут преобразованы в верхний регистр.

text4 = about_me_fstring.swapcase()
print(text4)


# *************************ЗАДАЧА №5******************************
# 1. Создать список с тремя вложенными случайными списками (каждый вложенный список должен состоять из 10 элементов);

import random
my_list = []
list1 = random.sample(range(100), 10)
list2 = random.sample(range(100), 10)
list3 = random.sample(range(100), 10)

my_list.append(list1)
my_list.append(list2)
my_list.append(list3)
print(my_list)


# 2. Сделать так чтобы первые три элемента первого вложенного списка были равны
# последним трем элементам третьего вложенного списка и наоборот
# (значения должны поменяться местами);

my_list[0][0], my_list[0][1], my_list[0][2], my_list[-1][-1], my_list[-1][-2], my_list[-1][-3] = \
    my_list[-1][-3], my_list[-1][-2], my_list[-1][-1], my_list[0][2],  my_list[0][1], my_list[0][0]
print(my_list)


# 3. Заменить второй вложенный список на список, в котором первая половина значений будут взяты из
# первого вложенного списка, а вторая часть из третьего;

length_list1 = len(my_list[0])
length_list3 = len(my_list[2])
my_list[1].clear()
my_list[1].extend(my_list[0][:length_list1 // 2])
my_list[1].extend(my_list[2][length_list3 // 2:])
print(my_list)


# 4. Объединить все три вложенных списка в один в один целый.

list1.extend(list2)
list1.extend(list3)
print(list1)
