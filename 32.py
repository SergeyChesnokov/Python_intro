

# Задача 32
#    ---Найти индексы элементов, значения которых не выходят за рамки диапазона---

import random
n = int(input('Задайте длинну массива: N = '))
lst = [random.randint(-9, 9) for i in range(n)]
print(lst)
upper = int(input('Введите верхнюю границу диапазона: '))
lower = int(input('Введите нижнюю границу диапазона: '))

res = []
for i in range(n):
    if lower <= lst[i] <= upper:
        res.append(i)

print(res)