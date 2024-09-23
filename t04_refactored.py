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



def start_story(delay):
    """
    Introduction text for the story.
    Don't modify this function.

    :param delay: float representing pauses in the program
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


def end_story(user, delay):
    """
    This is the ending to the story.
    Don't modify this function, either.

    :param user: the user's name
    :param delay: float representing pauses in the program
    :return: None
    """
    print(
        "Congratulations, " +
        user +
        ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay * 5)
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


def scott_adventure(username, delay):
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :param username: the name of the user
    :param delay: float representing pauses in the program
    :return: None
    """

    direction = input(
        "Which direction would you like to go, " + username + "? [North/South/East/West]")

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
        sleep(delay * 2)
        print("He eats you. You are delicious.")
        return False     # kill the user!
    else:
        # Neutral choice
        print(
            '''You're in another part of the cave. It is equally dark, and equally uninteresting. 
            Please get me out of here!''')
        sleep(delay)
    return True       # User survives all other scenarios


###################################################################################
###################################################################################
###################################################################################


def team_1_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_2_adv(username = "Scott", delay = 1.0):
    """
    https://docs.google.com/document/d/1P2oG3ls33RFbDiHRx_RqUnavHicq17E0QNQ90DO_nk4/edit?usp=sharing
    Caleb Tucker
    Kai Vaught
    :return: none
    """
    is_dead = False
    print("It's Wednesday morning. You wake up at 9:10am and see the sun through your window.")
    print("Suddenly, you realize that you are almost late for your CSC 226 class at 9:20am.")
    print("You know you need your morning coffee to get through the day, but you are almost late for class!")
    sleep(delay)
    decision = input("Coffee or class? ").lower()

    if decision == "coffee":
        print("You drink your coffee and run to class.")
        sleep(delay)
        print("You are late, and awake. But the instructor is also late so he doesn't know.")
        return True

    elif decision == "class":
        print("You manage to arrive to class at 9:20am.")
        sleep(delay)
        is_dead = True

    else:
        print("You couldn't make up your mind, so you were late. Your final score drops a letter grade. Ouch.")
        return True

    if is_dead:
        print("Although you made it to class on time, you cannot stay awake.")
        sleep(delay)
        print()
        print("In an attempt to wake you up, Caleb throws scalding McDonald's coffee in your face.")
        print("He accidentally kills you.")
        return False

###################################################################################


def team_3_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_4_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_5_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_6_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_7_adv(username = "pokitokog,melnichenkaa", delay = 1.0):
    """
    https://docs.google.com/document/d/1xjf1gnNMp4Dyr4_MjM-oRn7gzxW9Z4p4VG3_EWYA4vM/edit
    Galina Pokitko
    Aliaksandr Melnichenka
    :return: True if alive, False if dead
    """

    bridge = input("You come across three bridges do you want to take the [Left/Middle/Right] path?")

    if bridge == "Left":
        print("You walk across a stone pathway confronted with a beautiful waterfall at the end: [+5 inspiration]")
        sleep(delay)
        return True

    # if they go left: You come across a beautiful waterfall: [+5 inspiration]

    elif bridge == "Middle":
        print("You walk across a chasm and the wooden bridge breaks and you are about to fall: [THINK FAST]")
        sleep(delay)

        rope = float(input(
            "Quick! Catch yourself using a rope! Determine its length in feet by picking a number between [1] to [20]"))

        if rope > 13:
            print(
                "Phew! You managed to grab the rope just in time before the fall! Congratulations: [+5 Survival Skills]")
            return True
        else:
            print("Oh no! Your hand slips and you fal backwards into the chasm: [DEAD]")
            return False


    # elif they go middle: You walk across a chasm and the wooden bridge breaks and you fall: [DEAD]

    else:
        print("You walk safely across a plain bridge: [0 inspiration]")
        sleep(delay)
        return True
    # else they go right: You walk safely across a plain bridge: [0 inspiration]

    if dead:
        print("Oh no! You did not make it to the end: [GAME OVER]")
        return False

    # The following is the end of the story. Don't change this section, unless you really want to.
    print("Look at that! You made it to the end of the story without dying! ")
    print("Congratulations... now go play again and find an interesting way to perish. ")
    print("Try again by hitting the green play button.")

    return True


def team_8_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_9_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_10_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_11_adv(username, delay):
    """
    https://docs.google.com/document/d/1YOGdN09YEycwQEfGlS1LzdbXsjU7RXas1OybrXs8tDo/edit?usp=sharing
    Luis Olivas
    Puskar Chapagain
    :return: none
    """
    # TEAM 11
    direction = input("Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        print("The person gets closer to you. You get scared of them and, and if they may harm you")
        print()
        sleep(delay)
        print("You take a closer look. Oh look, it is just Dr. Scott Heggen, and he is trying to help you out!")
        print("Dr. Heggen helps you out, and you make it out of the cave!")
        sleep(delay)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(delay)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print("He eats you. You are delicious.")
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        return False
    else:
        # Neutral choice
        print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    return True
###################################################################################


def team_12_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_13_adv(username, delay):
    '''https://docs.google.com/document/d/1sKZjkZLcneOgKSvRHJKCQrmaeie3n3Okpfr3FIo-avQ/edit
    Charle Ryland
    Eber Lima
    SOURCE:
    https://stackoverflow.com/questions/39746427/expression-can-be-simplified-on-boolean-literal'''
    user_direction = input("You come at across three tunnels.... (Choose forward, left, or right): ")
    sleep(delay)

    if user_direction == "left" or user_direction == "Left":
        print("You hit a den a bear lives in...")
        sleep(delay)
        print("You get scared and the alert the bear!")
        sleep(delay)
        print("The bear then eats you...")
        sleep(delay)
        print("You have a chance to survive...")
        number_picked = input("The Eggmeister asks you to pick a number between 1 and 20.")
        number_picked = int(number_picked)
        if number_picked >= 14:
            sleep(delay)
            return True
        elif number_picked < 14:
            sleep(delay)
            return False

    elif user_direction == "right" or user_direction == "Right":
        sleep(delay)
        print("You find an exit and reach a hill that overlooks a waterfall")
        print("Everything seems peaceful.")
        return True
    else:
        print("You walk forward...")
        sleep(delay)
        print("Nothing happens...")
        return True


###################################################################################


def team_14_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_15_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################



def team_16_adv(username, delay):
    """ https://docs.google.com/document/d/14o_900GCeVZEadcvwv_15i2ZS8oINYH6bJigpeGAsV8/edit?usp=sharing
    Dalmar- Julio
    :return: none """


    direction = input("which direction do you want to go North/South/East/West")

    if direction.lower() == "north":
        # Bad choice! Sacrifice room!
        print("The north room is dimly lit by lanterns with red fire.")
        print("Five people in black robes are gathered around an altar.")
        print("Their argument quiets as you walk in.")
        sleep(delay)
        print("'Oh, how perfect,' one says. 'You have been Forgiven, Yuxila.'")
        print("Stone rises from the floor to block your exit.")
        sleep(delay)
        print("You are captured by the cultists. You are dead.")
        return False
    elif direction.lower() == "south":
        # Bad choice! Ritual room!
        print("You see a glowing circle on the floor. Robed figures stand around it and chant.")
        print("You do not recognize their words.")
        sleep(delay)
        print("A pressure builds in the room. It is too much.")
        print("Your heart bursts open inside your chest.")
        print("You are dead.")
        return False
    elif direction.lower() == "east":
        # Good choice! Dorms!
        print("The room you emerge into has a low stone ceiling. Bunked beds line the walls for fifty meters.")
        print("You walk carefully down the length of the room. Your breath is the loudest sound you hear.")
        sleep(delay * 2)
        print("At the end of the room is a kitchen and a door. There is no window.")
        print("You steel yourself and open the door as quietly as you can.")
        sleep(delay)
        print("The door leads outside. You are free.")
    elif direction.lower() == "west":
        # Neutral choice. Armory.
        print("This room is lined with weapons. Most are ornate daggers, hundreds of them hang on hooks lining the walls.")
        print("You see glowing runes on many of the daggers. Several do not have runes.")
        dagger = input("Do you take a dagger? [Yes/No]")
        if dagger == "Yes":
            print("You observe several daggers without runes. You take the one that looks unassuming.")
            print("The sound of a bell rings through the caves. You tense.")
            sleep(delay)
            print("Robed figures flood the room. You attempt to fend them off, but you are overwhelmed.")
            print("You are dead.")
            return  False
        else:
            print("This room looks suspicious. You return quietly to previous room.")


    return True


###################################################################################


def team_17_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_18_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_19_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_20_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_21_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_22_adv(username, delay):
    """
    https://docs.google.com/document/d/1KfNXomNLKmDJjPjTKwPYSAfdsDXUeLUHza7j-Q3XNqo/edit
    Harry Adkins
    :return: none
    """
    talk = input("Do you wish to talk to them? [Yes/No]")

    if talk == "Yes":
        print("It seems they're just as lost as you are!")
        sleep(delay)
        print("You agree to help each other find your way out of this cave, and they have tools to help")
    else:
        print("Due to your silence and shadowy figure in the dark, they mistake you for a beast!")
        chance = input("How many steps do you take towards the person? Enter an integer")
        if int(chance) > 7:
            print("They are startled by your rapid approach!")
            print("They charge at you head on and you trip and fall.")
            sleep(delay * 2)
            print("You keep falling?")
            sleep(delay)
            print("It seems you fell over a cliff, you're still falling and you don't know when you'll hit the gro-")
            return False
        else:
            print("They get closer to you and see you're a human too!")
            print("They agree to help you using tools from their backpack")


    tool = input("Which tool do you think will help? [Torch/Shovel/Compass]")

    progress = False
    while not progress:
        if tool == "Torch":
            progress = True
            print("You light the torch, and now you can see!")
            sleep(delay)
            print("It appears the cave leads into a well, and when you get closer you see light at the surface!")
        elif tool == "Shovel":
            progress = True
            print("You use the shovel and start blindly digging into the side of the cave")
            sleep(delay)
            print("You hear strange rumbling noises, you are pushed to dig faster")
            sleep(delay * 2)
            print("Are those sounds coming from above?")
            print("How strong are these cave walls anyways?")
            sleep(delay * 2)
            print("Brrrrrrr cshhhhhh CRASHHHHHHHH")
            sleep(delay)
            print("The walls collapsed in and crushed you! Seems those walls weren't too stable...")
            return False
        else:
            print("You pull out the compass, maybe if you follow one direction it'll lead somewhere eventually!")
            sleep(delay)
            print("...")
            sleep(delay)
            print("......")
            sleep(delay * 2)
            print("You can't see the compass, it's way too dark, maybe something else will help")
    return True
###################################################################################


def team_23_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_24_adv(username, delay):
    """ https://docs.google.com/document/d/1pagGD80WeZZPtCu2rmhw_abLWuwZWWwVawAJnmNB794/edit?usp=sharing
        Janee Amig
        :return: none """

    print("You're a lonely parakeet stuck in her cage. \nYou urge for freedom... \nYou heard from the local birds about a revolution to overthrow the humans, and to live among bird kind.")
    sleep(delay*3)
    print("Maybe you should take their wisdom and try to escape. But how?")
    sleep(delay*2)
    print("Get your owner's attention.")
    peck = int(input("How many times do you want to peck? [Enter a number]"))

    if peck > 6:
        print("Your owner takes notices and goes to your cage.")
        sleep(delay)
        print("'Do you want out?'")
        choice = (input("[yes/no]"))
        if choice == "no":
            print("Your owner leaves. Dang it. You could of escaped. Why didn't you say yes? (Replay to try again.)")
        else:
            print("Your owner opens the cage door. You are now free!")
            sleep(delay)
            print("Almost...")
            sleep(delay)
            print("Your owner picks you up and starts to pet you.")
            print("Should you accept the pets or bite? (Doing nothing is yes/Biting is no.)")
            choice = (input("[yes/no]"))
            if choice == "no":
                print("You bite your owner... 'OW! Why Pebbles?' ")
                sleep(delay)
                print("Biting is nice... ")
                sleep(delay*3)
                print("You keep on biting your owner's fingers.")
                sleep(delay*3)
                print("Ah yes... bloodshed... ")
                sleep(delay*4)
                print("Anyways your owner banned you in your cage. (Replay to try again.)")
            else:
                print("You like it when your owner spoils you with pets.")
                sleep(delay*2)
                print("Your owner puts you down on the dining table, and opens the window to let some fresh air in. \nYour owner has left the window opened multiple times and knows that you won't escape.")
                sleep(delay*3)
                print("Or will you?")
                sleep(delay*4)
                print("Should you escape to be free or stay? Do you want to leave?")
                choice = (input("[yes/no]"))
                if choice == "no":
                    print("You stay along with your owner. ")
                    sleep(delay*2)
                    print("Maybe freedom another day...)")
                    sleep(delay*2)
                    print("At least your safe from the outside and spoiled on the inside. \nThough will your brothern hate you for not wanting freedom you wonder?")
                else:
                    print("You made the choice to get outside of the house...")
                    sleep(delay*3)
                    print("Are you stupid?")
                    sleep(delay*2)
                    print("You think you could survive out there as a domestic animal?")
                    sleep(delay*2)
                    print("You fly around and try to begin your journey.")
                    sleep(delay)
                    print("Unforntaunly you get picked on by the local birds and get turned into a snack.")
                    sleep(delay*3)
                    print("Replay to try again to get a better ending.")
    else:
        print("Your owner doesn't hear you. Maybe try again? (Replay to try again).")

    return False
###################################################################################


def main():
    """
    The main function, where the program starts. No modifications are needed here!
    :return: None
    """
    delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!

    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv,
             team_21_adv, team_22_adv, team_23_adv,
             team_24_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story(delay)
    for i in range(len(paths)):
        is_alive = paths[i](user, delay)  # Runs each function in the paths list
        kill_if_dead(is_alive)
    end_story(user, delay)


main()