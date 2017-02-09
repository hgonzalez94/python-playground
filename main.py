greetings = ["Hey Tim", "What's Good Fam", "How's Life?"]

def show_greetings():
    for greeting in greetings:
        print (greeting)

def number_count():
    number = 0
    print "Your number is {0}".format(number)
    for i in range(0, 10):
        number+=1
        print "Your number is {0}".format(number)

print "We are executing the function 'show_greetings'"
print ""
show_greetings()

print "Now we are executing the function 'number_count'"
print ""
number_count()
