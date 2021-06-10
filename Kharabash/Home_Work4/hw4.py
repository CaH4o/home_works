# *************************ЗАДАЧА №1******************************
# Реализовать алгоритм пузырьковой сортировки.
from random import randint
bubbles = 10
bubble_list = []
for i in range(bubbles):
    bubble_list.append(randint(4, 88))
print(bubble_list)

for i in range(bubbles - 1):
    for j in range(bubbles - i - 1):
        if bubble_list[j] > bubble_list[j + 1]:
            bubble_list[j], bubble_list[j + 1] =\
                bubble_list[j + 1], bubble_list[j]

print(bubble_list)
# *************************ЗАДАЧА №2******************************
# Написать программу которая просит у пользователя ввести его любимое число.
# Если ввод число, тогда поблагодорить пользователя за сотрудничество и
# завершить программу.
# Если ввод не число, тогда попросить его быть более внимательным и ввести
# именно число.
# Если неправильный ввод более 3 раз, перейти на более грубое предупреждение.
# Если неправильный ввод более 5 раз, дать пользователю последний шанс.
# Если ввод по прежнему не число, тогда обругать пользователя и
# завершить программу.


def done():
    print('Thank you for interaction, you have done!')


def enter_4th():
    print('You have 4 incorrect enter. You need be attentive')


def enter_6th():
    print('You have 6 incorrect enter. You have last chance!')


def enter_last():
    print('You are strange a$$hole. Good bye!')


all_attempts = 0
for a in range(7):
    try:
        user_enter = int(input('Enter your best number: '))
        print(f'Thank you for interaction,'
              f' you have done! Your number {user_enter}')
        break
    except ValueError:
        all_attempts = a + 1
        if all_attempts == 4:
            enter_4th()
            continue
        elif all_attempts == 6:
            enter_6th()
            continue
        elif all_attempts == 7:
            enter_last()
        else:
            print("Enter must be a digit and"
                  " doesn't be empty. Try again.")
            continue
