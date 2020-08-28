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

delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!
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
    print(
        "Congratulations, " + user + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay * 5)
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
    global dead  # You'll need this to be able to modify the dead variable
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
        sleep(delay * 2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print(
            "You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)


###################################################################################


def team_1_adv():
    """
    https://docs.google.com/document/d/1F0P3vEZ3SmVABobUui34lsocI5Lq1GXCKaVj4BmOcag/edit?usp=sharing
    Kylea Hughes
    Yryskeldi Emilbek uulu
    :return: none
    """
    global dead
    direction = input("Which direction are you thinking to take now? [North, South, East, West] ")
    if direction == "East" or direction == "east" or direction == "E" or direction == "e" or direction == "EAST":
        print("You meet up with a Mariachi band who then starts following you")
        sleep(delay)
        print("They begin to play and it's so loud that your location is compromised")
        print("You are approached by a rogue team of explorers.")
        print("They rob you of your resources and leave you for dead")
        dead = True

    elif direction == "West" or direction == "west" or direction == "w" or direction == "W" or direction == "WEST":
        print("You stumble into a pit of mutated venomous snakes")
        sleep(delay)
        print("Your chances of survival = 0")
        dead = True

    else:
        # lucky choice
        print(
            "You somehow manage to make it out alive and land on a cotton candy trampoline "
            "that leads you to a mysterious place.")
        sleep(delay)
        print("Good luck")

    if dead:
        print("Tough luck. Enjoy the afterlife.:)")
        quit()


def team_2_adv():
    """
    https://docs.google.com/document/d/13oN12oZgBLbtxg2XFv_iQheZ6v5G8izLmzkvZ3CCxtg/edit?ts=5f47a42b#
    Lydia Bodine and Caleb Handley
    """
    dead = False
    print("")
    Choice = input("What is your choice of sword today, warrior? [Iron/Diamond] ")

    if Choice == "Iron":    # good choice
        print("Good choice! ")
        sleep(delay)
        print("This sword is known to be one of the most powerful. ")
        sleep(delay)
        print("The journey continues, good luck.")
        sleep(delay * 3)
        print("")
        sleep(delay)
    elif Choice == "Diamond":  # bad choice
        print(" Every warrior who has chosen this sword has lost their battle. ")
        sleep(delay)
        print(" And that will be your fate. ")
        sleep(delay)
        print(" However...you have one more chance to make the right decision ")
        sleep(delay)
        Choice2 = int(input(" pick a number between 10 and 100 "))
        if Choice2 < 20:
            print("You have lived to see another day. ")
        else:
            print("That is the wrong decision, my friend.")
            sleep(delay)
            print("Better luck in your next life.")
            dead = True
    else:   # neutral
        print(" I guess you are not ready for an adventure today....")
        print("")
        sleep(delay)


def team_3_adv():
    global dead
    print("You continue along...")
    sleep(delay * 2)
    print("You encounter a Thief mid-robbery, but he's having some trouble")
    sleep(delay)
    action = input("What do you do? [stop/help]")
    if action == "stop" or action == "Stop":  # good choice
        print("You attempt to stop the thief...")
        sleep(delay)
        print("You tackle the thief and pin him to the ground, and wait for the police.")
        sleep(delay)
        print("When the police arrive, they thank you for your service with a pink-sprinkled donut")
    elif action == "help" or action == "Help":  # bad choice (You chose to help the thief)
        print("You decide to help the thief...")
        sleep(delay)
        choice = int(input("Choose how much money you hold [whole number]"))
        if choice >= 1000000:
            sleep(delay * 2)
            print("As the you run away, you are too slow and are shot down by the police")
            print("As you lie there dying you regret being greedy and taking too much money")
            dead = True
        else: # You chose a number less than 1000000 dollars
            print("You are quick enough to get away from the police")
            sleep(delay)
            print("Good Job, you weren't greedy and got away with some money")
            sleep(delay * 2)
    else:  # neutral choice You ran from the scene
        print("You avoid the situation, not wanting to get involved, and continue on your journey")

    # TODO Don't forget to check if your user is dead at the end of your chapter!

    if dead:
        print("Oh no you died, you should have tried harder")
        print("press the green button to try again") # green button = start button
        quit()


def team_4_adv():
    '''https://docs.google.com/document/d/10x_uJfVX33fnu9rpqR4PTmpJyVsYfWm1fiIuUsRnPNs/edit?usp=sharing
    Darius Morton
    David Olorunpoju-Esssang
    :return:none
    '''
    global dead
    terrain = input("Which pathway would you like to take? [Rocky/Bumpy/Smooth/Round]")
    if terrain == "Smooth":
        # Good choice
        print("You see an open door and can see sunlight shining through.")
        sleep(delay)
    elif terrain == "Bumpy":
        # Neutral choice
        print("You run into a wall with a creepy painting.")
        sleep(delay)
    if terrain == "Rocky":
        # Bad choice
        print("As you walk through the pathway you see an valuable gemstone.")
        sleep(delay)
        print("Once you grab it the floor opens and you fall through.")
        print("Beneath you there is a sea of hungry piranhas.")
        dead = True
    elif terrain == "Round":
        # Neutral choice
        print("You stumble upon a locked door.")
        sleep(delay)

    if dead == True:
        print("You are now dead, better luck next time. Maybe you should have chose another path.")
        quit()

def team_5_adv():
    """
    google docs: https://docs.google.com/document/d/1fCEj4kbOZqeZgzxPEVBn__-nbkaEqMKdCoscA5RDhbY/edit?usp=sharing
    Alina Cooper
    Ndizeye Tschesquis
    :return: none
    """
    print("Within the cave there are blood thirsty vampire bats that are sleeping.")
    sleep(delay)
    print("You must make the choice to sliver into one of the many parts of the cave")
    sleep(delay)
    choose = input("Where do you choose to go? [left/center/right]")
    if choose == "left":
        # Good choice!
        print("You move through the dark depths of the cave safely without waking the bats")
        sleep(delay)
        print("You see a light at the end of the treacherous cave")
        print("You've escaped!")
    elif choose == "center":
        # Bad choice :(
        print("You trip over rocks and cut your knee open!")
        sleep(delay)
        print("You awaken the bats with the smell of your blood")
        sleep(delay)
        weapon = input("You pick up a sharp stick. How many bats can you take on at once?")
        weapon = int(weapon)
        if weapon < 2:
            print("You were attacked from behind and the bats ate you")
            dead = True
        elif 2 <= weapon <= 5:
            print("You have managed to fight off the blood thirsty bats and you have survived")
        elif weapon > 5:
            print("You take on more bats than you can handle and become overwhelmed and die")
            dead = True
    else:
        # Neutral choice
        print("Down this path, you get lost within the dark depths of the cave")
    if dead == True:
        print("You've died :(")
        quit()


def team_6_adv():
    """
   https://docs.google.com/document/d/1ddpxUQ-6Qg1vtmu0X20TJ0seO8tpDTFwMT3WaqXEXbY/edit?usp=sharing
   Collins Kandongwe
   Caleb Seward
    """
    global dead
    my_destination = input("Which destination would you like to go? [Beach/McDonald's/Carnival]")
    if my_destination == "McDonald's":
        # if they choose McDonald's!
        # Bad choice...
        print("You discover there's a terribly long line. Oh well you'll wait!")
        print('')
        print("You accidentally shove someone in line...")
        print('')
        print("That person is a KAREN!!")
        print('')
        print("She starts yelling in your face!! SHE'S GETTING THE MANAGER!!")
        print("The manager bans you from McDonald's...FOR LIFE")
        print('')
        print("YOU GO ON STRIKE!")
        print('')
        print("McDonald's unfortunately doesn't care...")
        print('')
        print("You die of starvation...:(")
        dead = True
    elif my_destination == "Carnival":
        # if they choose amusement park!
        # Bad choice...
        print("You've arrived at the Carnival and it's BEAUTIFUL!!")
        print('')
        print("You see a crowd of people...what's going on??")
        print('')
        print("OH MAN! There's a kid and an old man fighting!!!")
        print('')
        my_choice = input("Do you want to stop them??: yes/no")
        if my_choice == 'yes':
            print("You try to save the boy!")
            print("OH NO! THE OLD MAN HIT YOU IN THE HEAD WITH HIS CANE!!")
            print("You die from a concussion...")
            dead = True
        else:
            print("You need to use the restroom!")
            print('')
            print("You go into the nearest port-a potty.")
            # Cue ominous music...
            print('')
            print("Oh no...you hear thunder while doing your business!!")
            print('')
            print("OH MY GOODNESS! THE DOOR WON'T OPEN!!")
            print('')
            print("OOH NOO! THE WIND IS MOVING THE PORT-A POTTY!!")
            print('')
            print("DEAR GOD!!! IT'S A HURRICANE!!!")
            print('')
            print("YOU'RE BEING LIFTED INTO THE AIR!!!")
            print('')
            print("YOU'RE FALLING!!!")
            print('')
            print("You tragically died from the impact")
            print('')
            dead = True
    else:
        # good Choice!!!
        print("YOU FINALLY GOT OUT!")
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        kill_if_dead(dead)


def team_7_adv():
    pass
    # TODO Add your code here


def team_8_adv():
    pass
    # TODO Add your code here
    """"
     https: // docs.google.com / document / d / 1
    baJIWVUbm7os6gvjg_jRNmMuBTdsrLglumFw5zSe6zc / edit?usp = sharing
    Sierra Deitsch
    Aja
    :return: none
    """
    dead = False

    path = input("Where would you like to go now that you've escaped the cave? [Bridge/Tower/Forest/River] ")

    if path == "Bridge":
        # Good Choice!
        print("Over the bridge is a cabin. Nobody's home but you find food!")
        sleep(delay)
    elif path == "Tower":
        # Neutral Choice
        print("There is nothing in the tower, but maybe this would be a good place to rest.")
        sleep(delay)
    elif path == "Forest":
        # Bad Choice
        print("You walk aimlessly for what feels like hours. Maybe now would be a good time to rest...")
        sleep(delay)
        print("You wake up face to face with a snake!")
        print("Whew! You made it away just in time.")
        print("But, you're starving... And you come across a bush with blue berries! "
              "(That's blue berries, not blueberries.")
        berry_number = int(input("How many berries would you like to eat? "))
        if berry_number > 10:
            print("Great! You're not starving and you continue your path through the forest unharmed.")
        else:
            print("Oops! Too few... berries... You start to... feel... dizzy.")
            dead = True
    else:
        # Neutral Choice
        print("You don't find anything, but now might be a good time to rest.")
        sleep(delay)

    if dead == True:
        print("Oh no, you died. Try again by hitting the green play button.")
        quit()

def team_9_adv():
    pass
    # TODO Add your code here


def team_10_adv():
    # TODO Add your code here
    """
    Introduction text for the story. Don't modify this function.

    :return: the user's name, captured from user input
    """
    dead = False
    username = input("What do they call you?")
    print()
    print("welcome", username, "to the forest leading to Grandmothers house.")
    sleep(delay)
    print("You are walking to grandmas house, in front of you lies three paths")
    print("In front of you there are three paths. One leads you safely, one is a shortcut, one is undiscovered")
    print("Choose wisely")
    sleep(delay * 2)
    print("It is getting dark so she wants you to hurry")
    sleep(delay)
    direction = input("Which path do you choose to get to grandmas house? [1,2,3]")
    if direction == "1":
        # Correct choice!
        print("You made it to grandmas house safely, and you managed to miss the hungry werewolf")
        sleep(delay)
    elif direction == "2":
        # Wrong path
        print("Along the path you encounter something that blurs your vision.")
        sleep(delay)
        print("You try to react in time but you hear a growl and snarling getting closer behind you.")
        print("You see its a werewolf and try to run but he grabs you and eats you whole")
        dead = True
    else:
        # neutral choice
        print("Still walking on the path, yet to encounter the wolf.")
        sleep(delay)

    if dead:
        print("The wolf ate you, Better luck next time. Click the green button to try again")
        quit()
def team_11_adv():
    pass
    # TODO Add your code here


def team_12_adv():
    """
    https://docs.google.com/document/d/1KFmb0taSBgypm81r4ZO01vJLmb7bNNXZ2lI9EXUgOrc/edit?usp=sharing
    Destiney Mccoy and Nancy Landeros
    """
    # TODO Add your code here
    global dead
    print("OH NO! There's a sudden horrible screeching sound from up above!")
    sleep(delay)
    print("It's a massive CAVE BAT!!!")
    sleep(delay)
    print("And it's heading straight for you!!!")
    sleep(delay)
    choice = input("What will you do? [Run/Duck/Snatch]")

    if choice == "Snatch":             # the good choice
        print("SICK! You snatched that bat! It is now your sidekick.")
        sleep(delay)

    elif choice == "Run":                   # the bad choice
        print("that is a wrong choice, you were about to die. You will get one more chance to survive.")
        sleep(delay)
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        second_choice = input("pick a number between 1 and 10")

        if second_choice > "5":
            print(" right choice, you survived for now ")
        else:
            print("The bat caught you with it's weird long talons and scratched your eyes out.")
            print("You died from your injuries.")
            dead = True

    else:
        print("Hmm...you survived the beast. Carry on...")
        sleep(delay)


if dead:
    print("Bruh.")
    sleep(delay)
    print("Hit the green run button to try again.")
    quit()

pass

def team_13_adv():
    """
    https://docs.google.com/document/d/12B_ZB4AfvERDoiExACvnUPc96CUFAVZu9MydgHBHr88/edit?ts=5f47a426#
    Karina Agliullova
    Jakob Bister
    :return: none
    """
    # TODO Add your code here
    global dead
    dead = False
    print()
    print("You continue through the cave, light begins to creep through the ceiling")
    print("you notice a strange smell but a pile of wood and matches nearby catches your attention.")
    print()
    action = input("What would you like to do? [light/inspect/ignore]")

    if action == "light":
        # Bad Choice!
        print("You light the match, everything goes bright, now you realize what the smell was...Gas-BOOM!")
        print()
        dead = True

    elif action == "inspect":
        # Good Choice.
        print("You inspect the supplies, you go to light the fire but remember the smell in the room.. ")
        print("you decide to keep moving and take the supplies with you.")
        sleep(3)
        print()
        print("As you keep moving you walk upon a sign on the wall that warns of a Gas Leak.")
        print("You laugh realising how close you were to getting out of here...the wrong way.")
        print()

    else:
        # Neutral Choice.
        print("You're in another section of the cave, you begin the shiver wishing you had a fire")
        print("but at least the smell is gone...")
        print()

    if dead:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        quit()

def team_14_adv():
    """
    https://docs.google.com/document/d/1Ax0pfBALRhBNzidAtm-vubEhNZnjqW2tGaor7gEjW2c/edit?usp=sharing
    Genevieve McWilliams
    Jhonny Sontay
    :return: none
    """
    # TODO Add your code here
    global dead
    print("You wake up to several sounds...")
    print(
        "One coming from behind, one from something running to your right, "
        "and the other from a blazing fire to your left.")
    print("")
    sound = input("Which sound do you choose to follow? [Behind/Left/Right] ")

    if sound == "Behind" or sound == "behind":
        # Neutral Choice
        print("You're running away from your fears...this will not get you far in life.")
        sleep(delay)
    elif sound == "Left" or sound == "left":
        # Bad Choice...
        print("You arrive at a Devil Convention.")
        sleep(delay * 2.5)
        print("Part of the celebration is to roast you...")
        sleep(delay * 2.5)
        print("First by roasting you with offensive jokes about your life, then literally roasting you.")
        sleep(delay * 3)
        print("In order to survive, you have one option...")
        sleep(delay * 3.5)
        print("Join their cult.")
        sleep(delay * 2.5)
        choice = input("Would you like to accept the invitation to join the cult? [yes/no] ")
        if choice == "yes" or choice == "Yes":
            print("Congratulations, you have a new family.")
            print("You're officially a devil.")
            sleep(delay)
        else:
            print("Congratulations, you died.")
            dead = True
    else:
        # Great choice
        print("You see your deceased Grandma running...")
        sleep(delay * 3.5)
        print("You then embrace each other and talk about the days when you sucked your thumb.")
        print("You are so happy.")
        sleep(delay * 3)

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
    random.shuffle(paths)  # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()  # Runs each function in the paths list

    end_story(user)


main()
