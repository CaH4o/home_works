# Home Work №1

# 1
name = input()
age = input()
sex = input()
# 2
task_2 = "Hello! My name is " + name + ". " \
                                       "I'm " + age + " and I'm a " + sex + "."
print(task_2)
# 3
task_3 = "Hello! My name is %s. I'm %s and I'm a %s." % (
    name,
    age,
    sex,
)
print(task_3)
# 4
task_4 = "Hello! My name is {}. I'm {} and I'm a {}.".format(
    name,
    age,
    sex,
)
print(task_4)
# 5
about_me_fstring = f"Hello! My name is {name}." \
                   f" I'm {age} and I'm a {sex}."
print(about_me_fstring)
# 6
task_6_1 = about_me_fstring.split('!')[0]
task_6_2 = about_me_fstring[about_me_fstring.index('Hello')
                            + len('Hello'):].split('.')[0]
task_6_3 = about_me_fstring[about_me_fstring.index('Hello')
                            + len('Hello'):].split('.')[1]
print(task_6_1, task_6_2, task_6_3)
# 7
name1 = 'Klara'
age1 = 28
sex1 = 'female'
about_me_friend = about_me_fstring.replace(name, name1)\
    .replace(age, str(age1))\
    .replace(sex, sex1)
print(about_me_friend)
# 8
list_from_str = about_me_fstring.split(' ')
print(list_from_str)
# 9
print(type(list_from_str))
# 10
str_from_list = ' '.join(list_from_str)
print(str_from_list)
# 11
print(about_me_fstring.swapcase())
