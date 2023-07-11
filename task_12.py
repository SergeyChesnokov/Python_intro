# Задача 12
s = int(input('х + у = '))
p = int(input('х * у = '))
x = 1
while x < s:
    y = s - x
    if x * y == p:
        print(f'   x = {x},   y = {y}')
    x += 1
print('end')
