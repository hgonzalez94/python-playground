dictionary = {"key": "value",
              "another key": "another value",
              "harambe": "meme",
              "thanks": "obama"}


############# PRACTICE TEST CODE HERE #################
# asks the user to input shit
def ask_user_input():
    print "Please enter something (enter q to quit)"
    while 1:
        var = raw_input("")
        if var == "q":
            print "Good bye fam"
            break
        print "You entered {0}".format(var)
        
        # if what you entered, is in the dictionary as a key, print out something special
        if var in dictionary:
            print "Hey, looks like what you entered is: {0} and its the key that matches to value: {1}".format(var, dictionary[var])

        take_damage()


def dictionary_test(): 
    print "TESTING DICTIONARY"
    print "The value for the key: {0} is {1}".format("key", dictionary["key"])


############# END PRACTICE TEST CODE HERE ##############



############# GAME CODE HERE ##############

stats = {"health": 69,
         "attack": 420,
         "steps_moved": 0}

items = ["frostmourne", "doomhammer", "ashbringer", "ashes of a'lar", "lightsaber"]

monsters = [
                {"monster_name": "slime",  "health": "2", "damage": "2"},
                {"monster_name": "wolf",   "health": "5", "damage": "2"},
                {"monster_name": "spider", "health": "3", "damage": "1"},
           ]

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

def take_damage():
    current_health = stats["health"]
    current_health -= 1
    stats["health"] = current_health
    print "Oh no, you took damage!"
    print_stats()

def print_stats():
    print "|",
    for key in stats:
        print key,
        print stats[key],
        print "|",

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

############# END GAME CODE HERE ##############


############ CALLING STUFF ##############
# calls the read_items funciton
#read_items()

# calls the print_game_grid function
print_game_grid()

# calls the ask_user_input function
#ask_user_input()

dictionary_test()

ask_user_input()
