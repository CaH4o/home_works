# 1. Взять ввод от пользователя узнав имя, возраст и пол, результат сохранить в переменных.
# 2. Использовав созданные переменные создать строку 'Hello! My name is имя. I'm возраст and I'm a пол.'
# используя метод конкатенации, результат сохранить в переменной.
# 3. Создать такую же строку с помощью форматирования '%', результат записать в переменную.
# 4. Создать такую же строку с помощью метода format, результат записать в переменную.
# 5. Создать такую же строку с помощью F-строки, результат записать в переменную about_me_fstring.
# 6. Под каждое предложение из about_me_fstring создать отдельную переменную с помощь возможностей
# языка, а не копипаста (первое предложение в первой переменной и тд.).
# 7. Оперируя переменной about_me_fstring создать строку о вашем друге/подруге, подставив соответствующие значения о нем/ней.
# 8. Из about_me_fstring создать список и сохранить в переменной list_from_str.
# 9. Узнать тип list_from_str.
# 10. list_from_str склеить обратно в строку и записать в переменную str_from_list.
# 11. Использовав about_me_fstring создать новую строку, где литеры в верхнем регистре будут преобразованы в нижний регистр, а литеры в
# нижнем регистре будут преобразованы в верхний регистр.

# 1.
name = input('Укажите свое имя ')
age = input('Укажите свой возраст ')
sex = input('Укажите свой пол ')

# 2.
Hi = 'Hello! My name is ' + name + '. Im ' + age + ' and Im a ' + sex + '.'
print(Hi)

# 3.
Hi2 = 'Hello! My name is %s. Im %s and Im a %s.' % (name, age, sex)
print(Hi2)

# 4.
Hi3 = 'Hello! My name is {}. Im {} and Im a {}.'.format(name, age, sex)
print(Hi3)

# 5.
about_me_fstring = f'Hello! My name is {name}. Im {age} and Im a {sex}.'
print(about_me_fstring)

# 6.
S1 = about_me_fstring.split('!')
S2 = about_me_fstring.split('.')
S3 = S1[1].split('.')
Str1 = S1[0]
Str2 = S3[0]
Str3 = S2[1]
print(Str1)
print(Str2)
print(Str3)


# 7.
fr_name = input('Укажите имя друга ')
fr_age = input('Укажите возраст друга ')
fr_sex = input('Укажите пол друга ')

frend = about_me_fstring.replace(name, fr_name).replace(age, fr_age).replace(sex, fr_sex)
print(frend)

# 8.
list_from_str = list(about_me_fstring)
print(list_from_str)

# 9.
print(type(list_from_str))

# 10.
str_from_list = ''.join(list_from_str)
print(str_from_list)

# 11.
Swap = about_me_fstring.swapcase()
print(Swap)