def game():
    print("Welcome in Tic Tac Toe game!")

    sign = input("Choose a sign to start a game: ")

    result = check_sign(sign)

    if result == 'X':
        start(sign, 'O')
    else:
        start(sign, 'X')


def check_sign(sign):
    s = sign

    legal = ['X', 'O']

    is_legal = False

    if sign == legal[0]:
        is_legal = True
    elif sign == legal[1]:
        is_legal = True
    else:
        is_legal = False

    if is_legal:
        return s
    else:
        s = input("Invalid sign. Please type the correct option: X or O ")
        check_sign(s)


def start(sign, opp_sign):

    positions = ["", "", "", "", "", "", "", "", ""]

    turn(sign)

    pos = input("Enter the position")

    if not pos.isdecimal():
        pos = input("Please enter correct value")
    else:
        positions[pos]


def turn(player_sign, positions):

    print("")
    print("|     |      |      |")
    print(f"|  {positions[0]}   |   {positions[1]}   |  {positions[2]}    |")
    print("|     |      |      |")
    print("+++++++++++++++++++++")
    print("|     |      |      |")
    print(f"|  {positions[3]}   |   {positions[4]}   |   {positions[5]}   |")
    print("|     |      |      |")
    print("++++++++++++++++++++++")
    print("|     |      |      |")
    print(f"|  {positions[6]}   |   {positions[7]}   |   {positions[8]}   |")
    print("|     |      |      |")
    print("")


game()
