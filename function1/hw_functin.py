# Task1

from random import randint

n = 15
list_of_num = []
for i in range(n):
    list_of_num.append(randint(0, 50))
# print(list_of_num)


def bobbles(sort_list):
    last_item = len(sort_list) - 1
    for i in range(0, last_item):
        for x in range(0, last_item):
            if sort_list[x] > sort_list[x+1]:
                sort_list[x], sort_list[x + 1] = sort_list[x + 1], sort_list[x]

    return sort_list


sort_list = list_of_num.copy()
print(sort_list)
print(bobbles(list_of_num))


# Task2

def user_enter():
    for i in range(7):
        user_input = input('Enter your favorite number: ')
        print(i)
        try:
            number = int(user_input)
            print('success')
        except ValueError as err:
            if i < 3:
                print("wrong number")
            elif i < 5:
                print("wrong number, just a few attempts left")
            elif i == 5:
                print('last chance')
            else:
                print('fail')
            continue
        break


user_enter()

