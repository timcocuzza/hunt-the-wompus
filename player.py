class Player:

    @staticmethod
    def move(grid):
        # Find the player's current position (denoted by 1)
        player_position = None
        for i, row in enumerate(grid):
            if 1 in row:
                player_position = (i, row.index(1))
                break

        if player_position is None:
            print("Player not found on the grid!")
            return grid

        where_move = input("Where do you want to move? (up, down, left, or right) ")
        print(f"You entered {where_move}")

        move_x, move_y = 0, 0

        move_dict = {
            "left": (0, -1),
            "right": (0, 1),
            "up": (-1, 0),
            "down": (1, 0)
        }

        if where_move in move_dict:
            move_x, move_y = move_dict[where_move]
        else:
            print("Invalid input, try again")
            return grid

        # Calculate new player position
        new_x = player_position[0] + move_x
        new_y = player_position[1] + move_y

        # Check if the move is valid
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] != "W":  # Assume 'W' is a wall
                # Move player to the new position
                grid[player_position[0]][player_position[1]] = 0  # Clear old position
                grid[new_x][new_y] = 1  # Set new player position
                print(f"Moved to ({new_x}, {new_y})")
            else:
                print("Wowza!! That's a wall!")
        else:
            print("Invalid move, try again")

        return grid

    @staticmethod
    def shoot_arrow(grid):
        # Find the player's current position (denoted by 1)
        player_position = None
        for i, row in enumerate(grid):
            if 1 in row:
                player_position = (i, row.index(1))
                break

        if player_position is None:
            print("Player not found on the grid!")
            return grid

        # Ask for the direction to shoot the arrow
        direction = input("Where do you want to shoot the arrow? (up, down, left, right): ")
        print(f"You entered {direction}")

        # Set the movement based on direction
        move_x, move_y = 0, 0
        shoot_dict = {
            "left": (0, -1),
            "right": (0, 1),
            "up": (-1, 0),
            "down": (1, 0)
        }

        if direction in shoot_dict:
            move_x, move_y = shoot_dict[direction]
        else:
            print("Invalid input, try again")
            return grid

        # Shoot the arrow in the specified direction (only one step)
        arrow_x, arrow_y = player_position[0] + move_x, player_position[1] + move_y

        # Check if the arrow's target position is valid and within bounds
        if 0 <= arrow_x < len(grid) and 0 <= arrow_y < len(grid[0]):
            # Leave a 4 where the arrow lands
            grid[arrow_x][arrow_y] = 5
            print(f"Arrow shot to ({arrow_x}, {arrow_y})")
        else:
            print("Arrow shot out of bounds!")

        return grid
