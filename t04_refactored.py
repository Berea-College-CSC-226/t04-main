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
from operator import truediv

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

    if is_alive is not None and is_alive == False:
        quit()

###################################################################################

def scott_adventure(username):
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

def team_1_adv(username):
    """
    https://docs.google.com/document/d/1CpA6AyTEu6KLumAtVBWUhpw5lc3oJrjbbiS-z4GUpRY/edit?userstoinvite=yukikaleg8106@gmail.com&sharingaction=manageaccess&role=writer&tab=t.0#heading=h.f6tumop9n7at
    Yuki Fukushima
    Ryan Hensley
    :return: None
    """
    direction = input(
        "You bump your head into a wall. You feel your way around, you have two choices, left or right.  [Left/Right]: ")

    if direction == "Left":
        # Good choice
        print("You safely leave the cave.")
        sleep(DELAY)
        return True
    elif direction == "Right":
        # Neutral choice
        print("You fall into a pit. You have another chance of life. ")
        sleep(DELAY)
    else:
        print("You're confused.")
        print("An invalid direction makes you bump your head into a wall again.")
        sleep(DELAY)
        print("You died from a concussion.")
        return False

    direction = input("You find yourself at a crossroad. You can go left or right. [Left/Right]: ")

    if direction == "Left":
        # Good choice
        print("You find a town full of dwarfs that are willing to help you find your way out.")
        return True
    elif direction == "Right":
        # Bad choice
        print("You get trapped by the land around you and suffocated.")
        return False
    else:
        print("You're confused. ")
        print("An invalid direction makes you bump your head into a wall.")
        sleep(DELAY)
        print("You died from a concussion.")
        return False

###################################################################################
def team_2_adv(username):
    """
    https://docs.google.com/document/d/1zJS_Cxg4Jzp9z_NxLQ-2PFlvlQb04wrgZ4HA5WF6wFM/edit?usp=sharing
    Michael Damdinsuren
    Aryan Sehrawat
    """

    direction = input("Which direction would you like to go? [East/West]: ")

    if direction == "East":
        # Good choice!
        x = input("But don't worry, you're doing good, you've 2 paths in front of you. From first path you can hear the sound of water and the second path is full of Gems, make your choice wisely. Choose path 1 or 2?: ")

        sleep(DELAY)
        if x == "1":
            print("Great, you made it to the end of the story without dying! ")
            return True
        elif x == "2":
            print("Ah!!! there's the dragon of gems in front of you.")
            sleep(DELAY)
            print("You're dead(Loser😂)")
            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            return False

        else:
            print("Wrong input!")
            return True

    elif direction == "West":
        # Oh... Bad choice
        print("Oh there's some golden light to your left, can it be treasure or a way out")
        sleep(DELAY)
        print("and to your right it's still dark")
        y = input("Where will you go? right or left ")
        if y == "right":
            print("Wait, u see some light in front of you. ")
            sleep(DELAY)
            print("Booyah!! You made it to the end of the story without dying!")
            return True
        elif y == "left":
            print("OK sir you've jumped into the world of goblins")
            print("You're dead😂")
            sleep(DELAY)

            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            return False
        else:
            print("Wrong input!")
            return True

    else:
        x = input("You're in another part of the cave. Choose a path 1 or 2")
        if x == "1":
            print("Great, you made it to the end of the story without dying! ")
            return True
        elif x == "2":
            print("You fell in a pitt full of snakes")
            return False

        else:
            print("Wrong input!")
            return True



###################################################################################

def team_3_adv(username):
    """
    https://docs.google.com/document/d/1TFPxOsOpNuurpIvVdSkVr_I2v1vMKN9P40k_3U-St7E/edit?usp=sharing
    Mensah Derrick
    Mach R. Garang
    """
    direction = input("Which direction would you like to pass the ball? [Infront/Behind/To your left/To your right]")
    shoot = input("Which direction are you shooting the ball? [top post/Bottom corners]")

    dead = False
    if direction == "In front":
        print("Oh no, the defenders got the ball")
        dead = True

    elif direction == "Behind":
        print("Good job accurate pass to teammate")
        print("Your teammate holds the ball for too long and losses it")
        dead = True

    elif direction == "To your left":
        print("OMG!!!! WORLD CLASS PASS")
        print("Your teammate on the left wing got the ball")
        print("He's on the run, driving the ball forward")
        print("He is about to get tackled, and chops the ball to the inside of the feild and keeps driving")
        print("He sees you running into the 18 box and crossing it to you")
        print("You execute a phenomenal touch and are about to shoot")

        if shoot == "top post":
            sleep(DELAY)
            print("GOALLLLLLLLLLLLLLLLLLL!!!!!!!")

        else:
            print("Oh no the keeper caught the ball")
            return False
    else:
        print("Oh no, the defenders got the ball")

    if dead:
        print("Too bad your opponent got the ball and scored")
        print("YOU LOST ):")
    return True

###################################################################################

def team_4_adv(username):

    """
    https://docs.google.com/document/d/1ajIEehJiAZWTx5_dBGmj6-X5o7O4Kn2U8uJ5jeZpCj4/edit?usp=sharing
    Andre Booker
    Gabriella Sloboh
    :return: none
    """
    # TEAM 4

    from time import sleep

    delay = 3.0
    #initialize behind_tree...?
    behind_tree = True
    dead = False


    username = input("What is your name?")

    print(username, "is walking through the forest")
    sleep(delay)
    print("You see a bunch of people doing some sort of ritual around a campfire")
    print("You have many choices to make")
    sleep(delay)
    print("Type ""A"" if you would like to hide behind a tree.")
    print("Type ""B"" if you would like to make direct contact.")
    print("Type ""C"" if you would like to turn around.")
    sleep(delay)
    direction = input("What are you going to do in this situation?")

    if direction == "A":
        print("You hide behind a tree and watch from afar.")
        sleep(delay - 1.0)
        print("While you are behind the tree you overhear them talking about eating people")
        print("But for some reason there is an axe beside the tree you are hiding behind?")
        sleep(delay - 1.0)
        print()
        print("Type ""A"" if you want to grab the axe and make contact")
        print("Type ""C"" if you would like to go home.")
        behind_tree = input("Do you want to grab the axe and make direct contact or go home?")


    elif direction == "B":
        print("You confronted them, and then they instantly kill you!")


    elif direction == "C":
        print("You turn around a go home")
        dead = True

    if behind_tree == "A":
        print("You go up to them and chop their heads off with axe.")
        print("Congrats you survived!")
        dead = True

    elif behind_tree == "C":
        print("You turn around a go home")
        dead = True


    if dead == True:
        print("They turned out to be cannibals and they eat you.")
    elif dead == False:
        print("You are really smart, you weren't taking any chances of dying.")

###################################################################################

def team_5_adv(username):
    pass

###################################################################################

def team_6_adv(username):
    "Makayla and Elom"
    "https://docs.google.com/document/d/1IoGqIzwUB8Dhl-79Neu_qzU8yA1AHIAmnMEAtU1ljX8/edit?tab=t.0#heading=h.t96g5g4oo0q4"
    is_valid_choice = True
    is_alive = True
    direction = input("What sort of direction are you taking? Backward/Forward/Right/Left: ")
    if direction == "Backward":
        is_valid_choice = True
        print("You are dead!, that is a no go zone can you change the direction.")
        print("Buddy, I am warning you that you are gonna be dead if you do not change that direction.")
        print("Last time, my friend Victor was eaten by the wolf in the same forest, trust me take my warning seriously")
        print("Berea College computer science students want to joke with their CS prof by not completing their assignments on time...opps! I am lost")
        is_alive = False

    elif direction == "Forward":
        print("Things will be even more harder, get up!")
        print("There is a Lion and Tiger that will eat, you have to start running")
        print("Mach and Victor planned this game way back years ago and now its getting more and more fun, hahahahahah!!!!")

    elif direction == "Right":
        print("Things will be even more tougher get up !")
        print(" Why dont you liten you damn kid!")

    elif direction == "Left":
        print("You will not come out of this the same *ominous music*")
        is_alive = False

    else:
        is_valid_choice = False
        print(" Invalid")


    print(" The world has ended successfully")
    print(" And we have also finished the assignment and now looking forward to a nice lunch with Victor ")
    if not is_valid_choice:
        print("\nGame Over: You didn't choose a valid direction.")
        return False
    elif not is_alive:
        print("\nThe world has ended. You did not survive.")
        return False
    else:
        print("\nYou survived the turn!")
        return True

###################################################################################

def team_7_adv(username):
    pass

###################################################################################

def team_8_adv(username):
    pass

###################################################################################

def team_9_adv(username):
    pass

###################################################################################

def team_10_adv(username):
    pass

###################################################################################

def team_11_adv(username):
    pass

###################################################################################

def team_12_adv(username):
    pass


###################################################################################


def main():
    """
    Choose your own adventure!
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