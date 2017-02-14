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
        print "You entered {0}".format(var) # prints out what ever the fuck you entered

start_game() # calls the start game method
