# *************************ЗАДАЧА №1******************************
# Реализовать алгоритм пузырьковой сортировки.

list1 = [8, 4, 6, 5, 2, 0, 3, 10, 7, 1, 9]
print(list1)



def sort_buble(obj):
    if isinstance(obj, list):
        # cnt = 0
        e = 1
        sort_obj = obj.copy()
        while e < len(sort_obj):
            endSort = True
            for i, v in enumerate(sort_obj):
                # cnt += 1
                if i >= len(sort_obj) - e:
                     break
                else:
                     if sort_obj[i] > sort_obj[i + 1]:
                         sort_obj[i], sort_obj[i + 1] = sort_obj[i + 1], sort_obj[i]
                         endSort = False
                         continue
                     else:
                         continue
            if endSort:
                break
            e += 1
        # print(cnt)
        return sort_obj
    return obj


print(sort_buble(list1))
print(list1)

# *************************ЗАДАЧА №2******************************
# Написать программу которая просит у пользователя ввести его любимое число.
# Если ввод число, тогда поблагодорить пользователя за сотрудничество и завершить программу.
# Если ввод не число, тогда попросить его быть более внимательным и ввести именно число.
# Если неправильный ввод более 3 раз, перейти на более грубое предупреждение.
# Если неправильный ввод более 5 раз, дать пользователю последний шанс.
# Если ввод по прежнему не число, тогда обругать пользователя и завершить программу.

trying = 0
while True:
    try:
        userInput = input('Enter any number ...')
        userNumber = int(userInput)
    except ValueError:
        trying += 1
        if trying <= 3:
            print(f'\'{userInput}\' is not number. Please enter a number and be more carfully.')
            continue
        elif trying <= 5:
            print(f'\'{userInput}\' is not number. Is it easy to enter a number for yoy?.')
            continue
        elif trying == 6:
            print(f'\'{userInput}\' is not number. You have a last chance!')
        else:
            trying = -1
            print(f'\'{userInput}\' is not number. Are you blind? The program is over.')
            break
    else:
        trying = 0
        print(f'Thanks for number \'{userInput}\'.')
        break