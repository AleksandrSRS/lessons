#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
moscow_x = sites['Moscow'][0]
moscow_y = sites['Moscow'][1]
london_x = sites['London'][0]
london_y = sites['London'][1]
paris_x = sites['Paris'][0]
paris_y = sites['Paris'][1]
# print(moscow_x, moscow_y)
moscow_london = ((moscow_x - london_x)**2 + (moscow_y - london_y)**2)**0.5
moscow_paris = ((moscow_x - paris_x)**2 + (moscow_y - paris_y)**2)**0.5
london_paris = ((london_x - paris_x)**2 + (london_y - paris_y)**2)**0.5

distances = {
    'Москва - Лондон': moscow_london,
    'Москва - Париж': moscow_paris,
    'Лондон - Москва': moscow_london,
    'Лондон - Париж': london_paris,
    'Париж - Москва': moscow_paris,
    'Париж - Лондон': london_paris,
}
pprint(distances)




