# Задача 24
# На момент решения задачи функции map(), filter() и enumerate() ещё не были пройдены.
# Пришлось изобретать велосипед)))

#   -----Генерация списка-----

from random import randint
n = int(input('\nВведите число кустов: N = '))
lst = [randint(0, 12) for i in range(n)] # Рабочий список
scr = [f'{lst[i]}({i+1})' for i in range(n)] # Список для вывода на экран (с номерами кустов)
print(f'\n{scr}\n')

#    -----Основное решение-----

r = len(lst)
lst1 = [lst[i-2] + lst[i-1] + lst[i] for i in range(r)]
m = max(lst1)
print(f'Основное решение:    max = {m}\n')

#  -----Дополнительные решения-----

all_solutions = [f'{lst[i-1]}({i})' for i in range(r) if lst[i-2] + lst[i-1] + lst[i] == m]
# Либо:
# for i in range(r):
#     if lst[i-2] + lst[i-1] + lst[i] == m:
#         all_solutions.append(f'{lst[i-1]}({i})')
print(f'Все решения:    {all_solutions}\n')
