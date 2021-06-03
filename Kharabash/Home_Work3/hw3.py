# Данные о зарегестрированных пользователях хранить в файле 'users.txt', по желанию можете создать
# файл для логирования событий регистрации и входа.

# Создать эмуляцию системы входа и регистрации для пользователей.
# При запуске программы, пользователя должно спросить проходил ли он регистрацию на нашем ресурсе

with open('user_log.txt','a') as user_log,\
        open('users.txt','r+') as users_reg:
    user_enter = input("Hello! Didn't make a register? Y/N: ")
    while True:
        if user_enter == 'Y' or user_enter == 'N':
            break
        else:
            user_enter = input('Type only Y / N. Try again: ')
# Если да, тогда предложить ему ввести логин и пароль от его учетной записи.
# Если данные верны вывести сообщение об успешном входе в систему, если нет тогда сообщить об это.
    if user_enter == 'Y':
        log_in = input('Log In: ')
        while log_in == '':
            log_in = input('Type something. Try again: ')
        password = input('Password: ')
        while password == '':
            password = input('Type something. Try again: ')
        print('Welcome!')
# Если пользователь не регистрировался на ресурсе, тогда спросить не желает ли он пройти регистрацию.
# Если желает, взять от него необходимые данные и вывести об успешной регистрации, если не желает
# регистрироватся - пожелать удачи.
    else:
        sign_in = input('Want Sign In? Y/N: ')
        while True:
            if sign_in == 'Y' or sign_in == 'N':
                break
            else:
                sign_in = input('Type only Y / N. Try again: ')
        if sign_in == 'Y':
            log_in_reg = input('Log In: ')
            while log_in_reg == '':
                log_in_reg = input('Type something. Try again: ')
            password_reg = input('Password: ')
            while password_reg == '':
                password_reg = input('Type something. Try again: ')
            user_log.write(f'Added new Login: {log_in_reg}'
                           f' and Password: {password_reg}\n')
            print('Welcome to the community!')
        else:
            print('Good luck!')
