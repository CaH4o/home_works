with open('log3.txt','a') as log_file, open('users.txt', 'w+') as file_reg:
    # Создать эмуляцию системы входа и регистрации для пользователей.
    # При запуске программы, пользователя должно спросить проходил ли он регистрацию на нашем ресурсе,
    registration = input('Welcome! Do you have already account? (y/n)\n')
    # если да, тогда предложить ему ввести логин и пароль от его учетной записи.
    # Если данные верны вывести сообщение об успешном входе в систему, если нет тогда сообщить об это.
    if registration == 'y':
        login = input('Login:')
        password = input('Password:')
        rstring = f'{login} {password}\n'
        print(rstring)
        reg_list = file_reg.readlines()
        for i in range(len(reg_list)):
            if reg_list[i] == rstring:
                is_ok = 'Y'
                break
            else:
                is_ok = 'N'
        if is_ok == 'Y':
            print('Success login!')
            log_file.write(f'Success login for {login}\n')
        else:
            print ('Incorrect login or password!')
            log_file.write(f'Failed login for {login}\n')
    # Если пользователь не регистрировался на ресурсе, тогда спросить не желает ли он пройти регистрацию.
    # Если желает, взять от него необходимые данные и вывести об успешной регистрации, если не желает
    # регистрироватся - пожелать удачи.
    elif registration == 'n':
        new_acc = input('Do you want to create an account?(y/n) \n')
        if new_acc == 'y':
            login = input(' Login:')
            password = input('Password:')
            rstring = f'{login} {password}\n'
            file_reg.readlines()
            file_reg.write(f'{login} {password}\n')
            print (f'User with login {login} and password {password} has been created!')
            log_file.write(f'User creation with login {login}\n')
        else:
            print('Good luck!')
    else:
        print("You didn't make a choice! Good luck!")
    # Данные о зарегестрированных пользователях хранить в файле 'users.txt', по желанию можете создать
    # файл для логирования событий регистрации и входа.
