
def move(self, grid):
    where_move = input("Where do you want to move? (up, down, left, or right) ")
    print("You entered " + where_move)
    
    move_x, move_y = 0, 0

    if where_move == "left":
        move_x = -1
    elif where_move == "right":
        move_x = 1
    elif where_move == "up":
        move_y = -1
    elif where_move == "down":
        move_y = 1
    else:
        print("Invalid input, try again")
        return grid
    
    new_x = self.player_position[0] + move_x
    new_y = self.player_position[1] + move_y

    if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
        if grid[new_x][new_y] != "W":
            self.player_position = [new_x, new_y]
        else:
            print("Wowza!! That's a wumpus!!!!")
    else:
        print("Invalid move, try again")
    
    return grid

def shoot():
    **arrowcount
