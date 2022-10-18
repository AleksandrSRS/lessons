# -*- coding: utf-8 -*-
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# sd.resolution = (601, 601)
# x1 = 0
# y1 = 50


# for i in range(x1, 601, 10x1):
#     point_1 = sd.get_point(i, y1)
#     point_2 = sd.get_point(i, y2)
#     sd.line(start_point=point_1, end_point=point_2, color=969696, width=4)
#     for j in range(x1, 601, y1/2):
#         point_3 = sd.get_point(x1, j)
#         point_4 = sd.get_point(y2, j)
#         sd.line(start_point=point_3, end_point=point_4, color=969696, width=4)

y1 = 50
y2 = 0

for y in range(12):
    x1 = 0
    x2 = 100

    if (y % 2) == 0:
        x1, x2 = x1 - 50, x2 - 50
    for x in range(6):
        sd.lines(point_list=(sd.get_point(x1, y2),
                                 sd.get_point(x1, y1),
                                 sd.get_point(x2, y1),
                                 sd.get_point(x2, y2)),
                     closed=True,
                     color=969696,
                     width=2)
        x1 = x1+100
        x2 = x2+100
    y1 = y1+50
    y2 = y2+50
sd.pause()