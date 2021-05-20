# 1. Взять ввод от пользователя узнав имя, возраст и пол, результат сохранить в переменных.
name = input()
age = input()
sex = input()
# 2. Использовав созданные переменные создать строку 'Hello! My name is имя. I'm возраст and I'm a пол.'
# используя метод конкатенации, результат сохранить в переменной.
# var1 = "Hello! My name is "
# var2 = "I'm "
# var3 = "and I'm a "
# print(var1 + name + '. ' + var2 + age + ' ' + var3 + sex + '.')
# 3. Создать такую же строку с помощью форматирования '%', результат записать в переменную.
# task_3 = "Hello! My name is %s." % name, "I'm %s" % age, "and I'm a %s." % sex
# print(task_3)
# 4. Создать такую же строку с помощью метода format, результат записать в переменную.
task_4 = "Hello! My name is {}. I'm {} and I'm a {}.".format(name, age, sex)
print(task_4)
# 5. Создать такую же строку с помощью F-строки, результат записать в переменную about_me_fstring.
about_me_fstring = f"Hello! My name is {name}. I'm {age} and I'm a {sex}."
print(about_me_fstring)
# 6. Под каждое предложение из about_me_fstring создать отдельную переменную с помощь возможностей
# языка, а не копипаста (первое предложение в первой переменной и тд.).
task_6 = about_me_fstring.split()
task_6_1 = task_6[0]
task_6_2 = task_6[1:5]
task_6_3 = task_6[5:11]
print(task_6_1, task_6_2, task_6_3)
# 7. Оперируя переменной about_me_fstring создать строку о вашем друге/подруге, подставив соответствующие значения о нем/ней.
# about_me_fstring = f"Hello! My name is {name}. I'm {age} and I'm a {sex}."
# print(about_me_fstring)
# 8. Из about_me_fstring создать список и сохранить в переменной list_from_str.
list_from_str = about_me_fstring.split()
print(list_from_str)
# 9. Узнать тип list_from_str.
print(type(list_from_str))
# 10. list_from_str склеить обратно в строку и записать в переменную str_from_list.
import string
str_from_list = string.join(list_from_str)
print(str_from_list)

# 11. Использовав about_me_fstring создать новую строку, где литеры в верхнем регистре будут преобразованы в нижний регистр, а литеры в
# нижнем регистре будут преобразованы в верхний регистр.
print(about_me_fstring.swapcase())
