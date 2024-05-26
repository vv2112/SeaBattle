# Шаг 1. Расстановка кораблей пользователя и компьютера
# создаём два массива расстановки кораблей

# Шаг 2. Вывести оба поля на экран.

import random

boats = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

pole1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

pole2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def printpole(pole1, pole2):
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


def place_ship(field, width, height, x1, y1):
    for iy in range(y1 - 1, y1 + height + 1):
        for ix in range (x1 - 1, x1 + width + 1):
            if iy < 0 or iy >= 10 or ix < 0 or ix >= 10:
                continue
            if field[iy][ix] != 0:
                return False
    for iy in range(y1, y1 + height):
        for ix in range (x1, x1 + width):
            field[iy][ix] = 2
    return True

def place_ship_rnd(field, width, height):
    while True:
        x1 = random.randint(0, 10 - width)
        y1 = random.randint(0, 10 - height)
        is_placed = place_ship(field, width, height, x1, y1)
        if is_placed:
           break


def autofill(field):
    for boat in boats:
        if boat == 1:
            place_ship_rnd(field, 1, 1)
        else:
            horizont = random.randint(0,1)
            if horizont:
                place_ship_rnd(field, boat, 1)
            else:
                place_ship_rnd(field, 1, boat)



# def rand_coordinate(boat):
#     # h - положение корабля, рандом, горизонтальный (true) или вертикальный (false)
#     global h
#     global xold
#     global y
#     h = bool(random.getrandbits(1))
#     xold = random.randint(0, 9)
#     y = random.randint(0, 9)
#     if h:
#         if xold + boat + 1 > 10:
#             rand_coordinate(boat)
#     else:
#         if y + boat + 1 > 10:
#             rand_coordinate(boat)
#

#
# def autofill():
#     while True:
#         for boat in boats:
#             rand_coordinate(boat)
#             print(xold, y, h, boat)
#             if h:
#                 for i in range(boat):
#                     pole2[xold + i][y] = boat   #2
#                 for i in range(boat):
#                     if xold + i - 1 == -1:
#                         continue
#                     elif xold + i + 1 > 10:
#                         continue
#                     elif y + i - 1 == -1:
#                         continue
#                     elif y + i + 1 == 11:
#                         continue
#                     #if i == 0:
#                         #for yy in range (0, 2):
#                             #pole2[xold + i - 1][y + yy - 1] = 5
#                     #pole2[xold + i - 1][y - 1] = 5
#                     #pole2[xold + i - 1][y + 1] = 5
#                     #if i == boat:
#                         #for yy in range (0, 2):
#                             #pole2[xold + i + 1][y + yy - 1] = 5
#
#             else:
#                 for i in range(boat):
#                     pole2[xold][y + i] = boat #2
#
#         #когда все корабли расставленны - конец цикла
#         break

if __name__ == '__main__':
    autofill(pole1)
    autofill(pole2)
    printpole(pole1, pole2)