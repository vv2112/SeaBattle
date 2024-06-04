# Шаг 1. Расстановка кораблей пользователя и компьютера
# создаём два массива расстановки кораблей

# Шаг 2. Вывести оба поля на экран.

import random

boats = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
pole1 = []
pole2 = []


def init_field(field):
    for yy in range(10):
        line = []
        for xx in range(10):
            line.append(0)
        field.append(line)

def reset_field(field):
    for yy in range(len(field)):
        for xx in range(len(field[yy])):
            field[yy][xx] = 0


def printpole(pole1, pole2):   # Печатает оба поля
    #for i in range(10):
    #    print()
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


# def place_ship(field, width, height, x1, y1):       # Размещает корабль в указанном поле с указанными координатами.
#     for iy in range(y1 - 1, y1 + height + 1):
#         for ix in range (x1 - 1, x1 + width + 1):
#             if iy < 0 or iy >= 10 or ix < 0 or ix >= 10:    # Проверка на выход за границы поля
#                 continue
#             if field[iy][ix] != 0:      # Проверка на то, что клетки размещения корабля и на 1 клетку вокруг не заняты.
#                 return False
#     for iy in range(y1, y1 + height):              # Размещение "корабля" на поле
#         for ix in range (x1, x1 + width):
#             field[iy][ix] = 2
#     return True
def place_ship(field, ship, horizont, x1, y1):
    h = ship if not horizont else 1
    w = ship if horizont else 1
    for iy in range(y1 - 1, y1 + h + 1):
        for ix in range(x1 - 1, x1 + w + 1):
            if iy < 0 or iy >= 10 or ix < 0 or ix >= 10:
                continue
            if field[iy][ix] != 0:
                return False
    for i in range(ship):
        if horizont: field[y1][x1+i] = 2                                          # три варианта решения
        else: field[y1+i][x1] = 2

        # field[y1+(i if not horizont else 0)][x1 + (i if horizont else 0)] = 2    # второй вариант
        # field[y1+(i, 0)[horizont]][x1 + (0, i)[horizont]] = 2                      # третий вариант

    return True

def place_ship_rnd(field, boat):          # Генерация координаты случайного размещения корабля на поле
    while True:
        horizont = random.randint(0, 1)
        if horizont:
            x1 = random.randint(0, 10 - boat)
            y1 = random.randint(0, 10 - 1)
        else:
            x1 = random.randint(0, 10 - 1)
            y1 = random.randint(0, 10 - boat)
        is_placed = place_ship(field, boat, horizont, x1, y1)    # вызов процедуры размещения корабля
        if is_placed:                            # Если результат вызова процедуры True, то разрываем бесконечный цикл.
           break                                 #TODO А если не смогли разместить, то что???


def autofill(field):
    for boat in boats:
        place_ship_rnd(field, boat)




if __name__ == '__main__':
    init_field(pole1)
    init_field(pole2)
    autofill(pole1)
    printpole(pole1, pole2)
    reset_field(pole1)
    printpole(pole1, pole2)
