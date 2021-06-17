# Реализуйте шифратор и дешифратор по шифру Цезаря.
# Спросить пользователя, что он хочет сделать - зашифровать или расшифровать файл.
# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла, который мы получим на выходе(зашифрованного) и ключ(ключем будет уроваень сдвига).
# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на выходе(расшифрованного) и ключ.
import os.path
import string


def haveMistakeOnEntering(fileFrom, fileTo, key):
    if fileFrom == fileTo:
        print('file\'s names the same')
        return True
    if len(fileFrom) < 3 or len(fileTo) < 3:
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
    if not os.path.isfile(f'{fileFrom}.txt'):
        print('file is not find')
        return True
    # try:
    #     with open(f'{fileFrom}.txt', 'r') as file:
    #         file.read()
    # except FileNotFoundError:
    #     print('file is not find')
    #     return True

    return False



def cryptFile(fileFrom, fileTo, key, encrypt):
    with open(f'{fileFrom}.txt', 'r') as fileFrom,\
            open(f'{fileTo}.txt', 'w') as fileTo:
        fileContent = fileFrom.read()
        fileResult = cryptString(fileContent, key, encrypt)
        fileTo.write(fileResult)


def cryptString(str, key, encrypt):
    alphabet = string.ascii_letters + string.digits
    dicAlp = {v: i for i, v in enumerate(alphabet)}
    result = ''
    for s in str:
        t = dicAlp.get(s)
        if t == None:
            result += s
        else:
            n = t + key if encrypt else t - key
            n = n + 61 if 0 > n else n
            n = n - 61 if n > 61 else n
            result += alphabet[n]

    return result



def exitProgram(text):
    print(text)
    exit()


while True:
    userChose = input('Do you want to encrypt or decrypt the file?\n'
                      'e - encrypt, d - decrypt, s - stop program\n'
                      'Enter your answer here (e/d/s)...').lower()
    if userChose == 'e' or userChose == 'd' or userChose == 's':
        break
    else:
        print('Please be careful next time in entering.')

if userChose == 's':
    exitProgram('See you next time.')

if userChose == 'e':
    check = True
    while check:
        userFileFrom = input('Please enter the file name to encrypt...')
        userFileTo = input('Please enter a new file name to result...')
        userKey = input('Please enter the key...')
        check = haveMistakeOnEntering(userFileFrom, userFileTo, userKey)

    userKey = int(userKey)
    cryptFile(userFileFrom, userFileTo, userKey, True)
    exitProgram('File encrypt successfully.\nSee you next time.')

if userChose == 'd':
    check = True
    while check:
        userFileFrom = input('Please enter the file name to decrypt...')
        userFileTo = input('Please enter a new file name to result...')
        userKey = input('Please enter the key...')
        check = haveMistakeOnEntering(userFileFrom, userFileTo, userKey)

    userKey = int(userKey)
    cryptFile(userFileFrom, userFileTo, userKey, False)
    exitProgram('File decrypt successfully.\nSee you next time.')

