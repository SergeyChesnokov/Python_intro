# Задача 12
s = int(input('х + у = '))
p = int(input('х * у = '))
x = 1
while x < s:
    y = s - x
    if x * y == p and x <= 1000 and y <= 1000:
        print(f'   x = {x},   y = {y}')
        break
    x += 1
print('end')
