#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

table_code = goods['Стол']
table_item = store[table_code]
table_quantity1 = table_item[0]['quantity']
table_quantity2 = table_item[1]['quantity']
table_quantity = table_quantity1 + table_quantity2
table_price1 = table_item[0]['price']
table_price2 = table_item[1]['price']
table_cost = table_quantity1 * table_price1 + table_quantity2 * table_price2
print('Столов -', table_quantity, 'шт, стоимость', table_cost, 'руб')

sofa_code = goods['Диван']
sofa_item = store[sofa_code]
sofa_quantity1 = sofa_item[0]['quantity']
sofa_quantity2 = sofa_item[1]['quantity']
sofa_quantity = sofa_quantity1 + sofa_quantity2
sofa_price1 = sofa_item[0]['price']
sofa_price2 = sofa_item[1]['price']
sofa_cost = sofa_quantity1 * sofa_price1 + sofa_quantity2 * sofa_price2
print('Диванов -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

stool_code = goods['Стул']
stool_item = store[stool_code]
stool_quantity1 = stool_item[0]['quantity']
stool_quantity2 = stool_item[1]['quantity']
stool_quantity3 = stool_item[2]['quantity']
stool_quantity = stool_quantity1 + stool_quantity2 + stool_quantity3
stool_price1 = stool_item[0]['price']
stool_price2 = stool_item[1]['price']
stool_price3 = stool_item[2]['price']
stool_cost = stool_quantity1 * stool_price1 + stool_quantity2 * stool_price2 + stool_quantity3 * stool_price3
print('Стульев -', stool_quantity, 'шт, стоимость', stool_cost, 'руб')
# print(type(store[sofa_code]))




# stool_summ = sum(list(n['quantity'] for n in stool_item))
# print(stool_summ)
##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






