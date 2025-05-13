class Player:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_position = [0, 0] 

    def move(self, grid):
        where_move = input("Where do you want to move? (up, down, left, or right) ")
        print(f"You entered {where_move}")

        move_x, move_y = 0, 0

        move_dict = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }

        if where_move in move_dict:
            move_x, move_y = move_dict[where_move]
        else:
            print("Invalid input, try again")
            return grid

        new_x = self.player_position[0] + move_x
        new_y = self.player_position[1] + move_y

        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
            if grid[new_x][new_y] != "W":
                self.player_position = [new_x, new_y]
                print(f"Moved to {self.player_position}")
            else:
                print("Wowza!! That's a wumpus!!!!")
        else:
            print("Invalid move, try again")

        return grid

    def shoot(self):
        ****