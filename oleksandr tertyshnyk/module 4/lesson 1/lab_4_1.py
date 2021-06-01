# *************************ЗАДАЧА №1******************************
# 1. Узнать у пользователя его возраст;
# 2. Если пользователь достиг совершеннолетия, тогда вывести сообщение о том, что доступ разрешен;
# 3. Если ему меньше 18, тогда вывести сообщение, что нужно подождать n лет.

userAge = int(input('Enter your Age ...'))
if userAge > 17:
    print('Access is allowed!')
else:
    waite = 18 - userAge
    print(f'You need wait {waite} years')

# *************************ЗАДАЧА №2******************************
# 1. Взять от пользователя три числа;
# 2. Определить максимальное число без использования функции max().

userNumber_1 = int(input('Enter the first number .....'))
userNumber_2 = int(input('Enter the second number ....'))
userNumber_3 = int(input('Enter the third number .....'))

if userNumber_1 <= userNumber_2 >= userNumber_3:
    print(f'{userNumber_2} is max number')
elif userNumber_2 <= userNumber_3 >= userNumber_1:
    print(f'{userNumber_3} is max number')
elif userNumber_3 <= userNumber_1 >= userNumber_2:
    print(f'{userNumber_1} is max number')
else:
    print('error')
# *************************ЗАДАЧА №3******************************
# 1. Попросить у пользователя ввести случайное число от 5 до 15;
# 2. Создать кортеж состоящий из чисел от 0 до числа введеного пользователем;
# 3. Вывести на экран информацию, которая будет иметь вид:
# 	0
# 	-----
# 	1
# 	-----
# 	...
# 	n
# 	Success!

userNumber = int(input('Enter the number from 5 till 15 (5-15) ....'))
userTuple = tuple(range(0, userNumber))
print(*userTuple, sep='\n-----\n' , end='\nSuccess!')

# *************************ЗАДАЧА №4******************************
# 1. Попросить пользователя ввести любое целое число;
# 2. Если число четное, вывести 'Even number';
# 3. Если нечетное - 'Odd number'.

userNumber = int(input('Enter any even number  ....'))
if not userNumber % 2:
    print('Even number')
else:
    print('Odd number')

# *************************ЗАДАЧА №5******************************
# 1. Попросить пользователя ввести год;
# 2. Определить високосный год или нет.
# Високосный год, определяется по следующему алгоритму:
# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные;
# остальные годы, номер которых кратен 4, — високосные.

userYear = int(input('Enter a year  ....'))

if not userYear % 400 or userYear % 100 and not userYear % 4:
    print('leap year')
else:
    print('Not leap year')

# *************************ЗАДАЧА №6******************************
# Есть два файла whitelist.txt и blacklist.txt, наполните их именами и фамилиями пользователей.
#
# 1. Попросить пользователя ввести имя и фамилию;
# 2. Если имени нет в черном и белом списках, тогда добавить пользователя в whitelist.txt;
# 3. Если имя есть в белом списке, вывести приветствие;
# 4. Если имя в черном списке, тогда вывести сообщение, что имя в блоке.

# with open('whitelist.txt', 'w') as file_print:
#     file_print.write('John Doe\nJim Karter\nSandy Shine\n')
#
# with open('blacklist.txt', 'w') as file_print:
#     file_print.write('Jim Morty\nAnny Kruy\n')

userName = input("Enter first and family names ...")

with open('blacklist.txt', 'r') as file_print:
    blacklist = file_print.read().lower().split('\n')

with open('whitelist.txt', 'r') as file_print:
    whitelist = file_print.read().lower().split('\n')

if userName.lower() in whitelist:
    print(f'Hello {userName}!')
elif userName.lower() in blacklist:
    print(f'{userName} is in block!')
else:
    with open('whitelist.txt', 'a') as file_print:
        file_print.write(userName + '\n')
    print(f'{userName} added to the white list!')

# print(f'blacklist: {blacklist}')
# print(f'whitelist: {whitelist}')

# *************************ЗАДАЧА №7******************************
# 1. Прочитать содержимое файлов whitelist.txt и blacklist.txt;
# 2. Сделать вывод не на экран, а в новый файл
# Вывод должен выглядеть так:
# 	Имя
# ХХХХХХХХХХХХХХХХХХХХ
# 	Имя
# ХХХХХХХХХХХХХХХХХХХХ
# 	...
#     Print Finished

with open('blacklist.txt', 'r') as file_print:
    newList = file_print.readlines()

with open('whitelist.txt', 'r') as file_print:
    newList.extend(file_print.readlines())

# print(newList)
with open('newlist.txt', 'w') as file_print:
    print(*newList, sep='XXXXXXXXXXXXXXXXXXXX\n', end='    Print Finished', file=file_print)
