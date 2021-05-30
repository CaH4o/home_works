file = open('user_list.txt', 'r+', encoding='utf-8')
file_text = file.read()
lines = file_text.split('\n')

answer_acc = str(input('Do you have an account? \nAnswer y/n: ')).lower()

if answer_acc == 'n':
    answer_new_reg = str(input('Do you want to create one?: ')).lower()

    if answer_new_reg == 'y':
        login = str(input('Enter your Login: ')).lower()

        password = str(input('Enter your Password: '))
        print('Registration has been completed')
        file.write(f'\n{login} {password}')
    else:
        print('Ok, you still can work at only-read mode')


elif answer_acc == 'y':
    user_registered = False

    while not user_registered:
        login = str(input('Enter your Login: ')).lower()
        password = str(input('Enter your Password: '))

        for i, line in enumerate(lines[1:]):
            line.strip()
            log_pass = line.split(' ')
            login_value = log_pass[0]
            password_value = log_pass[1]

            # если пользователь в базе:
            if login_value == login:

                # проверим пароль
                correct_password = False
                while not correct_password:
                    # пока не получим правильный пароль:
                    if password_value != password:
                        password = str(input('Incorrect password, try again: '))
                    else:  # если пароль правильный
                        print('Hello and Welcome')
                        correct_password = True

                # если мы здесь, то пароль, и логин совпали, всё хорошо
                user_registered = True

        # если вышли из цикла и дошли сюда, значит пользователя нет в базе, всё с начала
        if not user_registered:
            print('\nNo such user in system, please try again')


else:
    print('type only \'y/n\'')

file.close()

