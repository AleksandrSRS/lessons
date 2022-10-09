#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
first = my_favorite_movies.find(",")
second = my_favorite_movies[first+1:].find(",") + first + 1
end = my_favorite_movies.rfind(",")
end_2 = my_favorite_movies[:end].rfind(",")
print(first, second, end, end_2)
print("первый фильм:", my_favorite_movies[:first])
print("последний:", my_favorite_movies[end+1:-1])
print("второй:", my_favorite_movies[first+1:second])
print("второй с конца:", my_favorite_movies[end_2+1:end])