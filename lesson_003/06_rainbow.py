# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.resolution = (500, 500)

# step = 0
# width = 4
#
# for x in rainbow_colors:
#     point_1 = sd.get_point(50, 50 + step)
#     point_2 = sd.get_point(350, 450 + step)
#     sd.line(point_1, point_2, x, width=width)
#     step += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(200, -100)
def bubble(point, step):
    radius = 400
    for x in rainbow_colors:
        radius += step
        sd.circle(center_position=point, radius=radius, color=x, width=5)

bubble(point, 5)
sd.pause()
