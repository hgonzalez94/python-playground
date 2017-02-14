my_array = ["some", "shit", "goes", "in", "here"]
print "You are printing the first item in this array: {0}".format(my_array[0])

# this is what is known as a dictionary. It's similar to arrays but uses a key, value system.
my_dictionary = {"key": "value",
                 "meme": "harambe"}
print "You are printing what ever is stored in the key 'meme' in this dictionary: {0}".format(my_dictionary["meme"])

game_responses_dictionary = {"phillip": "creator",
                             "thomas": "the tank engine",
                             "42": "the meaning of life"}


def start_game():
    print "Welcome to the text Game we talked about, that will help you catch up while I wrap up my tech shit, Python Edition"
    begin_asking_questions()

def begin_asking_questions():
    print "Please enter something (enter q to quit)"
    while 1: # while loops continue while a condition is true. Since 1 is always true, it will loop forever until the loop breaks.
        var = raw_input("") # pythons way of asking people for input, and then storing what ever you input, into a variable. In this case, it stores it to var.
        if var == "q": # check if what you entered is the letter 'q' to end the game
            print "Good bye fam" # good bye message
            break # ends the loop

        if var == my_dictionary["meme"]: # checking to see if what you entered is = to harambe, since harambe is stored in my_dictionary["meme"]
            print "Blessed be our lord and savior {0}".format(my_dictionary["meme"])

        print "You entered {0}".format(var) # prints out what ever the fuck you entered

        if var in game_responses_dictionary: # checks to see if what ever 'var' is, is a key inside of the dictionary
            print "key: {0} - value: {1}".format(var, game_responses_dictionary[var]) # print out what ever is stored in the dictionary, at var

start_game() # calls the start game method
