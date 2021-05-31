#-= Homework #1 by Mykola Honchar =-
# This temporary string for GIT
#1. Взять ввод от пользователя узнав имя, возраст и пол, результат сохранить в
# переменных.
import string
name = input("Input your name, please! ")
age = input("Input your age, please! ")
gender = input("Input your gender, please! ")

#2. Использовав созданные переменные создать строку 'Hello! My name is имя. I'm
# возраст and I'm a пол.' используя метод конкатенации, результат сохранить
# в переменной.

my_intro_2 = "Hello! My name is " + name + ". I'm " + age + " years old and" \
            " I'm a " + gender + "."
print(my_intro_2)

#3. Создать такую же строку с помощью форматирования '%', результат записать
# в переменную.
my_intro_3 = "Hello! My name is %s. I'm %s years old and I'm a %s." \
             %(name, age, gender)
print(my_intro_3)

#4. Создать такую же строку с помощью метода format, результат записать в
# переменную.
my_intro_4 = "Hello! My name is {}. I'm {} years old and I'm a {}."\
      .format(name, age, gender)
print(my_intro_4)

#5. Создать такую же строку с помощью F-строки, результат записать в переменную
# about_me_fstring.
about_me_fstring = f"Hello! My name is {name}. I'm {age} years old and" \
                   f" I'm a {gender}."
print (about_me_fstring)

#6. Под каждое предложение из about_me_fstring создать отдельную переменную
# с помощь возможностей языка, а не копипаста (первое предложение в первой
# переменной и тд.).
frst_sent = about_me_fstring[:about_me_fstring.index('!')+1]
print(frst_sent)
sec_sent = about_me_fstring[about_me_fstring.index('!')+2:
                            about_me_fstring.index('.')+1]
print(sec_sent)
thrd_sent = about_me_fstring[about_me_fstring.index('.')+2:]
print(thrd_sent)

#7. Оперируя переменной about_me_fstring создать строку о вашем друге/подруге,
# подставив соответствующие значения о нем/ней.
name_f = input("Input your friend/girlfriend name, please! ")
age_f = str(input("Input your friend/girlfriend age, please! "))
gender_f = input("Input your friend/girlfriend gender, please! ")
print(about_me_fstring.replace("My", "My friend's").replace("I'm", "He's/She's")
      .replace(name, name_f).replace(age, age_f).replace(gender, gender_f))

#8. Из about_me_fstring создать список и сохранить в переменной list_from_str.
list_from_str=list(about_me_fstring)
print(list_from_str)

#9. Узнать тип list_from_str.
print(type(list_from_str))

#10. list_from_str склеить обратно в строку и записать в переменную
# str_from_list.
str_from_list = ''.join(list_from_str)
print(str_from_list)


#11. Использовав about_me_fstring создать новую строку, где литеры в верхнем
# регистре будут преобразованы в нижний регистр, а литеры в нижнем регистре
# будут преобразованы в верхний регистр.
new_str = about_me_fstring.swapcase()
print(new_str)