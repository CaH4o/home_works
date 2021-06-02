user_infor = {}
with open('users.txt', 'r') as file_name:
    lines = file_name.readlines()
    for row in lines:
        row = row.strip()
        login, password = row.split(' ')

information = input('Ви проходили реєстрацію?')
if information == 'так':
    login = input('Ваш логін:')
    password = input('Ваш пароль:')

if login in user_infor:
    old_password = user_infor[login]
    if password == old_password:
        print('Ви увійшли в систему')
    else:
        print('Не правильні данні')

else:
        with open('users.txt', 'w') as file_name:
                new_lines = file_name.writelines()
                for new_row in new_lines:
                        new_row = row.strip()
                        new_login, new_password = row.split(' ')

                        new_information = input('Бажаєте зареєструватись?')
                        if new_information == 'так':
                                new_login = input('Ваш логін:')
                                new_password = input('Ваш пароль')
                                print('Ви увійшли в систему')
                                file_name.writelines(new_lines)
                        else:
                                print('Бажаємо успіху')





