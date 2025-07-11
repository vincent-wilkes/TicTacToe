board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

turnnumber = 2
player = 'Spieler-X'
target = "X"

def check_win(board, target):
    #check rows for win
    rows_match = any(row == [target] * 3 for row in board)

    #check columns for win
    cols_match = any([board[0][i], board[1][i], board[2][i]] == [target] * 3 for i in range(3))

    #check diagonals for win
    diag1 = [board[0][0], board[1][1], board [2][2]]
    diag2 = [board[0][2], board[1][1], board [2][0]]
    diags_match = diag1 == [target] * 3 or diag2 == [target] * 3

    return rows_match or cols_match or diags_match

while True:
    for row in board:
        print(row)

    turn = input(f"{player} Spiele deinen Zug indem du das Feld angibst in welches du spielen möchtest (Z.B. oben Mitte ist 0:1): ")
    for Sep in [',', ';', ':', '-', '.', ' ', '/']:
        if Sep in turn:
            turnlocation = list(map(int, turn.split(Sep)))
            break
    else:
        raise ValueError("Bitte gibt zwei Zahlen mit einem Trennzeichen wie ',' oder ':' ein.")

    if board[turnlocation[0]][turnlocation[1]] != ' ':
        print("Dieser Zug ist illegal!")
        break
    else:
        if turnnumber % 2 == 0:
            board[turnlocation[0]][turnlocation[1]] = 'X'
            player = 'Spieler-O'
            target = "X"

        else:
            board[turnlocation[0]][turnlocation[1]] = 'O'
            player = 'Spieler-X'
            target = "O"

        turnnumber = turnnumber + 1

        if check_win(board, target):
            if turnnumber % 2 == 0:
                player = "Spieler-O"
            else:
                player = "Spieler-X"
                
            print(f"Herzlichen Glückwunsch {player} du hast gewonnen!")
            for row in board:
                print(row)
            break
            
        elif turnnumber == 11:
            print("Das Spiel ist Unentschieden ausgegangen!")
            for row in board:
                print(row)
            break
