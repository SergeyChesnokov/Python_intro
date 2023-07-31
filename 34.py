# Задача 34

#    --- Входные данные ---
# готовая фраза для удобства тестирования программы:
phrase = 'пара-ра-рам рэм-пум-пипом па-ра-па-дам ю-я-ё-ы.'
# # альтернативный вариант для ввода из командной строки:
# phrase = input('Введите фразу: ') 

#    --- Ход реешния ---
# Разобьем фразу на список слов в фразе по пробелу:
phrase = phrase.split(' ')
# а затем составим список той же размерности
# возвращающий число гласных в каждом слове
# если список состоит из одинаковых значений,
# тогда, согласно условию задачи "ритм есть"
vowel_counter_list = []
total_vowel_set = {'а', 'э', 'ы', 'о', 'у',
                   'я', 'е', 'и', 'ё', 'ю'}
for word in phrase:
    vowel_counter = 0
    for letter in word:
        if letter in total_vowel_set:
            vowel_counter += 1
    vowel_counter_list.append(vowel_counter)

# print(vowel_counter_list) # Выводит число гласных к слове, что удобно
# при тестировании программы

# проверяем элементы списка на равенство:
flag = True
for i in range(1, len(vowel_counter_list)):
    if vowel_counter_list[i] != vowel_counter_list[0]:
        print('Пам парам')
        flag = False
        
if flag:
    print('Парам пам-пам')
