# lab

# 1. Сгенерировать строку состоящую из алфавитов в маленьком и большом регистрах, а также цифр от 0 до 9.
# Результат сохранить в переменную.
# 2. Вывести первый символ из созданной строки.
# 3. Вывести последний символ из созданной строки.
# 4. Создать новую строку состоящую из трёх первых и трёх последних символов строки созданной в первом пункте.
# Результат сохранить в переменной.
# 5. Вывести первые 8 символов из строки созданной в первом пункте.
# 6. Найти индекс символа "H" в строке созданной в первом пункте.
# 7. Посчитать количество символов в строке созданной в первом пункте.
# 8. В строке созданной в первом пункте заменить символ "A" на номер своего телефона.
# 9. Вывести строку в обратном порядке.
# 10. Вставить в центр строки Ваше имя.
# 11. Вырезать из созданной строки Ваше имя и сохранить в переменной.
import string

#1
s = string.ascii_lowercase + string.ascii_uppercase + string.digits
print(s)
#2
print(s[0])
#3
print(s[-1])
#4
bes = f'{s[:3]}{s[-3:]}'
print(bes)
#5
print(s[:8])
#6
print(s.find('H'))
#7
print(len(s))
#8
print(s.replace('A','38090000000'))
#9
print(s[::-1])
#10
l1 = int(len(s)/2)
l2 = int(len(s)/2*-1)
name = 'OleksandrTertyshnyk'
ns = f'{s[:l1]}{name}{s[l2:]}'
print(ns)
#11
print(f'{ns[ns.find(name):ns.find(name)+len(name)]}')
