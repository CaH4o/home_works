# Реализуйте шифратор и дешифратор по шифру Цезаря.
# Спросить пользователя, что он хочет сделать - зашифровать или расшифровать файл.
# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла, который мы получим на выходе(зашифрованного) и ключ(ключем будет уроваень сдвига).
# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на выходе(расшифрованного) и ключ.
import os.path
import string


def have_mistake_on_entering(file_from, file_to, key):
    if file_from == file_to:
        print('file\'s names the same')
        return True
    if len(file_from) < 3 or len(file_to) < 3:
        print('file\'s name should be more then 2 charts')
        return True
    try:
        int(key)
    except ValueError:
        print('key is not number')
        return True
    if int(key) > 26 or int(key) < -26:
        print('key should be in range -26 till 26')
        return True
    if not os.path.isfile(f'{file_from}.txt'):
        print('file is not find')
        return True
    # try:
    #     with open(f'{fileFrom}.txt', 'r') as file:
    #         file.read()
    # except FileNotFoundError:
    #     print('file is not find')
    #     return True

    return False


def crypt_file(file_from, file_to, key, encrypt):
    with open(f'{file_from}.txt', 'r') as fileFrom,\
            open(f'{file_to}.txt', 'w') as fileTo:
        file_content = fileFrom.read()
        file_result = crypt_string(file_content, key, encrypt)
        fileTo.write(file_result)


def crypt_string(text, key, encrypt):
    alphabet = string.ascii_letters + string.digits
    dic_alp = {v: i for i, v in enumerate(alphabet)}
    result = ''
    for s in text:
        t = dic_alp.get(s)
        if t == None:
            result += s
        else:
            n = t + key if encrypt else t - key
            n = n + 61 if 0 > n else n
            n = n - 61 if n > 61 else n
            result += alphabet[n]

    return result


def exit_program(text):
    print(text)
    exit()


while True:
    user_chose = input('Do you want to encrypt or decrypt the file?\n'
                      'e - encrypt, d - decrypt, s - stop program\n'
                      'Enter your answer here (e/d/s)...').lower()
    if user_chose == 'e' or user_chose == 'd' or user_chose == 's':
        break
    else:
        print('Please be careful next time in entering.')

if user_chose == 's':
    exit_program('See you next time.')

if user_chose == 'e':
    check = True
    while check:
        user_file_from = input('Please enter the file name to encrypt...')
        user_file_to = input('Please enter a new file name to result...')
        user_key = input('Please enter the key...')
        check = have_mistake_on_entering(user_file_from, user_file_to, user_key)

    crypt_file(user_file_from, user_file_to, int(user_key), True)
    exit_program('File encrypt successfully.\nSee you next time.')

if user_chose == 'd':
    check = True
    while check:
        user_file_from = input('Please enter the file name to decrypt...')
        user_file_to = input('Please enter a new file name to result...')
        user_key = input('Please enter the key...')
        check = have_mistake_on_entering(user_file_from, user_file_to, user_key)

    crypt_file(user_file_from, user_file_to, int(user_key), False)
    exit_program('File decrypt successfully.\nSee you next time.')

