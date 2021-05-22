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

#1
userName = input(   'Please enter your name (just first name)...')
userAge = int(input('Please enter your agr (only numbers).......'))
userGender = input( 'Please enter your gender (male/female).....')

#2
strWellcom = 'Hello! My name is ' + userName + '. I\'m ' + str(userAge) + ' and I\'m a ' + userGender + '.'
print(f'#2: {strWellcom}')

#3
strWellcom = 'Hello! My name is %s. I\'m %i and I\'m a %s.' % (userName, userAge, userGender)
print(f'#3: {strWellcom}')

#4
strWellcom = 'Hello! My name is {n}. I\'m {a} and I\'m a {g}.'\
    .format(a=userAge, g=userGender, n=userName)
print(f'#4: {strWellcom}')

#5
about_me_fstring = f'Hello! My name is {userName}. I\'m {userAge} and I\'m a {userGender}.'
print(f'#5: {about_me_fstring}')

#6
strSentence_1 = about_me_fstring[:about_me_fstring.find('!') + 1]
strSentence_2 = about_me_fstring[about_me_fstring.find('!') + 2: about_me_fstring.find('.') + 1]
strSentence_3 = about_me_fstring[about_me_fstring.find('.') + 2:]
print(f'#6: {strSentence_1}')
print(f'#6: {strSentence_2}')
print(f'#6: {strSentence_3}')

#7
friendName = 'Gloria'
friendAge = 30
friendGender = 'female'
about_me_fstring = about_me_fstring\
    .replace(userName, friendName)\
    .replace(str(userAge), str(friendAge))\
    .replace(userGender, friendGender)
print(f'#7: {about_me_fstring}')

#8
list_from_str = about_me_fstring.replace('!', '.').split('.')
print(f'#8: {list_from_str}')

#9
print(f'#9: {type(list_from_str)}')

#10
str_from_list = ''.join(list_from_str)
print(f'#10: {str_from_list}')

#11
about_me_fstring = about_me_fstring.swapcase()
print(f'#11: {about_me_fstring}')