import random as r

board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

def main():

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

    print(board)

main()