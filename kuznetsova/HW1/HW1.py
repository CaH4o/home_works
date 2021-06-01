# 1. Взять ввод от пользователя узнав имя, возраст и пол, результат сохранить в переменных.
name = input ('Print your name:')
age = input('Print your age:')
sex = input ('Print our sex:')
# 2. Использовав созданные переменные создать строку 'Hello! My name is имя. I'm возраст and I'm a пол.'
# используя метод конкатенации, результат сохранить в переменной.
simple_info = "Hello! My name is "+ name + ". I'm " + age +  " and I'm a " + sex + "."
print (simple_info)
# 3. Создать такую же строку с помощью форматирования '%', результат записать в переменную.
percent_info = "Hello! My name is %s. I'm %s and I'm a %s." % (name, age, sex)
print(percent_info)
# 4. Создать такую же строку с помощью метода format, результат записать в переменную.
format_info = "Hello! My name is {0}. I'm {1} and I'm a {2}.".format(name, age, sex)
print(format_info)
# 5. Создать такую же строку с помощью F-строки, результат записать в переменную about_me_fstring.
about_me_fstring = f"Hello! My name is {name}. I'm {age} and I'm a {sex}."
print(about_me_fstring)
# 6. Под каждое предложение из about_me_fstring создать отдельную переменную с помощь возможностей
# языка, а не копипаста (первое предложение в первой переменной и тд.).
about_me_fstring_1 = about_me_fstring.split(sep='.')[0] + '.'
about_me_fstring_2 =about_me_fstring.split(sep='.')[1] + '.'
about_me_fstring_3 =about_me_fstring.split(sep='.')[2] + '.'
# 7. Оперируя переменной about_me_fstring создать строку о вашем друге/подруге, подставив соответствующие значения о нем/ней.
friend_name = input ("Print friend's name:")
friend_age = input ("Print friend's age:")
friend_sex = input ("Print friend's sex:")
about_me_fstring = f"Hello! My name is {friend_name}. I'm {friend_age} and I'm a {friend_sex}."
print(about_me_fstring)
# 8. Из about_me_fstring создать список и сохранить в переменной list_from_str.
list_from_str=about_me_fstring.split(sep='.')
print(list_from_str)
# 9. Узнать тип list_from_str.
print(type(list_from_str))
# 10. list_from_str склеить обратно в строку и записать в переменную str_from_list.
str_from_list=str(list_from_str[0]+list_from_str[1]+'.')
print(str_from_list)
# 11. Использовав about_me_fstring создать новую строку, где литеры в верхнем регистре будут преобразованы в нижний регистр, а литеры в
# нижнем регистре будут преобразованы в верхний регистр.
print(about_me_fstring.swapcase())