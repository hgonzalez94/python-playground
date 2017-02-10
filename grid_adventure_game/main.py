items = ["frostmourne", "doomhammer", "ashbringer", "ashes of a'lar", "lightsaber"]

game_grid = [
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ]

# Prints the game grid by looping through the game grid array
def print_game_grid():
    print "GAME GRID"
    for row in game_grid:
        for column in row:
            print column,
        print ""

# reads the items inside the item array
def read_items():
    for item in items:
        print "Found {0} in collection of items".format(item)
        if item == "doomhammer":
            print "BRUH WE OUT HERE ON THE ENHANCE!!!"

    print ""
    print "the first item is {0}, the second item is {1}".format(items[0], items[1])

# asks the user to input shit
def ask_user_input():
    print "Please enter something (enter q to quit)"
    while 1:
        var = raw_input("")
        if var == "q":
            print "Good bye fam"
            break
        print "You entered {0}".format(var)

# calls the read_items funciton
read_items()

# calls the print_game_grid function
print_game_grid()

# calls the ask_user_input function
ask_user_input()
