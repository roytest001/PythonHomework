from sys import exit
from random import randint

def death():
    quips = ["You died.  You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]

    print quips[randint(0, len(quips)-1)]
    exit(1)


def central_corridor():

    action = raw_input("> ")

    if action == "shoot!":
      
        return 'death'

    elif action == "dodge!":
        return 'death'

    elif action == "tell a joke":
        return 'laser_weapon_armory'

    else:
        print "DOES NOT COMPUTE!"
        return 'central_corridor'

def laser_weapon_armory():
    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
    guess = raw_input("[keypad]> ")
    guesses = 0

    while guess != code and guesses < 10:
        print "BZZZZEDDD!"
        guesses += 1
        guess = raw_input("[keypad]> ")

    if guess == code:
        return 'the_bridge'
    else:
        return 'death'


def the_bridge():
    action = raw_input("> ")

    if action == "throw the bomb":
        return 'death'

    elif action == "slowly place the bomb":
        return 'escape_pod'
    else:
        print "DOES NOT COMPUTE!"
        return "the_bridge"

def escape_pod():

    good_pod = randint(1,5)
    guess = raw_input("[pod #]> ")


    if int(guess) != good_pod:
        return 'death'
    else:
        exit(0)
