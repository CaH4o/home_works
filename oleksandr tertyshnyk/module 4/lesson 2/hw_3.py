# Создать эмуляцию системы входа и регистрации для пользователей.
# При запуске программы, пользователя должно спросить проходил ли он регистрацию на нашем ресурсе,
# если да, тогда предложить ему ввести логин и пароль от его учетной записи.
# Если данные верны вывести сообщение об успешном входе в систему, если нет тогда сообщить об это.
# Если пользователь не регистрировался на ресурсе, тогда спросить не желает ли он пройти регистрацию.
# Если желает, взять от него необходимые данные и вывести об успешной регистрации, если не желает
# регистрироватся - пожелать удачи.
# Данные о зарегестрированных пользователях хранить в файле 'users.txt', по желанию можете создать
# файл для логирования событий регистрации и входа.

print('Welcome to OT site.')
while True:
    userRegistration = input('Do you have the registration? (y/n) ...')

    if userRegistration.lower() == 'stop':
        print('See you late!')
        break

    elif userRegistration.lower() == 'y':
        print('Please enter your:')

        while True:
            userLogin = input('Login: ')

            if not userLogin:
                print('Login is empty.')
                continue
            elif len(userLogin) < 3:
                print('Login is less then 3 letter.')
                continue
            else:
                break

        while True:
            userPassword = input('Password: ')

            if not userPassword:
                print('Password is empty.')
                continue
            elif len(userPassword) < 3:
                print('Password is less then 3 letter.')
                continue
            else:
                break

        criptPassword = ''.join([userPassword[i] for i, v in enumerate(userPassword) if not i % 2])
        criptPassword += ''.join([userPassword[i] for i, v in enumerate(userPassword) if i % 2])
        userStr = f'{userLogin}:!:{criptPassword}'

        with open('users.txt', 'r') as file:
            usersFile = file.read().split('\n')

        isUser = False
        for s in usersFile:
            if s == userStr:
                isUser = True
                break

        print('Login successful!' if isUser else 'Login failed')
        with open('logs.txt', 'a') as file:
            file.write(f'User:{userLogin}, login success:{isUser}\n')

        break

    elif userRegistration.lower() == 'n':
        while True:
            userIsNewRegistration = input('Would you like to registrate (y/n) ...')

            if userIsNewRegistration.lower() == 'n':
                print('Good luck!')
                break
            elif userIsNewRegistration.lower() == 'y':
                print('Please enter your:')

                while True:
                    userNewLogin = input('Login: ')

                    if not userNewLogin:
                        print('Login is empty.')
                        continue
                    elif len(userNewLogin) < 3:
                        print('Login is less then 3 letter.')
                        continue
                    else:
                        break

                while True:
                    userNewPassword = input('Password: ')

                    if not userNewPassword:
                        print('Password is empty.')
                        continue
                    elif len(userNewPassword) < 3:
                        print('Password is less then 3 letter.')
                        continue
                    else:
                        break

                criptNewPassword = ''.join([userNewPassword[i] for i, v in enumerate(userNewPassword) if not i % 2])
                criptNewPassword += ''.join([userNewPassword[i] for i, v in enumerate(userNewPassword) if i % 2])
                userStr = f'{userNewLogin}:!:{criptNewPassword}'

                with open('users.txt', 'a') as file:
                    file.write(userStr + '\n')

                print('Login is regestared successful!')
                break
            else:
                print('Please enter ''y''/''n''')

        break
    else:
        print('Please enter ''y''/''n'', or ''stop'' to exit')

