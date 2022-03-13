import time

# terminal print commands
ANSI_CLEAR_SCREEN =  lambda: print('\n' * 150)
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u""
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"



# print ship with colors and leading spaces
def Animation_print(position):
    print('\n' * 100)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + " ____")
    print(sp + "|    |")
    print(sp + "|O  O|")
    print(sp + "|  L |")
    print(sp + "| UU |")
    print(sp + "|    |")
    print(sp + "|    |")
    print(sp + "|    |")
    print(sp + "|    |")
    print(sp + " ____")
    print(RESET_COLOR)

# ship function, iterface into this file
def animation():

    # loop control variables
    start = 0  # start at zero
    distance = 75  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        Animation_print(position)  # call to function with parameter
        time.sleep(.1)

animation()