import random as r

board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

opponents = {

    "player": 1,
    "bat": 2,
    "wompus": 3,
    "hole": 4

}

def main():

    init_chars()
    pretty_print(board)
    hazard_check(board, "hole")
    hazard_check(board, "bat")
    hazard_check(board, "wompus")





def init_chars():
    
    wompus_init = [r.randint(0, 4), r.randint(0, 4)]
    board[wompus_init[0]][wompus_init[1]] = 3

    while True:
        bat_init = [r.randint(0, 4), r.randint(0, 4)]
        if board[bat_init[0]][bat_init[1]] == 0:  
            board[bat_init[0]][bat_init[1]] = 2
            break

    while True:
        player_init = [r.randint(0, 4), r.randint(0,4)]
        if board[player_init[0]][player_init[1]] == 0:  
            board[player_init[0]][player_init[1]] = 1
            break
    
    while True:
        hole_init = [r.randint(0, 4), r.randint(0,4)]
        if board[hole_init[0]][hole_init[1]] == 0:  
            board[hole_init[0]][hole_init[1]] = 4
            break

def pretty_print(grid):
    for row in grid:
        for column in row:   
            print("*", end="   ") if column == 1 else print("0", end="   ")
        print("\n")


def hazard_check(board, opponent):
    
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                if i > 0 and board[i - 1][j] == opponents[opponent]:
                    print(f"{opponent} is near")
                if i < rows - 1 and board[i + 1][j] == opponents[opponent]:
                    print(f"{opponent} is near")
                if j > 0 and board[i][j - 1] == opponents[opponent]:
                    print(f"{opponent} is near")
                if j < cols - 1 and board[i][j + 1] == opponents[opponent]:
                    print(f"{opponent} is near")
main()
