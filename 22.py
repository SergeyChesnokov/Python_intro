# Задача 22

# Автоматический ввод:
# ------------------------------------------\\\
from random import randint                           # При использовании автоматического ввода
n = int(input('\nВведите натуральное число: n = '))  # для  создания  списков  рекоммендуется
lst1 = [randint(-25, 25) for i in range(n)]          # выбирать  значения  n и m  не менее 20,
m = int(input('Введите натуральное число: m = '))    # чтобы  количество общих элементов  было 
lst2 = [randint(-25, 25) for i in range(m)]          # достаточно  велико  для  сортировки. 
# -------------------------------------------///

# Ручной ввод:
# -------------------------------------------\\\
# lst1 = [i for i in input('Введите набор 1: ').split()]
# lst2 = [i for i in input('Введите набор 2: ').split()]
# -------------------------------------------///

print(f'\n{lst1}')
print(f'{lst2}\n')

lst1 = set(lst1)
lst2 = set(lst2)
print(f'\n{lst1}')
print(f'{lst2}\n')

set_int = lst1.intersection(lst2)
print(set_int)

lst = []
for i in range(len(set_int)):
        lst.append(min(set_int))
        set_int.remove(min(set_int))
print(f'{lst}\n')

