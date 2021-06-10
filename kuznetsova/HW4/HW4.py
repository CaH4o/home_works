# *************************ЗАДАЧА №1******************************
# Реализовать алгоритм пузырьковой сортировки.
list_first = [1,60,8,90,10,50,0,3,6]
i = 0
j = 0
for j in range(len(list_first)):
    for  i in range(len(list_first)-1-j):
         if list_first[i]>list_first[i+1]:
             temp = list_first[i]
             list_first[i] = list_first[i+1]
             list_first[i+1] = temp
print(list_first)

# *************************ЗАДАЧА №2******************************
# Написать программу которая просит у пользователя ввести его любимое число.
# Если ввод число, тогда поблагодорить пользователя за сотрудничество и завершить программу.
# Если ввод не число, тогда попросить его быть более внимательным и ввести именно число.
# Если неправильный ввод более 3 раз, перейти на более грубое предупреждение.
# Если неправильный ввод более 5 раз, дать пользователю последний шанс.
# Если ввод по прежнему не число, тогда обругать пользователя и завершить программу.

i = 1
while i <= 6:
    try:
        digit = int(input('Please write your favourite digit:'))
        print('Than you! Have a nice day!')
        break
    except ValueError:
        i += 1
        if i <= 3:
            print(f'Pay attantion please! I\'m expexting a digit! Try {i}.')
        elif i <= 5:
            print(f'Are you drunk? You are writing {i} times not a digit!')
        elif i == 6:
            print('This is your last chance to prove your normality!')
        else:
            print('You are too stupid for this task! Good bye!')
