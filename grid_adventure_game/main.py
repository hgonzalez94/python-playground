items = ["frostmourne", "doomhammer", "ashbringer", "ashes of a'lar", "lightsaber"]

def read_items():
    for item in items:
        print "Found {0} in collection of items".format(item)

    print ""
    print "the first item is {0}, the second item is {1}".format(items[0], items[1])

read_items()
