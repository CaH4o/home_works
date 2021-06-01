# Создать переменную var1;
# Проверить тип переменной var1 используя функцию type();
# Перезаписать переменную var1 изменив тип хранящегося в ней значения;
# Проверить тип переменной var1 используя функцию type();
# Провести сложение переменной var1 c самой собой и записать результат в переменную var2;
# Создать переменную pi в которой сохранить значение числа ∏;
# Перезаписать переменную pi округлив значение до 2 знаков после запятой;
# Возвести переменную pi в 5-ую степень и найти целую часть от деления на 3;
# Умножить переменную pi на любое число и найти остаток от деления на 2;
# Создать переменную rand_float1 и записать в нее случайное значение в отрезке от 0 до 1;
# Создать переменную rand_float2 и записать в нее случайное значение в отрезке от 0 до 1;
# Создать переменную rand_digit1 и записать в нее случайное значение в отрезке от 10 до 40;
# Создать переменную rand_digit2 и записать в нее случайное значение в отрезке от -40 до 40 c
# шагом 5;
# Создать переменную rand_choice и записать в ней случайное число из объекта range;
# Найти максимальное значение из созданных выше переменных и записать в
# переменную max_result;
# Найти минимальное значение из созданных выше переменных округлить значение до 3-ох
# знаков после запятой и записать в переменную min_result;
# Создать случайную выборку из 10 чисел используя объект range в отрезке от 10 до 1000
# с шагом 25.
import math
import random

var1 = 1
print(type(var1))

var1 = 1.
print(type(var1))

var2 = var1 + var1
print(var2)

pi = math.pi
print(pi)

print(round(pi, 2))

print(pi ** 5 // 2)

print(pi * 5 % 2)

rand_float1 = random.random()
print(rand_float1)

rand_float2 = random.random()
print(rand_float2)

rand_digit1 = random.randrange(10, 40)
print(rand_digit1)

rand_digit2 = random.randrange(-40, 40, 5)
print(rand_digit2)

rand_choice = random.sample(range(10, 100, 5), 1)
#rand_choice = random.sample(random.choice([12,213,123,1,65, 565, 564]), 1)
print(rand_choice)

max_result = max(rand_digit1, rand_digit2, rand_float1, rand_float2)
print(max_result)

min_result = round(min(rand_digit1, rand_digit2, rand_float1, rand_float2),3)
print(min_result)

print(random.sample(range(10, 1000, 25), 10))