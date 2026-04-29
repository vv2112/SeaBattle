# Морской бой - полная игра

import random

boats = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
pole_player = []      # Поле игрока (с его кораблями)
pole_computer = []    # Поле компьютера (с его кораблями)
pole_player_shots = []   # Поле с выстрелами игрока по компьютеру
pole_computer_shots = [] # Поле с выстрелами компьютера по игроку

# Коды клеток:
# 0 = пусто
# 1 = промах (вода)
# 2 = корабль (не выстреленный)
# 3 = попадание
# 4 = потопленный корабль

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


def print_field_for_player(hidden_field, shots_field):
    """Печатает поле для игрока (враг = скрыто, свое = видно)"""
    print('      А Б В Г Д Е Ж З И К             А Б В Г Д Е Ж З И К')
    print('    |--------------------           |--------------------')
    for y in range(10):
        n = ' ' if y < 9 else ''
        print(f'{y+1} {n} | ', end='')
        
        # Своё поле
        for x in range(10):
            cell = hidden_field[y][x]
            if cell == 0: print('.', end=' ')
            elif cell == 2: print('■', end=' ')  # Корабль
            elif cell == 3: print('✕', end=' ')  # Попадание
            elif cell == 4: print('✕', end=' ')  # Потопленный
            else: print('.', end=' ')
        
        print('     ', end=' ')
        print(f'{y+1} {n} | ', end='')
        
        # Поле врага (выстрелы)
        for x in range(10):
            cell = shots_field[y][x]
            if cell == 0: print('.', end=' ')
            elif cell == 1: print('~', end=' ')  # Промах
            elif cell == 3: print('✕', end=' ')  # Попадание
            elif cell == 4: print('✕', end=' ')  # Потопленный


def printpole(pole1, pole2):   # Печатает оба поля (старая версия)
    print('      А Б В Г Д Е Ж З И К             А Б В Г Д Е Ж З И К')
    print('    |--------------------           |--------------------')
    for y in range(0, len(pole1)):
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
        if horizont: field[y1][x1+i] = 2
        else: field[y1+i][x1] = 2
    return True

def place_ship_rnd(field, boat):
    max_attempts = 1000
    attempts = 0
    while attempts < max_attempts:
        horizont = random.randint(0, 1)
        if horizont:
            x1 = random.randint(0, 10 - boat)
            y1 = random.randint(0, 10 - 1)
        else:
            x1 = random.randint(0, 10 - 1)
            y1 = random.randint(0, 10 - boat)
        is_placed = place_ship(field, boat, horizont, x1, y1)
        if is_placed:
            break
        attempts += 1
    return is_placed


def autofill(field):
    for boat in boats:
        place_ship_rnd(field, boat)


def shoot(field_ships, field_shots, x, y):
    """Выстрел по полю. Возвращает: 'попадание', 'промах', 'повтор' или 'ошибка'"""
    if x < 0 or x >= 10 or y < 0 or y >= 10:
        return 'ошибка'
    
    if field_shots[y][x] != 0:  # Уже стреляли в эту клетку
        return 'повтор'
    
    if field_ships[y][x] == 2:  # Есть корабль
        field_shots[y][x] = 3  # Попадание
        field_ships[y][x] = 3  # Отметим на поле кораблей
        return 'попадание'
    else:
        field_shots[y][x] = 1  # Промах
        return 'промах'


def get_player_move():
    """Получить ход от игрока"""
    letters = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ж': 6, 'З': 7, 'И': 8, 'К': 9}
    while True:
        try:
            move = input("Ваш ход (например: А1): ").upper().strip()
            if len(move) < 2:
                print("Неправильный ввод!")
                continue
            letter = move[0]
            number = int(move[1:]) - 1
            
            if letter not in letters or number < 0 or number >= 10:
                print("Координаты вне поля!")
                continue
            
            x = letters[letter]
            y = number
            return x, y
        except ValueError:
            print("Неправильный ввод! Используйте формат: А1")


def count_ship_cells(field_ships, x, y):
    """Проверить, потоплен ли корабль, если в него попали"""
    visited = set()
    
    def dfs(cx, cy):
        if (cx, cy) in visited:
            return 0
        if cx < 0 or cx >= 10 or cy < 0 or cy >= 10:
            return 0
        
        visited.add((cx, cy))
        
        if field_ships[cy][cx] == 2:  # Невредимая часть корабля
            return 1 + dfs(cx+1, cy) + dfs(cx-1, cy) + dfs(cx, cy+1) + dfs(cx, cy-1)
        return 0
    
    return dfs(x, y)


def is_ship_sunk(field_ships, x, y):
    """Проверить, потоплен ли корабль после выстрела"""
    # Пытаемся найти оставшиеся части корабля рядом
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10 and field_ships[ny][nx] == 2:
            return False  # Есть невредимые части
    return True


def mark_sunk_ship(field_ships, field_shots, x, y):
    """Отметить потопленный корабль и его окрестность"""
    visited = set()
    
    def dfs(cx, cy):
        if (cx, cy) in visited:
            return
        if cx < 0 or cx >= 10 or cy < 0 or cy >= 10:
            return
        
        visited.add((cx, cy))
        
        if field_ships[cy][cx] == 3 or field_ships[cy][cx] == 2:  # Часть корабля
            field_shots[cy][cx] = 4  # Отметим как потопленный
            dfs(cx+1, cy)
            dfs(cx-1, cy)
            dfs(cx, cy+1)
            dfs(cx, cy-1)
    
    dfs(x, y)


def count_alive_ships(field_ships):
    """Посчитать количество невредимых клеток кораблей"""
    count = 0
    for row in field_ships:
        for cell in row:
            if cell == 2:
                count += 1
    return count


def get_computer_move():
    """Компьютер выбирает случайный ход"""
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        # Можно сделать более умный ход, но пока просто случайный
        return x, y


def game_loop():
    """Основной игровой цикл"""
    init_field(pole_player)
    init_field(pole_computer)
    init_field(pole_player_shots)
    init_field(pole_computer_shots)
    
    print("=" * 60)
    print("МОРСКОЙ БОЙ")
    print("=" * 60)
    print("\nРасставляем корабли...")
    
    autofill(pole_player)
    autofill(pole_computer)
    
    print("\nКораблей расставлены!")
    print("\nПомощь:")
    print("  . = пусто")
    print("  ■ = ваш корабль")
    print("  ~ = ваш промах")
    print("  ✕ = попадание")
    
    player_turn = True
    
    while True:
        print("\n" + "=" * 60)
        print_field_for_player(pole_player, pole_player_shots)
        
        player_ships_left = count_alive_ships(pole_player)
        computer_ships_left = count_alive_ships(pole_computer)
        
        print(f"\nКораблей у вас: {player_ships_left} | Кораблей у компьютера: {computer_ships_left}")
        
        # Проверка на конец игры
        if player_ships_left == 0:
            print("\n" + "=" * 60)
            print("КОМПЬЮТЕР ВЫИГРАЛ!")
            print("=" * 60)
            break
        
        if computer_ships_left == 0:
            print("\n" + "=" * 60)
            print("ВЫ ВЫИГРАЛИ!")
            print("=" * 60)
            break
        
        if player_turn:
            print("\n>>> ВАШ ХОД <<<")
            x, y = get_player_move()
            
            result = shoot(pole_computer, pole_player_shots, x, y)
            
            if result == 'повтор':
                print("Вы уже стреляли в эту клетку!")
                continue
            elif result == 'ошибка':
                print("Ошибка координат!")
                continue
            elif result == 'попадание':
                print("✕ ПОПАДАНИЕ!")
                if is_ship_sunk(pole_computer, x, y):
                    mark_sunk_ship(pole_computer, pole_player_shots, x, y)
                    print("КОРАБЛЬ ПОТОПЛЕН!")
                else:
                    print("Корабль ранен!")
            else:  # промах
                print("~ промах")
                player_turn = False
        else:
            print("\n>>> ХОД КОМПЬЮТЕРА <<<")
            x, y = get_computer_move()
            
            # Проверяем, что компьютер не повторяет выстрел
            while pole_computer_shots[y][x] != 0:
                x, y = get_computer_move()
            
            result = shoot(pole_player, pole_computer_shots, x, y)
            
            letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
            coords = f"{letters[x]}{y+1}"
            
            if result == 'попадание':
                print(f"Компьютер стреляет в {coords} и ПОПАДАЕТ!")
                if is_ship_sunk(pole_player, x, y):
                    mark_sunk_ship(pole_player, pole_computer_shots, x, y)
                    print("Компьютер потопил ваш корабль!")
            else:  # промах
                print(f"Компьютер стреляет в {coords} и промахивается.")
                player_turn = True
        
        input("\nНажмите Enter для продолжения...")


if __name__ == '__main__':
    game_loop()
    printpole(pole1, pole2)
