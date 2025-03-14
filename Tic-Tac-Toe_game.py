import sys
from random import choice
from random import randrange

def display(nested_list):

    grid = nested_list
    print('+-------+-------+-------+')

    for row in grid:
        print('|       |       |       |')
        print('|  ', row[0], '  |  ', row[1], '  |  ', row[2], '  |')
        print('|       |       |       |')
        print('+-------+-------+-------+')
    

def edit(player, nested_list):
    grid = nested_list
    check = True

    for row in grid:
        for i in range(3):
            if row[i] == player:
                row[i] = 'o'
                display(grid)
                check_won(grid)
                check_game_over(grid)

                empty_cells = [(r, c) for r in range(3) for c in range(3) if isinstance(grid[r][c], int)]

                if empty_cells:
                    r, c = choice(empty_cells)
                    grid[r][c] = 'x'
                    display(grid)
                    check_won(grid)
                    check_game_over(grid)
                return
    print("Cell already taken, please choose an empty cell.")

def check_won(nested_list):

    for row in nested_list:
        if row[0] == row[1] == row[2]:
            if row[0] == 'x':
                print('You lost')
                sys.exit()
            elif row[0] == 'o':
                print('You won')
                sys.exit()
                
    diagonals = [(nested_list[0][0], nested_list[1][1], nested_list[2][2]), 
                (nested_list[0][2], nested_list[1][1], nested_list[2][0])]
    
    for diag in diagonals:
        if diag[0] != ' ' and diag[0] == diag[1] == diag[2]:
            if diag[0] == 'x':
                print('You lost')
            else:
                print('You won')
            sys.exit()
    else:
        for j in range(3):
            if nested_list[0][j] != ' ' and nested_list[0][j] == nested_list[1][j] == nested_list[2][j]:
                if nested_list[0][j] == 'x':
                    print('You lost')
                    sys.exit()
                elif nested_list[0][j] == 'o':
                    print('You won')
                    sys.exit()

def check_game_over(nested_list):

    symbols = {'x', 'o'}
    flat_list = {cell for row in nested_list for cell in row}
    if flat_list.issubset(symbols):
        print("Draw")
        sys.exit()

nested_list = [[1, 2, 3], [4, 'x', 6], [7, 8, 9]]
display(nested_list)

while True:
    try:
        player = int(input("Enter your move: "))
        if player in range(1, 10):
            edit(player, nested_list)
        else:
            print("Invalid move. Choose a number between 1 and 9.")
    except ValueError:
        print("Please enter a valid number.")
        

