######################################################################
# Author: Fall 2019 Class
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = .10  # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False  # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print("\n")
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

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
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print(
        "You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TODO Team 1
sleep(delay * 2)
print("\n\nYou continue on with your journey. You happen to stumble across a bomb.")
print("God offers you some wirecutters. With nothing to lose, you decide to be a hero.")
print("You unscrew the bomb. In front of you are three wires: red, blue, and yellow.")
sleep(delay * 2)
print("Which wire will you choose?", username, "?")
color = input("Red, Blue, or Yellow?")

if color == "Red" or color == "red" or color == "Red " or color == "red ":
    # if color == "Red" or "red" or "Red " or "red ":
    # The good choice
    print("You suck in a breath and then cut the wire. The LEDs flicker, then shut off. You did it!")

elif color == "Blue" or color == "blue" or color == " blue" or color == "Blue ":
    # elif color == "Blue" or "blue" or " blue" or "Blue ":
    # The bad choice
    print("You suck in a breath and then cut the wire. The bomb explodes into a white light. You die instantly.")
    dead = True

else:
    # neutral choice
    print("You suck in a breath and cut the yellow wire.")
    print("")
    print("Nothing explicitly happens, but suddenly you have a loaf of banana nut bread in your pocket.")
    print("... You decide to move on.")

#########################################################################################################
# TODO Team 2
print (
    "Congratulations! You have survived so far. But the journey does not end for the gold still lays undiscovered. \n ")
sleep(delay * 2)
direction = input("Which way would you like to go now? Choose wisely North, East, West or South?\n")
if direction == "East":
    print (
        "You have proven how worthy you are so the gods have decided to reward you with Gold. \n You are rich now go home and spread your wealth! \n")
elif direction == "North":
    print("This trip is only for the worthy. You have been found unworthy and the gods have sacked your soul.\n")
    quit()
elif direction == "West":
    print (
        "Some wolves come by and urinate all over your stuff, then eat your face off. Tragic, you could have been rich but now you're dead.")
else:
    print (
        "You were found by a group of robbers. They know you have enough food and gold to last you days. They loot you and leave you for the bears.")
sleep(delay)
print ("You're in the cave, its night time and you began to hear screams from one of two paths.")
direction = input("Which path will you take, East or West? Choose wisely.")
if direction == "East":
    print ("""Congratulation! You have found the exit and havce made it out with only a few scratches and maybe some broken bones, but look on the bright side, atleast you're alive.
     Look on the bright side, you have experienced the deadly cave and came out with your life. Yay!""")
else:
    print (
        "You become curious of the screams and follow them. You stumble upon a group of rich cave partiers and they invite you to join them")
    quit()

#########################################################################################################
# TODO Team 3
sleep(delay)
print()
print(
    "You are being chased by a group of goblins. You and your friend for some reason decide to run to a cliff. What do you do?")


def input_action():
    action = input("[Sleep | Jump | Do Nothing | Fight] ")
    return action


def ask_action(my_input):
    # Another option of prompting the user to re-enter option incase they had an input that is not Jump, sleep. fight or do nothing
    # while 2==2:
    #     my_input = my_input.lower()
    #     if (my_input =="sleep") or (my_input == "jump") or (my_input =="do nothing") or (my_input =="fight"):
    #         break
    #     print("This is out of the choice Sleep,Jump,Do nothing or fight.Make another choice!")
    #     my_input = input_action()
    if my_input == "sleep":
        # Good choice
        sleep(delay)
        print("Amazing! Good job, ", username, "! You have found their weakness! Goblins can't see sleeping people...")
        sleep(delay)
        print("As you awake, you notice some golden coins one of the goblins meleft behind.")
        sleep(delay)
    elif my_input == "do nothing":
        # Bad choice
        print("Do nothing? YOU DIE!!!!")
        dead = True
        sleep(delay)
        if dead == True:
            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            quit()
    elif my_input == "fight":
        print("You have proved so brave. Go on with your journey!")
    elif my_input == "jump":
        print("At the bottom of this cliff lies waves of fast flowing water. Jumping was not a good choice!")
    else:
        print("The choice you entered is not available. Renter ")
        main1()


def main1():
    ask_action(input_action())


main1()

#########################################################################################################
# TODO Team 5
direction = input("Which flavor would you like? [Strawberry/Pistachio/Chocolate]")

if direction == "strawberry":
    # Good choice!
    print(
        "Good choice!This makes you feel a lot better considering your friend disappeared mysteriously the other day.")
    sleep(delay)
elif direction == "chocolate":
    # Oh... Bad choice
    print("Here you go, this is a van favourite!")
    sleep(delay)
    print("Oh it tastes so familiar but not in a good way")
    print("At first you don't realize it but then you start feeling nauseous")
    print("You start vomiting and ask 'what the hell was that?'")
    print("The ice cream people tells you: Don't worry! It's just your friend!")
    sleep(delay)

else:
    # Neutral choice
    print("You feel a tingling sensation in your throat, and you start puking blood and pistachios.")
    print("As everything starts going black, you vaguely hear evil laughter. ")
    print("The ice cream van starts up and a merry song starts playing and slowly fades away")
    dead = True
    sleep(delay)

if dead == True:
    print("Hey friendo! Wanna make some more chocolate ice cream?")
    quit()

#########################################################################################################
# TODO Team 6
# Introduction
print('''Ah! So I see you're still alive ''' + username + "!")
print('''Little did you know though, you have yet another path before you!''')
print('''Before you, you see a old, green bridge. It's length is terrifying, looking as though it goes for miles''')
print('''each board creeks as a small, wrinkly figure appears before your''')
print('''It looks like a troll and begins to speak to you''')
print('''Troll: Here before you is the bridge of DEE''')
print('''       If you wish to pass, answer these questions, three''')
print('''''')
# Assign user input values
playername = input('       What ... is your name?')
print('       What ... is your quest?')
quest = input('     You say, "I seek: ')
quest = quest.lower()
color = input('       What is my favorite color?')
color = color.lower()

# Checks if player gets all questions right or all questions wrong
if playername == username and quest == "the holy grail" and color == "green":
    # Good Answer
    print("As you answer the last question you leave the troll flabergasted and he goes flying off into the sky.")
    print("He will bother you no more and you can finnaly continue onward in your journey")
    print("plus you pick up a bag of doritos on your way")
elif playername != username and quest != "the holy grail" and color != "green":
    # Bad Answer
    print("Oh no it seems you have not meet up to the trolls standards")
    print("You feel the wind building up beneath you and within seconds you find you self launched it to the air")
    sleep(delay)

    dead = True
else:
    print("You have just barley meet the trolls standards. you may pass the bridge")
    print("he does growl at you as you pass though")
# Scott Heggen is Iron Man :) also the TA's
if dead == True:
    print("As your consciousness slowly fades, a shaded figure appears.")
    print("Before you pass, you realize that the shaded figure is Scott Heggen.")
    print('He leans over and says, "better luck programming next time." Then he takes your wallet.')
    print("It was sad, because you remember as he leaves that you had a coupon in there.")
    print("You are dead.")

    quit()

#########################################################################################################
# TODO Team 7
direction = input("Which direction would you like to go? [Right/Forwards/Backwards/Left]")

if direction == "Right":
    # Good Choice!
    print("You rush into the nearby trees for cover. There you find a mystical coconut that will slay the dragon.")
    sleep(delay)
elif direction == "Forwards":
    # Bad Choice
    # print("You almost made a bad choice! The dragon hasn't seen you yet! Pick a number.")
    integer = int(
        input("You have made a bad choice! You have one more chance to avoid being burnt alive. Pick a number. [1,2]"))
    if integer == 1:
        print("You have saved yourself and spared yourself from the dragon!")
    elif integer == 2:
        print("You failed to make a better decision and gave the dragon time to get the BBQ sauce.")
        print("You have decided to run towards the dragon. The dragon scoffs and burns you to a crisp.")
        dead = True
        sleep(delay)
        # Finished!
else:
    # Oh...Bad Choice
    print("You just got eaten by man-eating roaches!")
    sleep(delay)
    print("Try to pick another direction to follow!")

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button.")
    quit()

#########################################################################################################
# TODO Team 8
sleep(delay)
print()
print ("Thum.. Thum.. Thum.. You heard footsteps approaching.")
sleep(delay * 2)
print ("Hello,", username, "I am the spirit of the cave, here take some of these food to help you with you journey.")

choice = input("Take the food? [yes/no]")
choice = choice.lower()

if choice == "yes":
    print ("You took the food and ate it. Now you have enough energy to continue on you journey.")
    sleep(delay)
    print("Congratulations! You made a wise choice.")
elif choice == "no":
    second_choice = int(input(
        "\nOkay, you don't have to eat all the food but you must take some bites. How many bites are you going to take? [0-200]"))
    while True:
        if second_choice >= 0:
            if second_choice > 100:
                print ("\nYou ate too much, and exploded!!")
                dead = True
            elif second_choice == 0:
                print ("\nYou get hungry and your energy level dropped. You passed out.")
                dead = True
            elif second_choice <= 100 and second_choice > 0:
                print ("\nYou took the food and ate it. Now you have enough energy to continue on you journey.")
                print("Congratulations! You made a wise choice.")
            break
        second_choice = int(input(
            "That is not possible. Now, lets try again. How many bites would you like to take? Input a number from 0-200 this time. "))

else:
    print ("Enter either 'yes' or 'no'. The spirit of the cave would not take any other answers.")

# TODO Don't forget to check if your user is dead at the end of your chapter!
if dead == True:
    print ("Oh no, when you are passed out, a bear came accross your body and YOU WERE EATEN.")
    quit()

#########################################################################################################
# TODO Team 9
print("You see a dim light glowing behind a loose boulder. Do you choose to "
      "investigate?")
Choice = input("[Yes/no/leave]")
sleep(delay)

if Choice == "Yes":
    print ("You place your hand against the boulder and it dissipates into the air like fine mist. Behind it you see "
           "a giant sword bigger than most men.")
    sleep(delay)
    print("A giant humanoid creature enters your view and begins to grab the sword.")
    sleep(delay * 2)
    print("He swings the sword in your direction causing the timid ceiling to collapse in between you saving yourself "
          "from the giant beast. ")
    print("You are safe for now, and you begin to search for a way out..")
    #
    #
    sleep(delay)
elif Choice == "no":
    print("You choose to hastily run away from the boulder and you begin to lose your footing.")
    sleep(delay)
    print("You trip and fall forward breaking your neck in the most boring possible fashion")
    dead = True
else:
    print("You decide against your gut and move away from the glowing boulder.")
    sleep(delay)
    print(
        "You leave the cave by following the sounds of wilderness outside. You begin to hear some disgruntled shuffling in the cave as you leave.")
    if dead == True:
        print("You Died! Try again.")
    quit()

#########################################################################################################
# TODO Team 10
# Beginning of the Amulet Encounter Chapter

print()
print("You are in a room with strange symbols all over the walls.")
print("Looking at the eldritch markings makes your head hurt just by looking at them.")
print("You see an amulet floating in the middle of the room over a pedestal.")
print()

amuletAction = input("What do you want to do? [Wear/Ignore/Destroy]")

print()

if amuletAction == "Wear":
    # Bad choice
    print("Nothing happens... ")
    sleep(delay * 3)
    print("...")
    sleep(delay * 3)
    print("You feel strange, your hands starts twitching uncontrollably.")
    print("You start walking back into the darkness, not in control of your own actions.")

    # Begin Test of Wills

    print()
    print("You're body is under new management at the moment.")
    print("The walls begin to morph, forming words you can comprehend, requesting a number.")
    amuletSave = input("What is The Ultimate Answer to Life, The Universe and Everything?")

    if int(amuletSave) == 42:
        print()
        print("Your body starts responding again.")
        print("You seem to have shaken off the evil manipulation.")
        print("Harrowed by your brush with death, you carry on, deeper into the labyrinth")
    elif int(amuletSave) >= 41 and int(amuletSave) <= 43:
        print()
        print("Close enough!")
        print("You shake off the control with moments to spare and come to your senses.")
        print("You twitch one last time and run for you life, towards (unlikely) safety...")
    else:
        print("INCORRECT MORTAL!!!")
        print("NOW DIE FOR YOUR IGNORANCE!")
        dead = True

elif amuletAction == "Destroy":
    # Good option
    print("As you cast the amulet into some previously un-narrated lava, you feel watched by a giant eye.")
    print("As the amulet disintegrated, you feel a cursed being lifted from the Median-Earth.")
    print("Satisfied with your good deed for the day you carry on deeper into the labyrinth...")
    print()


elif amuletAction == "Ignore":
    # Boring option
    print("So you ignore the floating mystical artifact in the middle of the room.")
    print("We went through all of the trouble in making a cool, levitating, magic item for you and you ignore it...")
    print("Way to go, you hurt our creative pride.")
    print("Well, I guess you can carry on, further deeper into the depths of the labyrinth...")
    print("Away from anything fun...")
    print()

else:
    # Just in case option
    print("Somehow, our scenario wasn't interesting enough for you to even answer properly.")
    print("Whatever you just did somehow broke the laws of causality and you glitch")
    print("through a lamp using a backwards long jump and end up in a parallel dimension in another room...")
    print()

if dead == True:
    print("Congratulations! You've been possessed by an ancient evil!")
    print("Don't mess with cursed objects kids!")
    print("Better luck next time! Try again by hitting the green play button in the top right. ")
    quit()

print()
print()

#########################################################################################################
# TODO Team 12
choice = input("[yes/no] ")
print("You walk into a room and see a glass of milk sitting on a table. Do you drink it?)")
if choice == "yes":
    print("Great you refilled your health ")
elif choice == "no":
    print("you die from starvation?!")
    sleep(delay)
else:
    # neutral choice
    print("you later found berries in the dark hall")

print("In the dark hall you see a libra scale. You have to set the scale equal to a bar of silver.")
choice = int(input("Pick a number"))
if choice > 0 and choice <= 10:
    print("A door opens")
elif choice > 10:
    print(" You fall to your death")

# TODO Don't forget to check if your user is dead at the end of your chapter!

if dead == True:
    print("Oh no! you died. Better luck next time! Try again by hitting the green play button")
    quit()

#########################################################################################################
# TODO Team 13
sleep(delay * 3)
print("")
print("")
print("It seems like you will be here a while.")
print("You see two doors in front of you. One is made of wood. It looks like it is about to fall off.")
print("The other door is just plants. All you gotta do is walk through and you're on the other side. ")
print("There is also a doorway with no door. ")
choice = input("Where will you go? [Wood/Plant/No door]   ")
if choice == "Wood":
    print("As you push the door open, it falls off. ")
    print("The loud noise wakes up the polar bear sleeping inside. It then proceeds to devour you with salt.")
    dead = True
elif choice == "Plant":
    print("You brush the plants to the side and walk through the doorway.")
    print("This opens up a secret path. You follow this path for hours.")
    print(" You somehow ended up at the same doorways that you encountered earlier.")

elif choice == "No door":
    print(" You walk through the doorway and you see a faint light in the distance. You run to this light.")
    print("You discover a chest. You open the chest and find food and water in the chest!.")
    print("After eating, you continue to walk on and eventually find the Exit. ")
    print("You are free!")
if dead == True:
    print("You have been eaten by the polar bear!")
    quit()

#########################################################################################################
# TODO Team 14
print()
print("You stumble into the woods. There are three paths in front of you.")
print()
answer = input("Which direction do you want to go? [North/East/West] ")
print()
if answer == "North":
    # Bad choice
    print("You are being chased by wolves.")
    print("Try to run away! Good luck!")
    print()
    safe = input("How long do want to run? [1-10]")
    try:
        a = int(safe)
        if int(safe) >= 7:
            print()
            print("The wolves get tired of chasing you.")
    except ValueError:
        print()
        print("Oh no. They caught you.")
        dead = True
elif answer == "West":
    # Good choice
    print("You stumbled into a clearing. \n You escape the woods.")

elif answer == "East":
    # Neutral choice
    print("The path leads you deeper into the woods.")
    print("You are now lost.")
else:
    print("You can't think clearly. \n You sit there for eternity.")
    dead = True

if dead == True:
    print("Seems like you made a poor decision.")
    print("You have died!")
    quit()

#########################################################################################################
# TODO Team 15
print("You come upon three doors.")
sleep(delay * 2)
print("The one of the left has a light glowing from underneath.")
sleep(delay * 4)
print("The one in the middle looks old and cracked.")
sleep(delay * 4)
print("The one on the right is made of rusted metal.")

direction = input("Which door will you choose? [Left, Middle, Right]")
if direction.lower() == "right":
    # good choice
    print(
        "You can barely see because the room is so dark and dusty. \nYou light your torch and see the room is filled to the brim with gold and jewels!.")
    sleep(delay * 4)
    print("Congratulations, you're rich!")
    choice = 0

elif direction.lower() == "left":
    # worst choice
    print(
        "You step through the door onto a thin sheet of ice. Below the ice, electricity arcs from one electric eel to another.\nYou turn quickly to walk back out the door and...")
    sleep(delay * 3)
    print("A golden dragon appears, he offers to help if and only if you can guess a number between 1 to 10")
    number = int(input("What number do you choose?"))
    if number >= 6:
        print("He offers you a ride to safety, you come out with no major injuries.")
        choice = 2
    else:
        print("The ice breaks! You are electrocuted while you are drowned... ")
        dead = True
        choice = 1
else:
    # boring choice
    print("You open the middle door. Behind the door you find a long passage with stairs that seem to go up forever.")
    sleep(delay * 2)
    print("...")
    sleep(delay * 2)
    print("....")
    sleep(delay * 2)
    print(".....")
    sleep(delay * 2)
    print("You realize this tunnel is leading to nowhere and close your eyes, wishing for an escape.")
    sleep(delay)
    choice = 2

# TODO Don't forget to check if your user is dead at the end of your chapter!
if choice == 0:
    print("You collect your treasure and you move on to the next part of the cave")
elif choice == 1:
    print("You die, try again to test your fate again!")
else:
    print("You open your eyes and you are in a new place. You are alive, but somewhat bored and disappointed.")

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
