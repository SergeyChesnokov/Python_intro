# Задача 10 - Про переворачивание монеток
list_c = [ ]
n = int(input('Введите число монеток: n = '))
print('Введите 1 - орел, 0 - решка:  ')
for i in range(n):
    coin = int(input(f'   {i+1} монета:   '))
    while coin != 1 and coin != 0:
        print('1 or 0 only!!!')
        coin = int(input(f'   {i+1} монета:   '))
    list_c.append(coin)
print(list_c)
eagle_count = 0
tails_count = 0
for i in range(n):
    if list_c[i] == 1:
        eagle_count += 1
    else:
        tails_count += 1
print(f'Итого {eagle_count} орлов и {tails_count} решек')
if eagle_count < tails_count:
    s = eagle_count
else:
    s = tails_count
print(s)
