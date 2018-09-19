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
    pass
    # TODO Add your code here


def team_3_adv():
    pass
    # TODO Add your code here


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():
    pass
    # TODO Add your code here


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
    """
    Team 9's refactored chapter.
    Originally by hilljac & nudgarrobot, refactored by Juem, Jamalie, Gutheriet.
    Google doc:
    https://docs.google.com/document/d/1gmxTnKp2swHlYWCZ1cTMZxnLcmNqr2PQnm7XLbYNwsU/edit?usp=sharing

    :return: None
    """


injured = 0          # You start with 100% of your limbs! When this reaches two, you die!
flashlight = 0       # You have no source of light!
anti_soft_lock = 0     # For loops
checkGlint = 0       # Tracking!
checkPool = 0       # ^

direction = input("Which direction would you like to go? [North/South/East/West]")

if direction == "South":
    # Good choice!
    print("...")
    sleep(delay)
    print("Ooooooo boy!! You enter a room FILLED WITH GOLD!")
    sleep(delay)
    print("In addition to the gold, there seems to be a flashlight right in front of you! This is too good to be true!!")
    sleep(delay)
    itemChoice = input("What do you do? [Pocket the gold]/[Grab the flashlight]/[Try to grab both]")
    sleep(delay)
    if itemChoice == "Pocket the gold":
        print("You stuff your pockets as full as you can, and continue on your journey")
        sleep(delay*3)
        print("But wait!!")
        sleep(delay)
        print("Suddenly an enchanted skeleton appears, demanding that you return the gold, or pay with your life")
        skeletonChoice = input("Which will you do? [Keep the gold / Leave the gold]")
        sleep(delay)

        # branching good path
        if skeletonChoice == "Keep the gold":
            print("You decide to keep the gold for yourself, and attempt to run for your life. You escape the room, but in the process, the skeleton stabs you in the shoulder, injuring you for the duration of the adventure")

        elif skeletonChoice == "Leave the gold":
            print("You leave the gold and peacefully leave the room. Satisfied with your following his orders, the skeleton disappears. Your adventure continues")

        else:
            print("You have the confused the skeleton.")
            sleep(delay)
            print("Now the skeleton is angry!")
            sleep(delay*5)
            print("the skeleton has killed you...")
            sleep(delay)
            dead = True
            sleep(delay)
            if dead is True:
                print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
                quit()

    elif itemChoice == "Grab the flashlight":
        print("You decide to play it safe and only grab the flashlight. Obviously, the gold was a trap.")
        sleep(delay)
        print("You peacefully leave the room and your adventure continues. Also, now you have a flashlight!")
    elif itemChoice == "Try to grab both":
        print("You rush towards the motherlode in front of you!")
        sleep(delay)
        print("You grab the flashlight and start stuffing your pockets with as much gold as you can carry.")
        sleep(delay)
        print("You're gonna be so ri-")
        sleep(delay*2)
        print("everything is going dark...")
        sleep(delay*2)
        print("you're not sure, but you feel as though you have been stabbed from behind.")
        sleep(delay*2)
        print("You fall to the ground...")
        sleep(delay*2)
        dead = True
        sleep(delay)
        if dead is True:
            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            quit()
    else:
        print("You decide this whole situation is too good to be true, and is certainly a trap.")
        sleep(delay)
        print("You turn away and your adventure continues.")
elif direction == "East":
    # Bad direction 2. Internal decisions can make it a trade, but an injury is normally guaranteed.
    print("You notice a rather low overhang in the darkness of the cave")
    sleep(delay)
    print("You're wary, but nothing's going to get done if you're overly hesitant.")
    sleep(delay)
    print("You crawl under the overhang and realize it's more of a short tunnel-")
    sleep(delay)
    print("It's very narrow, and you barely make your way out the other side.")
    sleep(delay*1.33)
    print("The air is has a notable chill and movement on the other side of the tunnel,")
    sleep(delay)
    print("and you hear a faint dripping reverberating through the space.")
    sleep(delay)
    if flashlight == 1:
        print("You sweep the flashlight over the space, but its beam doesn't reach the opposite wall.")
        sleep(delay*2)
        print("The stone in this part of the cave is smooth, seemingly worn down.")
        sleep(delay)
        print("The light does, however, illuminate a layer of mist swirling over a small pool")
        sleep(delay*1.33)
        print("The pool is perfectly still, and despite the darkness, is a deep, almost ethereal blue.")
        sleep(delay*2.33)
        print("In the far side of the cave, you see something small glisten as you sweep the flashlight over it.")
        choice = input("[Inspect pool]/[Check Glint]")
        # TODO Flesh out choices for flashlight-enabled play!
        if choice == "Check Glint":
                print("You carefully walk around the pool and inspect the base of the wall for anything unusual.")
                sleep(delay)
                print("Unlike most of the room, there are rough, broken rocks here and a crack in the wall.")
                sleep(delay)
                print("Sifting through the rocks and debris, you find a kind of cup--")
                sleep(delay)
                print("The cup is shaped in such a way as to resemble a stemless goblet.")
                sleep(delay)
                print("It's inlaid with small gemstones, and strange symbols mark its surface.")
                sleep(delay)
                print("You decide that it's worth keeping.")
                checkGlint = 1
                chalice = 1
        elif choice == "Inspect pool":
            checkPool = 1
            print("You walk up to the lip of the pool. As you approach, the mist recedes.")
            sleep(delay)
            print("Thick and unnatural, the mist seems almost to pulse as you draw near.")
            sleep(delay)
            print("Upon closer observation, the pool is by no means water-")
            sleep(delay)
            print("Instead, it's a thinner liquid, so much so that the edge seems at times to blur with the mist above it.")
            sleep(delay)
            print("As you remain by the edge, the mist seems to grow more agitated in its swirling.")
            sleep(delay)
            if checkGlint == 1:
                choice = input("[Collect from Pool]/[Touch Pool]/[Remain Motionless]/[Retreat]")
            else:
                choice = input("[Check Glint]/[Touch Pool]/[Remain Motionless]/[Retreat]")
            if choice == "Touch Pool":
                print("You dip your hand into the crystal clear liquid.")
                sleep(delay)
                print("It feels strange, as if it were fine silk that was impossible to hold.")
                sleep(delay)
                print("Suddenly, you feel something coil around your wrist")
                sleep(delay)
                print("But the pool is still perfectly clear, and you see nothing.")
                sleep(delay)
                print("In panic you try to wrest your arm free, but only throw yourself off balance.")
                sleep(delay)
                print("Your other arm plunges into the pool as you try to steady yourself")
                sleep(delay)
                print("You claw at your bound wrist, trying to remove the invisible restraint")
                sleep(delay)
                print("But your hand finds nothing to grasp.")
                sleep(delay)
                print("You struggle helplessly against the swirling fluid, which is now pulling your arms deeper")
                sleep(delay)
                print("Absorbed in your struggle, you notice the mist too late--")
                sleep(delay)
                print("It has rolled forward, and is upon you, enveloping you.")
                sleep(delay)
                print("Forced to breathe it in, the last of your strength drains away")
                sleep(delay)
                print("As your vision slowly goes black, the last you feel is the soft, silky feeling of the pool's embrace.")
                sleep(delay)
                sleep(delay)
                dead = True
            elif choice == "Check Glint":
                print("You carefully walk around the pool and inspect the base of the wall for anything unusual.")
                sleep(delay)
                print("Unlike most of the room, there are rough, broken rocks here and a crack in the wall.")
                sleep(delay)
                print("Sifting through the rocks and debris, you find a kind of cup--")
                sleep(delay)
                print("The cup is shaped in such a way as to resemble a stemless goblet.")
                sleep(delay)
                print("It's inlaid with small gemstones, and strange symbols mark its surface.")
                sleep(delay)
                print("You decide that it's worth keeping, but upon taking it the wall behind caves in--")
                sleep(delay)
                print("You're blinded by light pouring through the opening the cave in created.")
                sleep(delay)
                print("When you can see again, you realize you're looking out over a range of mountains.")
                sleep(delay)
                print("Far from being deep underground, you had been trapped in the top of a mountain!")
                sleep(delay)
                print("You step out and breathe a sigh of relief in the clean mountain air.")
                checkGlint = 1
                chalice = 1
            else:
                print("If you're seeing this, you've probably referred to one of our placeholders!")
                print("While we intend to flesh these out later, at present it would be detrimental")
                print("to assignment deadlines! Speaking of deadlines, this is one! Have fun replaying!")
                dead = True

    else:
        print("Although the room is still too dark to see anything, the cavern feels immense.")
        sleep(delay)
        print("The cave floor under you feels smoother than the rest of the cave so far.")
        print("You place a hand on the wall to ground yourself- In the pitch blackness, you feel you could easily lose yourself.")
        sleep(delay*1.33)
        print("The wall is angled inward, and is just as smooth as the floor.")
        print("You don't particularly feel the space inviting...")
        sleep(delay*2)
        print("...But you still need to find a way out of here.")
        while anti_soft_lock == 0:
            choice = input("[Follow wall]/[Venture into dark]/[Retreat through tunnel]")
            if choice == "Follow wall":
                print("Placeholder text, you follow the wall.")
                anti_soft_lock = anti_soft_lock + 1
            elif choice == "Venture into dark":
                print("Placeholder text, you leave the wall and walk into the inky blackness.")
                anti_soft_lock = anti_soft_lock + 1
            elif choice == "Retreat through tunnel":
                print("Placeholder text. The tunnel is too wide to retreat through without forcing yourself through.")
            else:
                print("If you're seeing this, you've probably referred to one of our placeholders!")
                print("(Or just something that doesn't exist!)")
                print("While we intend to flesh these out later, at present it would be detrimental")
                print("to assignment deadlines! Speaking of deadlines, this is one! Have fun replaying!")
                dead = True


else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead is True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

def team_10_adv():
    pass
    # TODO Add your code here


def team_11_adv():
    pass
    # TODO Add your code here


def team_12_adv():
    pass
    # TODO Add your code here


def team_13_adv():
    pass
    # TODO Add your code here


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
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story(user)


main()
