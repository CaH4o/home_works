# *************************ЗАДАЧА №1******************************
# 1. Создать несколько словарей всеми известными вам методами;
# 2. Выбрать один словарь и добавить в него 5 пар ключ-значение;
# 3. Удалить одну пару используя инструкцию del;
# 4. Удалить еще одну пару используя другой метод;
# 5. Выбрать еще один словарь и наполнить его;
# 6. Расширить словарь из 5-го пункта словарем из 2-го;
# 7. Вывести все ключи последнего словаря;
# 8. Вывести все значения последнего словаря;
# 9. Создать поверхностную копию получившегося словаря;
# 10. Очистить расширенный словарь.

#1
dicrinory_1 = {'One': 1, 'Two': 2}
dicrinory_2 = {}.fromkeys(['LastName', 'FirstName', 'PatronName'])
dicrinory_3 = dict(gender='male', age=33)
dicrinory_4 = dict().fromkeys(['ID_1', 'ID_2', 'ID_3'], 'non')
print(dicrinory_1)
print(dicrinory_2)
print(dicrinory_3)
print(dicrinory_4)

#2
dicrinory_1.update({'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Nine': 9})
print(dicrinory_1)

#3
del dicrinory_1['Nine']
print(dicrinory_1)

#4
dicrinory_1.popitem()
print(dicrinory_1)

#5
dicrinory_2['LastName'] = 'Erikh'
dicrinory_2['FirstName'] = 'Maria'
dicrinory_2['PatronName'] = 'Remark'
dicrinory_2.update(dict(gender='male', age=72))
print(dicrinory_2)

#6
dicrinory_2.update(dicrinory_1)
print(dicrinory_2)

#7
print(dicrinory_2.keys())

#8
print(dicrinory_2.values())

#9
dicrinory_5 = dicrinory_2.copy()
print(dicrinory_5)

#10
dicrinory_2.clear()
print(dicrinory_2)

# *************************ЗАДАЧА №2******************************
# 1. Создать словарь store и наполнить его (товар: колличество на складе);
# 2. Создать словарь price и наполнить его (товар: цена за единицу товара);
# 3. Поиграть с колличеством товара (симитировать его покупку клиентами(убавлять количество на складе)
#  и пополнение на складе(увеличивать количнство на складе));
# 4. Добавить несколько новых товаров на склад и прайс соответственно;
# 5. Создать словарь total_price в котором будет подсчитана общая стоимость по каждому
# товару;
# 6. Создать словарь total_store в котором будет подсчитанo общее количество товаров на складе;
# 7. Создать словарь total в котором будет подсчитанa общая стоимость всей продукции на складе.

#1
store = {'apple': 32, 'strawberry': 12, 'tomato': 21}

#2
price = {'apple': 0.24, 'strawberry': 0.5, 'tomato': 0.34}

#3
store['apple'] -= 10
store['strawberry'] += 17

#4
newItem = [['potato', 120, 0.16], ['muesli', 44, 0.8]]
store.update({newItem[0][0]: newItem[0][1]})
price.update({newItem[0][0]: newItem[0][2]})
store.update({newItem[1][0]: newItem[1][1]})
price.update({newItem[1][0]: newItem[1][2]})
print(store)
print(price)

#5
total_price = {
    'apple': store['apple'] * price['apple'],
    'strawberry': store['strawberry'] * price['strawberry'],
    'tomato': store['tomato'] * price['tomato'],
    'potato': store['potato'] * price['potato'],
    'muesli': store['muesli'] * price['muesli']
}
print(total_price)

#6
total_store = sum(store.values())
print(total_store)

#7
total = sum(total_price.values())
print(total)

# *************************ЗАДАЧА №3******************************
# Даны словари такого типа:
#
# hero = {
#     'health': 100,
#     'gold': 500,
#     'mana': 100,
#     'artefacts': ['knife', 'shield', 'helmet'],
#     'backpack': ['mana', 'tablet']
# }
#
# enemy_hero = {
#     'health': 150,
#     'gold': 300,
#     'mana': 100,
#     'artefacts': ['boots', 'ring'],
#     'backpack': ['meet']
# }
#
# 1. Ваш hero прокачался и его здоровье должно удвоится;
# 2. Герой подобрал новый артефакт 'sword';
# 3. Герой участвовал в схватке и потерял 50 здоровья;
# 4. Что бы восполнить здоровье он воспользовался таблеткой из своего рюкзака;
# 5. Герой зашел в ломбард и купил новую таблетку за 50 золота,
# также продал свой нож за 100 и купил кольчугу за 200;
# 6. Герой схватился в бою с другим героем, в итоге потерял всю ману и половину
# здоровья, но забрал все золото, артефакты и содержимое рюкзака героя противника.

hero = {
    'health': 100,
    'gold': 500,
    'mana': 100,
    'artefacts': ['knife', 'shield', 'helmet'],
    'backpack': ['mana', 'tablet']
}

enemy_hero = {
    'health': 150,
    'gold': 300,
    'mana': 100,
    'artefacts': ['boots', 'ring'],
    'backpack': ['meet']
}

print(hero)
print(enemy_hero)

#1
hero['health'] *= 2
print(hero)

#2
hero['artefacts'].append('sword')
print(hero)

#3
hero['health'] -= 50
print(hero)

#4
hero['backpack'].remove('tablet')
hero['health'] += 50
print(hero)

#5
hero['backpack'].append('tablet')
hero['gold'] -= 50
hero['artefacts'].remove('knife')
hero['gold'] += 100
hero['artefacts'].append('mail')
hero['gold'] -= 200
print(hero)

#6
hero['health'] //= 2
hero['mana'] = 0
enemy_hero['health'] = 0
enemy_hero['mana'] = 0
hero['gold'] += enemy_hero['gold']
enemy_hero['gold'] = 0
hero['artefacts'].extend(enemy_hero['artefacts'])
enemy_hero['artefacts'].clear()
hero['backpack'].extend(enemy_hero['backpack'])
enemy_hero['backpack'].clear()

print(hero)
print(enemy_hero)
del enemy_hero