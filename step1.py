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

def printpole(pole1, pole2):   # Печатает оба поля
    print('      А Б В Г Д Е Ж З И К             А Б В Г Д Е Ж З И К')
    print('    |--------------------           |--------------------')
    for y in range(0, len(pole1)):     #  заполняет цифры слева от поля
        if y < 9:
            n = ' '
        else: n = ''
        print(y+1, n, '| ', end='')
        for x in range(0, len(pole1[y])):
            print(pole1[y][x], end=' ')
        print('     ', end=' ')
        print(y+1, n, '| ', end='')
        for x2 in range(0, len(pole2[y])):
            print(pole2[y][x2], end=' ')
        print()


def place_ship(field, width, height, x1, y1):       # Размещает корабль в указанном поле с указанными координатами.
    for iy in range(y1 - 1, y1 + height + 1):
        for ix in range (x1 - 1, x1 + width + 1):
            if iy < 0 or iy >= 10 or ix < 0 or ix >= 10:    # Проверка на выход за границы поля
                continue
            if field[iy][ix] != 0:      # Проверка на то, что клетки размещения корабля и на 1 клетку вокруг не заняты.
                return False
    for iy in range(y1, y1 + height):              # Размещение "корабля" на поле
        for ix in range (x1, x1 + width):
            field[iy][ix] = 2
    return True

def place_ship_rnd(field, width, height):          # Генерация координаты случайного размещения корабля на поле
    while True:
        x1 = random.randint(0, 10 - width)
        y1 = random.randint(0, 10 - height)
        is_placed = place_ship(field, width, height, x1, y1)    # вызов процедуры размещения корабля
        if is_placed:                            # Если результат вызова процедуры True, то разрываем бесконечный цикл.
           break                                 #TODO А если не смогли разместить, то что???


def autofill(field):
    for boat in boats:
        if boat == 1:
            place_ship_rnd(field, 1, 1)
        else:
            horizont = random.randint(0,1)                    # Генерация случайного положения горизонт/вертикаль
            if horizont:
                place_ship_rnd(field, boat, 1)
            else:
                place_ship_rnd(field, 1, boat)




if __name__ == '__main__':
    autofill(pole1)
    autofill(pole2)
    printpole(pole1, pole2)
