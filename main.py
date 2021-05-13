import os #потом будем чистить консоль

def grt():
    print("-------------------")
    print("  Добро пожаловать  ")
    print("       в игру       ")
    print("  крестики-нолики  ")
    print("-------------------")



def shw():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")

    for i, row in enumerate(field):
        print(f"  {i} | {' | '.join(row)} | ")
        print("  --------------- ")

    print()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


while True: # повторно играть: условие на 96-й строке
    grt()
    field = [[" "] * 3 for i in range(3)]
    count = 0

    while True:
        count += 1
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")
        shw()
        print(f"Ход {count}-й")
        print(" Ходит крестик!" if count % 2 == 1 else " Ходит нолик!")

        x, y = ask()

        field[x][y] = "X" if count % 2 == 1 else "0"

        if check_win():
            shw() # выводим поле с изображением победы
            break

        if count == 9:
            print(" Ничья!")
            break

        # чистим консоль (в PyCharm не работает)
        os.system('cls' if os.name == 'nt' else 'clear')
    if input('Если желаете сыграть еще - нажмите "y", если нет - нажмите "n"') == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        break
