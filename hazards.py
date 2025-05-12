import random

def touched_bat(grid):
    while True:
        new_location = (random.randint(0, 5), random.randint(0, 5))
        if new_location == 0:
            continue
        else:
            return new_location

def touched_hole():
    print("You fell down a hole. Game over.")

def touched_wompus():
    print("You have been attacked by the Wompus!")
