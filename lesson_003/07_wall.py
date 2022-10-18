# -*- coding: utf-8 -*-
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (601, 600)
x1 = 1
y1 = 1
x2 = 1
y2 = 600

for i in range(0, 601, 100):
    point_1 = sd.get_point(i, y1)
    point_2 = sd.get_point(i, y2)
    sd.line(start_point=point_1, end_point=point_2, color=969696, width=4)
    for j in range(0, 601, 50):
        point_3 = sd.get_point(x1, j)
        point_4 = sd.get_point(y2, j)
        sd.line(start_point=point_3, end_point=point_4, color=969696, width=4)
# step = 0

# for y in range(0, 1000, 50):
#     y1 = y + 50
#     step -= 50
#     for x in range(step, 1000, 100):
#         x1 = x + 100
#         point = sd.get_point(x, y)
#         point1 = sd.get_point(x1, y1)
#         sd.rectangle(point, point1, color=sd.random_color(), width=0)

# width сделал 0 специально, чтобы получились красивые кирпичики

sd.pause()