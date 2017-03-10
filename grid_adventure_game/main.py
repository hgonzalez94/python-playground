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


#############Tim Homework Code#############
def ask_user_movement():
	print "Where do you want to go?"
	while 1:
		var = raw_input("")
		player_row = stats ["current_row"]
		player_column = stats ["current_column"]
		if var == "up" : 
			if player_row != 0:
				player_row -= 1
			
			else:
				print "You cant move that way you rascal!\n\n"

		if var == "down":
			if player_row != 9:
				player_row += 1

			else:
				print "You cant move that way you rascal!\n\n"
		
		if var == "right":
			if player_column != 9:
				player_column += 1

			else:
				print "You cant move that way you rascal!\n\n"

		if var == "left":
			if player_column != 0:
				player_column -= 1

			else:
				print "You cant move that way you rascal!\n\n"
		
		if var == "q" :
			break
		set_player_position(player_row, player_column)
		print_game_grid()

		print "You have entered the direction: {0} \n\n".format(var)
		##### use set_player_position to move character

############# GAME CODE HERE ##############

stats = {"health": 69,
         "attack": 420,
         "steps_moved": 0,
         "current_row": 0,
         "current_column": 0}

items = [
			{"item_name": "frostmourne", "item_damage": "100", "flavor_text": "frostmourne hungers"},
			{"item_name": "doomhammer", "item_damage": "12", "flavor_text": "still has some green jesus juice in it"},
			{"item_name": "ashbringer", "item_damage": "101", "flavor_text": "ooh! shiny!"},
			{"item_name": "ashes of a'lar", "item_damage": "0", "flavor_text": "its a fire bird, not a weapon"},
			{"item_name": "lightsaber", "item_damage": "1", "flavor_text": "really strong flashlight"},
		]

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

def start_game():
    reset_game_grid()
    game_grid[0][0] = "@"
    print_welcome_message()
    print_game_grid()

def print_welcome_message():
    print "Welcome to Tim's Game. Please be respectful and stay lit fam\n\n"

def set_player_position(row, column):
    reset_game_grid() # clear game grid
    game_grid[row][column] = "@" # set the player position on the game grid
    stats["current_row"] = row # set the row the player is at
    stats["current_column"] = column # set the column the player is at
    stats["steps_moved"] += 1 # make steps moved increase by 1

# sets every position in the game grid to a default '.'
def reset_game_grid():
    for i, value in enumerate(game_grid):
        for j, val in enumerate(game_grid[i]):
            game_grid[i][j] = "."

# Reduces player health. So far health is only reduced by 1 by default.
def take_damage():
    current_health = stats["health"]
    current_health -= 1
    stats["health"] = current_health
    print "Oh no, you took damage!"
    print_game_grid()

# Prints player stats
def print_stats():
    print "|",
    for key in stats:
        if key != "current_row" and key != "current_column": # only print out shit as long as its not the current_row or current_column key
            print key,
            print stats[key],
            print "|",
    # \n means a new line. I'm printing 2 lines here
    print "\n\n"

# Prints the game grid by looping through the game grid array
def print_game_grid():
    print_stats()
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
#print_game_grid()

# calls the ask_user_input function
#ask_user_input()

#dictionary_test()

#ask_user_input()

start_game()

ask_user_movement()