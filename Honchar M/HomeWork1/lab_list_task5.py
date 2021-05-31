# ************************* ЗАДАЧА №5 ******************************
# This temporary string for GIT
# 1. Создать список с тремя вложенными случайными списками (каждый вложенный
# список должен состоять из 10 элементов);
# 2. Сделать так чтобы первые три элемента первого вложенного списка были равны
# последним трем элементам третьего вложенного списка и наоборот
# (значения должны поменяться местами);
# 3. Заменить второй вложенный список на список в котором первая половина
# значений будут взяты из первого вложенного списка, а вторая часть
# из третьего;
# 4. Объединить все три вложенных списка в один целый.

import random
from copy import deepcopy
# 1
print("# 1")
lister = list([random.sample((range(30, 3000)), 10)] +
            [random.sample((range(30, 3000)), 10)] +
            [random.sample((range(30, 3000)), 10)])
print('list_before=', lister)

# 2
print("# 2")
list2 = deepcopy(lister)
sublist_1 = list2[0][:3]
del list2[0][:3]
print('sublist_1=', sublist_1)
sublist_2 = list2[2][-3:]
del list2[2][-3:]
print('sublist_2=', sublist_2)
sublist_1, sublist_2 = sublist_2, sublist_1
print('sublist_1=', sublist_1)
print('sublist_2=', sublist_2)
print('list_after2=', list2)
list2[2].extend(sublist_2)
list2[0].reverse(), sublist_1.reverse()
list2[0].extend(sublist_1)
list2[0].reverse()
print('result=', list2)

# 3
print("# 3")
list3 = deepcopy(lister)
list3_sum02 = list3[0] + list3[2]
print("list3_sum02=", list3_sum02)
list3[1].clear()
print()
list3[1].extend(list3_sum02)
print('result=', list3)

# 4
print("# 4")
print(lister[0]+lister[1]+lister[2])

