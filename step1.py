# Шаг 1. Расстановка кораблей пользователя и компьютера
# создаём два массива расстановки кораблей

# Шаг 2. Вывести оба поля на экран.


pole1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],]

pole2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],]


print('      А Б В Г Д Е Ж З И К             А Б В Г Д Е Ж З И К')
print('    |--------------------           |--------------------')
for i in range(0, len(pole1)):
    if i < 9:
        n = ' '
    else: n = ''
    print(i+1, n, '| ', end='')
    for i2 in range(0, len(pole1[i])):
        print(pole1[i][i2], end=' ')
    print('     ', end=' ')
    print(i+1, n, '| ', end='')

    for n2 in range(0, len(pole2[i])):
        print(pole2[i][n2], end=' ')
    print()