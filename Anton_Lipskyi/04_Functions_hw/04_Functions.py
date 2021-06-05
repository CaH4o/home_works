# задача №1
# вариант №1 - через вложеный цикл, простым полным проходом, с уменьшением шага каждый раз:
'''
# Вариант #1, через 2 цикла, полный проход
def silly_sort(arr):
    lenth = len(arr)
    while lenth >= 2:
        count = 0
        for i in range(lenth-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        if count == 0:
            print(f'\ncompleted it earlier, on cycle # {len(arr)-lenth}')
            break
        lenth -= 1

        '''

# вариант №2, пока массив в результате цикла меняется

def silly_sort_diff(arr):
    lenth = len(arr)
    arr_temp, arr = arr.copy(), []
    while arr_temp != arr:
        arr = arr_temp.copy()
        lenth -= 1
        for i in range(lenth):
            if arr_temp[i] > arr_temp[i+1]:
                arr_temp[i], arr_temp[i+1] = arr_temp[i+1], arr_temp[i]

    return arr_temp

# arr1 = [90, 60, 55, 48, 32, 21, 2]
# arr_sorted = silly_sort_diff(arr1)
# print(arr_sorted)

# arr2 = [101, 202, 505, 404, 606, 707]
# arr_sorted2 = silly_sort_diff(arr2)
# print(arr_sorted2)

# arr3 = [1, 2, 3, 4, 6, 7]
# arr_sorted3 = silly_sort_diff(arr3)
# print(arr_sorted3)


# вариант №3 через рекурсию (ну, или похоже на то, пока не знаю точно):
'''
def rec_sort(arr, arr_temp=[]):
    arr_temp = arr.copy()
    for i in range(len(arr_temp)-1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if arr_temp == arr:
        return arr_temp
    else:
        rec_sort(arr)


# arr4 = [90, 60, 55, 48, 32, 21, 2]
# rec_sort(arr4)
# print(arr4)

# arr5 = [101, 202, 505, 404, 606, 707]
# rec_sort(arr5)
# print(arr5)

# arr6 = [1, 2, 3, 4, 6, 7]
# rec_sort(arr6)
# print(arr6 )

'''

# Задача 2

def fav_num():

    message_list = [
        'Input your favourite number : ',
        'Please pay attention! this should be an integer, try again : ',
        'Please pay attention! this should be an integer, try again : ',
        'Hey! this is not funny, should be a number! : ',
        'Hey! this is not funny, should be a number! : ',
        'This is your last chanche! : ',
                    ]

    for var in message_list:
        digit = input(var)
        try:
            favourite = int(digit)
            print('Thank you, have a nice day!')
            return favourite
        except ValueError:
            pass

    print('You are either hopeless, or curious, Bye! ')
    return None

fav_num()









