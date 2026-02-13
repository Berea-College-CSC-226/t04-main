######################################################################
# Author: Scott Heggen  # Don't change me this time!
# Username: heggens     # Don't change me this time!
#
# Assignment: T04: Adventure in Gitland
#
# Purpose: To recreate a choose-your-own-adventure style game
# by refactoring T01.
#
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
#
# This new version will take advantage of functions, as well as
# demonstrate the value of git as a tool for collaborating.
######################################################################
# Acknowledgements:
#   Original Author: Scott Heggen
#
######################################################################
import random
from time import sleep

DELAY = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!


def start_story():
    """
    Introduction text for the story.
    Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(DELAY)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(DELAY * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(DELAY)
    return user


def end_story(user):
    """
    This is the ending to the story.
    Don't modify this function, either.

    :param user: the user's name
    :return: None
    """
    print(
        "Congratulations, " +
        user +
        ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(DELAY * 5)
    print("Now go play again.")


def kill_if_dead(is_alive):
    """
    Simple function to check if you're dead

    :param is_alive: A boolean value representing livelihood.
    :return: None
    """
    if not is_alive:
        quit()


###################################################################################
###################################################################################

def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """

    direction = input(
        "Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(DELAY)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(DELAY)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(DELAY * 2)
        print("He eats you. You are delicious.")
        return False     # kill the user!
    else:
        # Neutral choice
        print(
            '''You're in another part of the cave. It is equally dark, and equally uninteresting. 
            Please get me out of here!''')
        sleep(DELAY)
    return True       # User survives all other scenarios


###################################################################################
###################################################################################
###################################################################################

def team_1_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_2_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_3_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_4_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_5_adv(username):
    """
    https://docs.google.com/document/d/1dzAfok-haJ2YMxQP-wVvN76Y-88vlwHmhbum4cHUhDc/edit?usp=sharing
    Jayden Fleming
    Artem Kurasov
    :return: Bool
    """

    alive_team_5 = True

    print("After your previous adventure, you seek another path.")
    print("You're walking up the side of a mountain, desiring the title of 'Greatest Adventurer'...")
    sleep(DELAY)
    print("Legends say that those who climb the mountain never return.")
    sleep(DELAY)

    input("Press Enter to roll for dexterity:")
    roll_value = random.randrange(2)

    if roll_value == 0:
        sleep(DELAY * 3)
        print("Nothing happens! You carry on walking up the mountain....")
    else:
        sleep(DELAY * 3)
        print("Oh no! You tripped on a vine! Like an idiot!")
        sleep(DELAY)
        print("You fall hundreds of meters to the depths of the Underground onto a bed of yellow flowers.")
        sleep(DELAY)
        print("You, somehow still alive, look around to see the smiling face of a particularly stupid-looking flower.")
        sleep(DELAY)
        print('??????: "Howdy! I\'m FLOWEY. FLOWEY the FLOWER! Hmmm... You\'re new to the UNDERGROUND, aren\'tcha? Golly, you must be so confused. \nSomeone ought to teach you how things work around here! I guess little old me will have to do."')
        sleep(DELAY)
        print("What do you want to do?")
        sleep(DELAY)
        while True:
            try:
                choice_flowey = input("\n\tA:Stomp on the stupid flower \n\tB:Accept its suspicious offer \n\tC:Decline its suspicious offer (trust me, bro)\n\t")
                choice_flowey = choice_flowey.lower()
                if choice_flowey == "a":
                    sleep(DELAY * 3)
                    print("You killed it.")
                    sleep(DELAY)
                    print(username, ", you are a meanie, and you killed it...")
                    sleep(DELAY)
                    print("You are evil and I don't trust you")
                    sleep(DELAY)
                    print("Flowey might have been a father of over fifteen thousand seeds. (true--look it up)")
                    sleep(DELAY)
                    print("Go away, be ashamed")
                    sleep(DELAY)
                    print("You moved on with your adventure...somehow. With no remorse.")
                    sleep(DELAY * 3)
                    break
                elif choice_flowey == "b":
                    sleep(DELAY * 3)
                    print("You accepted the flower's offer.")
                    sleep(DELAY)
                    print("(I can't believe you trusted it.)")
                    sleep(DELAY)
                    print("FLOWEY: \"REALLY? You accept my offer?\" ")
                    sleep(DELAY)
                    print("FLOWEY: \"Let me show you defend yourself in this world.\" ")
                    sleep(DELAY)
                    print("You enter into a fight with the stupid-yellow flower, where it taught you how to navigate the UNDERGROUND.")
                    sleep(DELAY)
                    print("You now, feeling prepared to FIGHT some monsters, go on your merry way throughout the UNDERGROUND.")
                    sleep(DELAY * 3)
                    break
                elif choice_flowey == "c":
                    sleep(DELAY * 3)
                    print("You rejected the offer.")
                    sleep(DELAY)
                    print("He is mad.")
                    sleep(DELAY)
                    print("You are scared")
                    sleep(DELAY)
                    print("You. Are. In. Danger.")
                    sleep(DELAY)
                    print("FLOWEY: \"DIE.\"")
                    sleep(DELAY)
                    print("The ground shakes. This flower, a fifth of your size, extends from beneath you in all directions. \nGiant pinchers made of flesh and teeth form from within an overgrown mass of stupid-yellow flowers and sit on either side of you. \nPinchers which, with the force of fifteen-thousand flowers, slam shut.")
                    sleep(DELAY)
                    alive_team_5 = False
                    break
                else:
                    sleep(DELAY * 3)
                    print("Please choose ONLY a,b,c")
            except ValueError:
                print(" ")

    if not alive_team_5:
            print("Woops. You died. Bummer.")
            sleep(DELAY * 3)

    return alive_team_5

###################################################################################


def team_6_adv(username):
   pass
   # TODO Add your code here

###################################################################################


def team_7_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_8_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_9_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_10_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_11_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_12_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def main():
    """
    The main function, where the program starts. No modifications are needed here!
    :return: None
    """

    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story()
    for i in range(len(paths)):
        is_alive = paths[i](user)  # Runs each function in the paths list
        kill_if_dead(is_alive)

    end_story(user)


if __name__ == "__main__":
    main()