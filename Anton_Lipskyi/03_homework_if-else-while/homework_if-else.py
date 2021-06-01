with open('user_list.txt', 'a+') as file:
    file.seek(0)
    file_text = file.read()
    lines = file_text.split('\n')

    answer_acc = input('Do you have an account? \nAnswer y/n: ').lower()

    # проверим соответсвие шаблону y/n:
    while True:
        if answer_acc == 'y' or answer_acc == 'n':
            break
        else:
            answer_acc = input('Type only \'y/n\'. Please try again: ').lower()


    if answer_acc == 'n':
        answer_new_reg = input('Do you want to create one?: ').lower()

        # снова проверим на соответсвтие шаблону:
        while True:
            if answer_new_reg == 'y' or answer_new_reg == 'n':
                break
            else:
                answer_new_reg = input('Type only \'y/n\'. Please try again: ').lower()


        if answer_new_reg == 'y':
            login = input('Enter your Login: ').lower()

            # нужно узнать, нет ли уже пользователя с таким логином, и, не пустой ли он.
            # для этого 1 раз сделаем массив из существующих логинов,
            # чтобы не перебирать его каждый раз, и убрать вложеные циклы while

            user_array = []

            for line in lines:
                line.strip()
                log_pass = line.split(' ')
                login_value = log_pass[0]
                user_array.append(login_value)

            # теперь сама проверка:
            while True:

                if login == '':
                    login = input('Login can\'t be empty. Please try again: ').lower()
                elif login in user_array:
                    login = input('This name has been taken already. Try another: ').lower()
                else:
                    break


            password = input('Enter your Password: ')

            # проверим, не пустой ли пароль:
            while True:
                if password == '':
                    password = input('Password can\'t be empty. Please try again: ').lower()
                else:
                    break
            # если мы здесь, можно регистрировать пользователя
            file.write(f'\n{login} {password}')
            print('Registration has been completed')

        else:
            print('Ok, you still can work at only-read mode')


    # если пользователь в самом начале выбрал ответ 'Y':
    else:
        # user_registered = False

        # получим словарь с логинами и паролями, а также список пользователей
        user_dict = {}
        for line in lines[1:]:
            line.strip()
            log_pass = line.split(' ')
            login_value = log_pass[0]
            password_value = log_pass[1]
            user_dict.update({login_value: password_value})

        user_list = list(user_dict.keys())

        login = input('Enter your Login: ').lower()
        while True:
            if login not in user_list:
                login = input('Incorrect Login, try again: ')
            else:
                break

        password = input('Enter your Password: ')


        # проверка правильности пароля:
        correct_password = user_dict.get(login)

        while True:
            if password != correct_password:
                password = input('Incorrect Password, try again: ')

            else:
                print('Hello and Welcome')
                break




