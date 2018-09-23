######################################################################
# Author: The Fall 2018 226 Class!
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

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False


def start_story():
    """
    Introduction text for the story. Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(delay)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(delay * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(delay)
    return user


def end_story(user):
    """
    This is the ending to the story. Don't modify this function, either.

    :param user: the user's name
    :return: None
    """
    print("Congratulations, " + user + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay*5)
    print("Now go play again.")


def kill_if_dead(dead):
    """
    Simple function to check if you're dead

    :param dead: A boolean value where false let's the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()

###################################################################################


def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """
    global dead             # You'll need this to be able to modify the dead variable
    direction = input("Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(delay)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(delay)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(delay*2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)


def team_1_adv():
    pass
    # TODO Add your code here


def team_2_adv():
    """
    Google Doc: https://docs.google.com/document/d/19jYjDRX_WR4pPynsAYmeglDpQWDvNVMDgYvd4EUWqm8/edit?usp=sharing
    Goes through the berea section of the story. Asks if you want to go to dining or go do homework.
    Choosing either will take you to two possibilities of being "dead" or being asked how much money you have.
    This choice then will make you "dead" or will continue on the "story" to the next function
    """
    global dead
    print()
    print()
    direction = input ("As a Berean, no matter where you end up, you have to constantly make this hard decision: Go to dining or Go do homework, what do you say? [Go to dining/Go do homework]")
    if direction == "Go to dining" or "go to dining":       # Good choice! asking if they want to go to dining
        print()
        print("you get tired of this trivial cave and leave and head to dining to meet up friends")
        print()
        sleep(delay*3)
    elif direction == "Go do homework" or "go do homework":  # Bad choice! asking if they want to do homework
        print()
        sleep(delay*3)
        print("You think you are making the right choice to conform to this capitalist world.")
        sleep(delay*3)
        print()
        print("When you, at heart, are a leftist Marxist")
        sleep(delay*3)
        print()
        print("You know you shouldn't be enslaved by the institution that is generally accepted in the form of")
        sleep(delay*3)
        print()
        print("'all american college'")
        sleep(delay*3)
        print()
        print("You graduate with a degree.")
        sleep(delay*3)
        print()
        print("Work an 8-5 job.")
        sleep(delay*3)
        print()
        print("Have two children.")
        sleep(delay*3)
        print()
        print("Get old.")
        sleep(delay*3)
        print()
        print("And, when sitting at your white wood porch, looking at your old pictures, quietly sob realizing...")
        sleep(delay*3)
        print()
        print("that you should have gone to the dining hall")
        sleep(delay*3)
        print()
        print("You die a victim of this machine.")
        print()
        print()
        dead = True
    else:                                                   #user inputs something other than the dining or homework asnwers
        sleep(delay)
        print()
        print("You are not a true Berean.")
        print()
        sleep(delay)
    if dead == True:                                        #end of the homework answer
        sleep(delay)
        print("Oh no. You are dead. Bye.")
        quit()

    money = int(input ("How much is your family income?"))   #ask what family income is
    if money < 30000:                                        #does the print if they asnwer with something below 30000
        sleep (delay)
        print()
        print("Berea, berea, beloved")
    elif money > 30000:                                      #does the print if they answer with something above 30000
        sleep(delay)
        print()
        print("you don't belong here")
        dead = True
    else:                                                    #catches any answers that are not the ones we want
        sleep(delay)
        print("illiterate. bye. *middle finger emoji* *clown emoji* *middle finger emoji*")
    if dead == True:
        print("go back to the centre college where you belong.")
        quit()

def team_3_adv():
    pass
    # TODO Add your code here


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():
    """
    Google doc: https://docs.google.com/document/d/1BzQqW9mFzMhzRlAyL1DkV31Ps5QJOwXgqQtEBJ4gJAI/edit?usp=sharing
    Team 5's refactored chapter
    Originally by Dunn & Dovranov , refactored by Jacob Hill, Bryan Epperson, Susan Coreas
    :return: None
    """
    # Dunn & Dovranov
    # Refactored by Team 5

    global dead

    direction = input("Where do you want to go?  [North/South/East/West]")

    if direction == "East" or direction == "east":
        # Bad Choice
        print("You followed the light and it led to another person that was lost.")
        print("Slowly approaching the other person you fall and they now know they are not alone.")
        print("You are now injured and the other person is leaving you because of the noise.")
        print("After they have left you fall asleep.")
        sleep(delay)
        print("You awaken to the noise of bear that is approaching closer to you.")
        print("Unfortunately, you can't walk and the bear is close to you.")
        print("The bear is hungry and is looking for a delicious meal.")
        print("The bear begins to eat you.")
        print("You have one more chance to live. You see a rock.")

        userinput = input("Can you grab it? [Yes/No]")

        if userinput == "Yes":
            print("You hit the bear and it runs off.")
        elif userinput == "No":
            print("The bear ate you.")
        else:
            print("The bear ate you.")

        dead = True

    elif direction == "West" or direction == "west":
        # Good choice
        print("You are walking in the dark and you stumble across something on the ground.")
        print("You bend over and pick it up.")
        print("It is a flashlight!")
        print("However, you are still in the dark but now you have a flashlight to see more with so you do not fall.")
        sleep(delay)

    elif direction == "North" or direction == "north":
        # Neutral choice
        print("You found a place to stay for the night until daytime.")
        sleep(delay)

    elif direction == "South" or direction == "south":
        # Neutral choice
        print("You found a place to stay for the night until daytime.")
        sleep(delay)

    else:
        print("That is not a direction! Please input a direction")
        team_5_adv()

    if dead == True:
        print("Oh no! You died. Try again by hitting the green play button.")
        quit()



def team_6_adv():
    """
    Team 6's refactored chapter.
    Originally by lovelle, refactored by lovelle.

    :return: None
    """

    global dead
    direction = input("Which direction would you like to go? [North/South/East/West] ")

    if direction == "East":
        # Good choice
        print()
        print("You come upon an underground lake, fed by a glistening stream.")
        print()
        print("The sound of the water soothes your troubled nerves.")
        sleep(delay)
        print()
    elif direction == "South":
        # Bad choice
        print()
        print("Ever so suddenly, you find yourself surrounded by ogres twice your size.")
        print("They realize you are harmless and you catch your breath. It seems they might let you pass...")
        sleep(delay * 5)
        print()
        print("They strike up a song, ready to continue on their way.")
        print("Oh, but how loud their voices are! And you aren't feeling so good...")
        sleep(delay * 5)
        print()
        print("The leader asks you to rank the quality of their singing, on a scale of 1 to 10.")
        rating = int(input("What do you say? Choose wisely; your life depends on it... "))
        print()
        if rating < 10:
            print("You fall to the ground, feeling the power of a cursed song. Looks like your time is up, friend.")
            dead = True
            sleep(delay)
            print()
        else:
            print("The ogre thanks you for the complement and sends you on your merry way.")
            sleep(delay)
            print()
    else:
        # Neutral choice
        print()
        print("Phew, you're still on solid ground. But still in the dark. Think fast!")
        sleep(delay)
        print()

    if dead == True:
        print("Oh no! You died. And what a shame it had to happen this way.")
        print("Better luck next time - try again by hitting the green play button!")
        quit()



def team_7_adv():
    pass
    # TODO Add your code here


def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():
    pass
    # TODO Add your code here


def team_10_adv():
    pass
    # TODO Add your code here


def team_11_adv():
    pass
    # TODO Add your code here


def westth_benningfield():
    """ inputs the room we were asked to refactor.
    link to our google doc: https://docs.google.com/document/d/11l9OqTJTGxCbiatW3S5czFA036_AvCPBq0RjwNz4eaA/edit?usp=sharing"""
    print()
    print('An eerie box lays before you, and for some reason you are drawn to it.')
    print()
    print('As you draw closer you hear a voice in your head...')
    print()
    print('"In order to receive the treasures of the box you must reveal your deepest and darkest secret"')

    choice = input('Will you reveal your secret? [Yes/No]')

    if choice == "Yes" or choice == "Y" or choice == "yes":
        secret = input('Speak now and reveal the truth.')
        print(secret)
        print("The box opens and you reach inside to retrieve your treasure...")
        sleep(delay)
        print()
        print('''It's a flower with petals made of fire and a note that says, "It's a me, copyright."''')
        sleep(delay)
        print()
        print('Confused by the note, you take your reward and move on.')
        print()
        sleep(delay)
    elif choice == "No" or choice == "N" or choice == "no":
        death = input('Will you open the box? [Yes/No]')
        if death == "Yes" or choice == "Y" or choice == "yes":
            print('You attempt to open the box but you become consumed by a deadly darkness that envelops your body.')
            print()
            print('You died. LOL')
            revive = input("would You like to restart")
            if revive == "Yes" or choice == "Y" or choice == "yes":
                riddle = input("What starts with 'e' ends with 'e' and contains one letter? ""[a/an]")

                if riddle == "envelope":
                    print("You live. Good job! However, you don't get the treasure.")
            if revive == "No" or choice == "N" or choice == "no":
                print("ah its your choice")
                quit()
        elif death == "No" or choice == "N" or choice == "no":
            print('You decide not to open the box.')
            print()
            print('You feel like you have avoided some mysterious danger but missed out on some sweet loot.')
    else:
        print("You walk away")
    pass
    # TODO Add your code here


def team_13_adv():
    # tori and jessie
    # https://docs.google.com/document/d/1oPzq92-44tG37zoKnEG_hnjtZtgnz1UUe1kYTGTp81A/edit?usp=sharing

    print()
    print("You find yourself on a cliff. There doesn't seem to be a path down. You chance a glance over the edge")
    print("Seems like a long way...")
    print()

    jump = input("What would you like to do?[jump/stay/parachute]")

    if jump == "jump" or jump == "Jump" or jump == "j" or jump == "J" or jump == " jump" or jump == " Jump" or jump == " j" or jump == "J":
        # bad choice
        print("You fall from the sky and land on your head...")
        sleep(delay)
        print("Your skull burst open and your brains spread everywhere")
        sleep(delay)
        print("Your chances of survival are zero.")
        sleep(delay * 2)
        print("You're dead meat.")
        print()
        dead = True
        if dead is True:
            print("You died, but at least you don't have to take 226 anymore. :)")
            quit()

    elif jump == "parachute" or jump == "Parachute" or jump == "p" or jump == "P" or jump == " parachute" or jump == " Parachute" or jump == " p" or jump == " P":
        # good choice
        print("You open your parachute at approximately 1000 feet and you avoid injury.")
        sleep(delay * 2)
        print("Congratulations, you passed your parachute test!")
        print()

    elif jump == "stay" or jump == "Stay" or jump == "s" or jump == "S" or jump == " stay" or jump == " Stay" or jump == " s" or jump == " S":
        print("You decided to stay. The wind is pretty fierce this high up.")

    else:
        print("What was that?")
        print()




def team_14_adv():
    pass
    # TODO Add your code here


def team_15_adv():
    pass
    # TODO Add your code here


def team_16_adv():
    pass
    # TODO Add your code here


def team_17_adv():
    pass
    # TODO Add your code here


def team_18_adv():
    pass
    # TODO Add your code here


def team_19_adv():
    pass
    # TODO Add your code here


def team_20_adv():
    pass
    # TODO Add your code here


def main():
    """
    The main function, where the program starts.
    :return: None
    """

    user = start_story()
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             westth_benningfield, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story(user)


main()
