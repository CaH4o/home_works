import string

print('Hi! What\'s your name?')
name = input('My name is:')
print(name, ', enter your age.')
age = input('My age is:')
print('Who are you:')
sex = input('My gender is:')    #1 (done)

about_me_fstring = 'Hello, my name is ' +  name + '. I\'m ' + age + ' and I\'m a ' + sex + '.'    #2 (done)
print(about_me_fstring)

first = 'Hello, my name is %s. I\'m %s and I\'m a %s.' % (name, age, sex)    #3 (done)
print(first)

second = 'Hello, my name is {0}. I\'m {1} and I\'m a {2}.'.format(name, age, sex)    #4 (done)
print(second)

third = f'Hello, my name is {name}. I\'m {age} and I\'m a {sex}.'    #5 (done)
print(third)

# 6 (done)

print('What\'s your friend\'s name?')
name1 = input('His/Her name:')
print(name, ', enter your friend\'s age.')
age1 = input('His/Her age:')
print('Who is your friend:')
sex1 = input('His/Her gender:')
about_me_fstring = about_me_fstring.replace(name, name1)
about_me_fstring = about_me_fstring.replace(age, age1)
about_me_fstring = about_me_fstring.replace(sex, sex1)
print(about_me_fstring)    #7 (done)

list_from_str = list(about_me_fstring)    #8 (done)
print(list_from_str)

print(type(list_from_str))  #9 (done)

str_from_list = ''.join(list_from_str)      #10 (done)
print(str_from_list)

print(about_me_fstring.swapcase())    #11 (done)