# Tic-tac-toe

def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


#  функция проверки условия выйгрыша
def win_condition(pole_, sim):
    for element in pole_:
        if element == [sim, sim, sim]:
            return True
    for i in range(3):
        if [pole_[0][i], pole_[1][i], pole_[2][i]] == [sim, sim, sim]:
            return True
    if [pole_[0][0], pole_[1][1], pole_[2][2]] == [sim, sim, sim]:
        return True
    if [pole_[0][2], pole_[1][1], pole_[2][0]] == [sim, sim, sim]:
        return True
    return False

# функция отрисовки игрового поля
def print_pole(pole_):
    print("    0  1  2")
    print("0   {}  {}  {}".format(pole_[0][0], pole_[0][1], pole_[0][2]))
    print("1   {}  {}  {}".format(pole_[1][0], pole_[1][1], pole_[1][2]))
    print("2   {}  {}  {}".format(pole_[2][0], pole_[2][1], pole_[2][2]))

# функция хода игрока
def hod(player_):
    proverka(pole, player_)
    print_pole(pole)
    fig = 'x' if player_ == 1 else 'o'
    if win_condition(pole, fig):
        # print(f"Игрок {player} победил!")
        return True

# функция проверки ввода данных
def proverka(pole_, player_):
    while True:
        coord = input(f"Игрок {player_} ({'крестики' if player_ == 1 else 'нолики'}"
                      f") введите координаты поля (строка столбец) ").split()

        if not (coord[0].isdigit()) or not(coord[0].isdigit()):
            print("Введите числа")
            continue

        L = list(map(int, coord))
        if len(L) != 2:
            print("Введите 2 координаты")
            continue

        stroka, stolbez = L[0], L[1]

        if all([0 <= stroka <= 2, 0 <= stolbez <= 2]):
            if pole_[stroka][stolbez] == ' ':
                fig = 'x' if player_ == 1 else 'o'
                pole[stroka][stolbez] = fig
                break
            else:
                print("В данном месте уже есть фигура. Повторите ввод")
        else:
            print("Координаты введены неверно. Повторите ввод")

    return True


# основной блок выполнения программы
pole = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# print("Игра крестики - нолики")
greet()
print("Начало игры")
player = 1
counter = 0
while True:
    if hod(player):
        print(f"Игрок {player} победил!")
        break
    else:
        counter += 1
        if counter == 9:
            print("Ничья")
            break
        if player == 1:
            player = 2
        else:
            player = 1


print("Игра окончена")
print(":)")