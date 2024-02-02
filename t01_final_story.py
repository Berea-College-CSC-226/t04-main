######################################################################
# Author: Spring 2024 Class
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
#
# NOTE: Because of weather, T01 wasn't completed. You are modifying a previous classes' T01.
######################################################################
from time import sleep

#########################################################################################################
# TEAM 1
delay = 1.0
isDead = False

username = input("What is your name?")
print()
sleep(delay*2)
print("welcome", username, "to fruit Land")
print("you will be given three fruits and you can only choose one")
print("Be careful the choice you make ")
print("one will give you fortune, one will lead to death, and one is just a normal fruit")
sleep(delay*2)

Fruit = input("which fruit would you like? [Banana, Orange, Apple] ")

if Fruit == "Banana":
    print("unfortunately, you've chosen the rotten fruit, this is the end of your journey!")
    isDead = True
elif Fruit == "Orange":
    print("you've chosen the special fruit, you've earned ")
# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 2

print("It's Wednesday morning. You wake up at 10:30am and see the sun through your window")
print("Suddenly, you realize that you are almost late for your CSC 226 class at 10:40am ")
print("You know you need your morning coffee to get through the day, but you are almost late for class")
sleep(delay)
decision = input("coffee or class?")

if decision == "coffee":
      #good choice
      print("you drink your coffee and run to class")
      sleep (delay)

elif decision == "class":
#bad choice
      print("You manage to get in class at 10:41am")
      sleep(delay)

      isDead = True

if isDead == True:
      print("although you made to class in time, you cannot stay awake.")
      sleep(delay)
      print()
      print("in an attempt of helping you, Nick throws coffee in your face")
      print("accidently, he kills you")
      quit()

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 3
print("\n")
print("You find a room that contains two gold statues.")
sleep(delay)
statues = input("Do you take the left or right statue, or don't pick up the statue?: ")
print("\n")

if statues == "left":
    #good choice
    print("You pick up the statue on the left.")
    sleep(delay)
    print("A passageway opens and you see outside.")
    print("Congrats! You escaped the cave!")
    sleep(delay)
elif statues == "right":
    #bad choice
    print("You pick up the statue on the right.")
    sleep(delay)
    print("A passageway opens above you.")
    sleep(delay)
    print("A bunch of snakes and spiders fall on you!")
    isDead = True
    sleep(delay)
else:
    #neutral choice
    print("You don't pick up either of the statues.")
    sleep(delay)
    print("Nothing happens... You are still stuck in the cave.")
    sleep(delay)

# TODO Make sure to add the additional check if the user makes the "bad" choice!
if isDead == True:
    print("\n")
    print("One of the snakes asks you to pick a number 1 through 20.")
    sleep(delay)
    number = int(float(input("Which number do you pick? (only put whole numbers): ")))
    sleep(delay)
    if number >= 13:
        print("Congrats! The snake decided to spare you!")
        isDead = False
        sleep(delay)
    else:
        print("You chose a wrong number, which angers the snake. He and the other snakes and spiders bite you!")


# TODO Don't forget to check if your user is dead at the end of your chapter!
if isDead == True:
    print("Oh no! You died! Try again by hitting the green play button.")
#########################################################################################################
# TEAM 4
print()
print("Welcome,", username, ", to Generic Fantasy College™.")
sleep(delay)
print("You are awoken by your alarm")
print("It is 8:00AM")
print()
sleep(delay * 2)
print("Looking through your window the sky has a magenta hue")
print("Staying here is certainly not wise. You must find your way out.")
print("\n")
sleep(delay)

sleepChoice = input("Do you wake up, be late, or sleep?")

if sleepChoice == "wake up":
    #Good Choice
    print("You go to classes and are a productive member of society")
    sleep(delay)
elif sleepChoice == "be late":
    #Neutral Choice
    print("You miss breakfast and your day is stressful")
    sleep(delay)
else:
    #Bad Choice
    print("You here the sound of wings flapping in the distance")
    sleep(delay)
    print("You know you fucked up")
    sleep(delay)
    deathChoice = input("On a scale of 1-10, how much do you want to stay at Generic Fantasy College™")
    if deathChoice == "<3"
    print("The dean whomst happens to be a fire breathing dragon roasts you alive for not attending Generic Fantasy College™")
    isDead = True
    sleep(delay)

if isDead == True:
    print("If only you would've gone to class, Try again by hitting the green play button.")
    quit()
#########################################################################################################
# TEAM 5
print("\n")


chalice = input("Hello intrepid explorer! You have stumbled upon The Flying Dutchman's lost treasure! Before you lie 4 colored chalices, however, you can only choose one. Choose wisely! [Gold/Silver/Bronze/Brass]")

if chalice == "Bronze":
    # Good choice!
    print("Excellent choice, wise explorer! The Bronze chalice grants you a life filled with resilience and courage. You have proven to have a heart as unyielding as bronze! May you forge onwards with the spirit of a warrior.")
    sleep(delay)

elif chalice == "Gold":
    # Oh... Bad choice
    print("As you reach out and touch the gold chalice, a chilling breeze fills the cavern.")
    sleep(delay)
    print(
        "Suddenly, the cavern trembles and the chalice levitates, emitting a blinding light. A voice booms, 'Dare you to tempt fate? Roll the dice and let destiny decide your path.'")

    roll = int(input("Roll the dice (enter a number between 1 and 20): "))

    if roll <= 5:
        print("You roll the dice... it's a low number.")
        sleep(delay)
        print(
            "The ground shakes violently as the cave begins to collapse. Unfortunately, you are unable to escape in time, meeting a tragic end. The treasure remains unclaimed, lying amidst the ruins of the cavern.")
        isDead = True
    elif roll <= 10:
        print("You roll the dice... it's a moderate number.")
        sleep(delay)
        print(
            "The cavern stops trembling and the path you came from reopens, allowing you a gracious yet narrow escape. It appears you've been given a second chance, but the golden chalice remains elusive.")
    else:
        print("You roll the dice... it's a high number!")
        sleep(delay)
        print(
            "A hidden pathway illuminated by golden light suddenly appears, leading you to a secret chamber filled with unimaginable treasures. It seems luck is on your side, brave explorer!")

else:
    # Neutral choice
    print("You find yourself wandering into a hidden cove within the cave, the ground here is covered in sand and you can hear the distant sound of lost souls.")
    sleep(delay)
    print("You see remnants of old pirate camps, and signs of many stories that remain untold in this isolated refuge of the Flying Dutchman's cavern.")

if isDead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 6
Path = input("Which path will you take? [Left/Middle/Right]")
SecondChance = input("Do you want another chance? [Yes/No]")

if Path == "Left":
    # Wrong Path
    print("Sss....sss...sss...")
    sleep(delay)
    print("You have encountered a python.")
    print("Oh no! The python has bitten you.")
    print("You are now slowly dying from the poison.")
    print("Do you want another chance?")


elif Path == "Middle":
    # Neutral Path
    print("The path is never-ending.")
    print("You continue walking through the cave.")

else:
    # Correct Path
    print("drip...drip...drip")
    print("You arrived at a water faucet and met a fellow adventure!")
    print("You can now continue your adventure.")
    sleep(delay)

if isDead == isDead:
    print("You are now dead!You can try again after hitting the green play button. ")
    quit()


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 7
input("Go with him further [Up, or Down]?")
if direction == "Up":
    print("You've reached a large vault... a large console stands to its right...")
    print("The console lights up when you reach it... it asks for a passcode")
input("Guess the code/Ask for help")
if "Ask for help":
    print("You ask Dr. Heggen for help")
    print("He pulls out a small electrical device and plugs it into the console")
    print("The console glows green and the vault opens up")
    print("you've found riches beyond your wildest dreams")
elif "Guess the code":
        print("You type in '12345' and the console turns red")
        print("The walls close in on you, crushing you like a Wookie in a trash compactor")
        isDead = True









elif direction == ("Down"):
    print("you have reached the strongest creature in all of the lands..")
    sleep(delay * 3 )
    print("It is the Teacher Assistant Silas! Do you fight or run?")


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 8

print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lie two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print("\n")
sleep(delay)

print("Up ahead is a lit chamber with 3 doors, one to the East, one to the North, and one to the West.")
cardinal = input("Which door will you choose?")
if cardinal == "East":
    # GOOD !!!
    print("Fortune favors you! The door you have chosen is filled to the brim with treasures unimaginable in this world!")
    sleep(delay)
elif cardinal == "North":
    # Not A Good Choice
    print("Behind the door lies a small snake that upon seeing you starts to grow!")
    print("As you run away, the snake chases you as it continues to grow, expanding to fill everything behind you as your path ahead leads to a dead end...")
    sleep(delay)
    luck = random.randint(0,10)
    print(luck)
    if luck <= 5:
        print("There is no escape...")
        isDead = True
    elif luck > 8:
        print("As the snake grows, the cave roof starts to collapse onto it, killing the snake, but trapping you forever...")
    else:
        print("As you press against the wall, you feel it fade away as you are transported to nothingness as you slowly become part of it...")
        isDead = True
else:
    # I mean you're not dead
    print("You are now in the middle of an island alone forever, enjoy !!!")
    sleep(delay)
# TODO Make sure to add the additional check if the user makes the "bad" choice!
if isDead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()
# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 9
if direction == "North":
    print("Now you have to complete three treacherous trials with the other person in the cave. Each more arduous than the last.")
    print("The first trial is you must befriend and then destroy a sneaky salamander. [Yes, No]")
if direction == "yes":
    print("Congratulations you can proceed to the next trial. The next trial you have to go find the other person in the cave with you and make them poke a grizzly bear. [Yes, No]")
if direction == "no":
    print("Due to your declination, you will now be forced to leave the labyrinth.")
    isDead = True

# picking the neutral choice
else :
    #neutral choice
    print("Now you are presented with two choices. One direction could lead to your death and the other solution is unknown")

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!

#########################################################################################################
# TEAM 10
print("A cave guard appears at the cave entrance")
sleep(delay)
action = input("Should you: [Talk/Ignore/Punch] him?")
print("\n")

if action == "Talk":
    #good choice
    print("Greeting Traveler, didn't see you there.\nIt's awfully dark in there.\nIf you want to reach the "
          'treasure,\nyou must answer my riddles and there will be light to guide you.')

if action == "Ignore":
    #first neutral choice
    print("You ignore the cave guard and walk past him.")
    print("You're still lost and it's still dark. Maybe he knows how to fix that.")

elif action == "Punch":
    #bad choice
    print("Uh oh. The cave guard didn't appreciate that...")
    sleep(delay)
    print("You hear a sword unsheath.")
    sleep(delay)
    print("Before you can even think about running, you're sliced and diced into pieces. Ouch.")
    sleep(delay)
    isDead = True

else:
    #idk what the user typed in but it was definitely not a choice
    print("Nothing happens. That wasn't even an option. Try again.")

    if isDead == True:
        print("You are dead. Make a better choice next time.")
        quit()

print("The cave guard asks you the riddle: I am thinking of a number 1 through 10. If you guess correctly, you are on your way to the treasure!")
number = input("What number am I thinking of? [int>0]")
if int(number) >= 5:
    print("You answered correctly. The cave guard gives you flashlight.")

elif int(number) <= 5:
    print("That is incorrect.")
    print("The cave guard unsheaths his sword and slices you.")
    isDead = True
if isDead == True:
    print("You are dead. Make a better guess next time.")
    quit()


#TODO Make sure to add the additional check if the user makes the "bad" choice!

#TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 11
from time import sleep

delay = 2.0
isDead = False


username = input("Hello player, why don't you start off by telling us what your favorite color is? ")

print()
print("Ok player! You will be driving a",username,"car.")

sleep(delay)

print()
print("You're heading to Walmart and you're low on gas, make the right turns to the gas station to fuel up!")
print("\n")
sleep(delay)
# print("You're pulling up to Main st, the light is green. Would you like to take a left or right? [Left/Right]")





direction = input("You're pulling up to Main st, the light is green. Would you like to take a left or right? [Left/Right/Continue] ")


if direction == "Left":
        # Correct
    # print("Great, you just took a shortcut! You're almost near. Would you like to continue straight? [Yes/No]")
    sleep(delay)

    direction = input("Great, you just took a shortcut! You're almost close. Would you like to continue straight? [Yes/No] ")
    print("\n")
    if direction == "Yes":
        # Correct
        print("Hooray! You have arrived at the gas station and were able to fuel up!")

    elif direction == "No":
    # Incorrect
        print("You missed the entrance to the gas station and ran out of gas. Better luck next time.")
        isDead = True
        sleep(delay)

elif direction == "Right":
      # Incorrect
    print("Well looks like you took the wrong turn and ran out of gas sorry.")
    sleep(delay)
    print("Try again next time!")
    isDead = True

else:
      # Neutral Choice..
     print("Oops, you missed the entrance and your gas is still running LOW! ")
     sleep(delay)

     print("ALERT! You are out of gas, better luck next time taking turns correctly!")
     isDead = True


# elif direction == "No":
#     # Incorrect
#     print("You missed the entrance to the gas station and ran out of gas. Better luck next time.")
#     dead = True

#########################################################################################################
# TEAM 12
global HasSword
global goblindead
######Intro
print("You stand in your makeshift campsite, a pitiful fire smoulders, sending black smoke to the sky.")
sleep(delay)
print("To the North: The Mystic Wood lies, fabeled to hold a great treasure.")
sleep(delay)
print("To the South: The Mouth of a cave, you can hear noises creep from within.")
sleep(delay)
print("To the West: A long road that you came from.")
sleep(delay)
print("To the East: A vast meadow of yellow flowers.")
sleep(delay)
############
direction = input("Choose a direction or action[Search the camp/North/South/East/West]: ")
###CHECK FOR VALID INPUT###
while direction != "north" and direction != "south" and direction != "east" and direction != "west" and direction != "search camp":
    print("Now", username, " That wasn't a valid option.")
    direction = input("Choose a direction or action[Search the camp/North/South/East/West]: ")

###Print string based on input###
if direction == "north":

    if goblindead==False:
        print("You go north.")
        sleep(delay)
        print("The trees tower over you almost nearly blocking out the sun.")
        sleep(delay)
        print("Suddenly a large goblin bandit jumps from the bushes roaring")
        sleep(delay * 3)
        ##check if user has sword
        if HasSword == True:
            print("The goblin lunges at you, your swords clash.")
            sleep(delay)
            print("You best the goblin, stabbing him in the chest.")
            print("You step over the goblins corpse, procceding deeper into the forest.")
            goblindead = True
            sleep(delay*3)
            room2()

        elif HasSword == False:
            print("The goblin rushes you, pulling back his arm for a mighty swing.")
            print("His sword makes contact with your neck, chopping it clean off.")
            death()
    elif goblindead == True :
        print("You go north.")
        sleep(delay)
        print("The trees tower over you almost nearly blocking out the sun.")
        sleep(delay*2)
        room2()

elif direction == "south":
    print("You go south.")
    sleep(delay)
    print("You approach the cave, and as you enter you here a loud growl.")
    print("A vicious bear appreaches from the darkness.")
    sleep(delay*3)
    if HasSword==True:
        print("You swing your sword, plunging it into the bear.")
        print("The bear screams in pain as it swats you like a fly, slinging against the cave wall.")
        print("Your head makes first contact with the wall, the blow kills you instantly")
        sleep(delay*4)
        death()
    elif HasSword == False:
        print("The bear roars and swats you like a fly, slinging against the cave wall.")
        print("Your head makes first contact with the wall, the blow kills you instantly")
        death()
elif direction == "east":
    print("You go east")
    room3()


elif direction == "west":
    print("You look at the road to the west, this is where you came from.")
    sleep(delay)
    print("There's no turning back now. You must find the treasure hidden in the forest")
    sleep(delay)
    room1()

elif direction == "search camp":
    print("You look around the camp for anything of interest.")


    sleep(delay)
    if HasSword == True :
        print("You don't see anything of interest - there's nothing here.")
        sleep(delay*3)
        room1()
    elif HasSword == False:
        print("You find your sword laying on a rock near the fire.")
        print(">>sword obtained!<<")
        HasSword=True
        sleep(delay*3)
        room1()

else:
    room1()
#########################################################################################################
# TEAM 13
from time import sleep

delay = 1.5
pieFace = False

username = input("What shall we call you? ") # asking for user's name
print("\n")

print()
print("Welcome,", username, ", to our yearly raffle!")
sleep(delay)
print("In front of you, we have presented you with five tickets. Choose a number from 1 to 5.")
print("Choose carefully!")
sleep(delay)

raffleTicket = input("Which ticket shall you choose? [1/2/3/4/5] ")

if raffleTicket == "3":
    # Good Choice
    print("Congrats! You picked the golden ticket!")
    print("You have won a delicious chocolate pie! Enjoy!")
    sleep(delay)
elif raffleTicket == "5":
    # Bad Choice
    print("Oh, no! Someone is out of luck today. Watch out for the flying whipped cream pie!")
    pieFace = True
else:
    # Neutral Choice
    print("Oh, no! You picked one of the right tickets, but we ran out of pies :( ")
    print("But lucky you, we still have some cupcakes! Enjoy!")
    sleep(delay)

if pieFace == True:
    print("This year was not your year. Come back and test your luck next time. Try again by hitting the green play button.")
    quit()

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 14
if direction == "North":
    print("You didn't die. In fact, you made it out of the cave and back into society. Yay.")
    sleep(delay)
elif direction == "South":
    print("You unfortunately fell off a cliff and are about to die.")
    isDead = True
    sleep(delay)
else:
    print("You're still in the cave, and no closer to being out of it. Sucks to be you.")
    sleep(delay)
if isDead == True:
    numbertest = input("Pick a number 1-10 to try and survive.")
    numbertest = float(numbertest)
    if numbertest > 5 and numbertest <= 10:
        isDead == False
        print("You got lucky this time.")
    else:
        print("Unlucky, you're dead. Very sad")
        quit()

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 15
opponent = input("Who will you choose for your opponent? (Scott/Tojo/Bystander")

if opponent == "Scott":
    #bad choice
    print('''As he steps into the ring he make nervous eye contact with you. He says "I was hoping no one would choose me, I didn't want it to come to this"''')
    sleep(delay * 3)
    print("Within a millisecond he teleports behind you wrapped around your waist and suplexes you, snapping your neck on the hard cold unforgiving concrete floor")
    print("Dr.Scott has killed you")
    isDead = True

elif opponent == "Tojo":
    #good choice
    print("You get in the ring with Tojo. You notice he's moving a little slow and creaky.")
    print("Turns out he overdid it on the bench press before the fight. You easily throw him to the ground.")
    print("Unable to properly use his arms, he can't get up and is tapped out.")
    sleep(delay)

else:
    #nutral choes
    print("The fellow student you fight happens to be on the exact same level as you so you tie.")
    print("You have to try fighting them again  at the next BWT")
    sleep(delay)

if isDead == True:
    print("oh no! You have died, hopefully there is no wrestling in the afterlife!")
    quit()

#########################################################################################################
# TEAM 16
direction = input("Which direction would you like to go? [Left/Right/Forward/Backward]")

if direction == "Left":
    print("You stumbled on a torch, pick it up and press the button to light it.")
    print("You will see two paths in front of you.")
    print("You use the light from the torch you found to guide you out of the cave into the tulip garden full of people")

elif direction == "Right":
    print ("You step on a fox's tail.")
    choice = input("Would you run or stand still? [Run/Stay]")
    if choice == "Run":
        print("You run into two kind strangers, who lead you out of the cave.")
    elif choice == "Stay":
        print("You get attacked by the fox, he invites his friends and they all have a nice dinner.")


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!

#########################################################################################################
# TEAM 17
if count == 10:
    print("You look at the figure and it turns out to be your best friend, Katie!")
    print("Katie wants to hand you a demonic sword.")
    sword = input("Do you accept the sword: Yes/No: ").lower()
    if sword == ("yes"):
        print("You unlock a special power: Super Strength!")
        count = 11
    else:
        print("Katie stabs you!")
        isDead = True

if count == 1:
    print("You enter into a hallway and meet a dog.")
    dog = int(input("Would you like a companion? Use 1 or 2, with 1 being correct and 2 as wrong: "))
    if dog == (1):
        print("Congratulations! You have earned a doggy pet!")
        count = 11
    elif dog ==("2"):
        print("The dog got sad and ran away crying.")
        count = 3
    else:
        print("The dog did not like your answer, and you got bit.")
        print("You are a terrible human.")
        isDead = True

if count == 11:
    print("You go down a crevice in the wall.")
    print("You found a treasure chest in a hole, but you can't reach your arm in.")
    if dog == (1):
        print("Congrats! The dog opened the chest and found money!")
    elif sword == ("yes"):
        print("Congrats! Your sword was long enough to reach the chest! You found money!")
    else:
        isDead = True
if count == 3:
    print("The dog brought back a monster. There is no escape!")
    isDead = True

if isDead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()


#########################################################################################################
# TEAM 18
isDead = False

username = input("What is your name? ")
print("Welcome," ,username, ", to the woods.")
sleep(delay *3)
print("Before you wait too long choose a direction that will let you escape.")
print("You can take one of the four directions.")
direction = input ("Which direction in the woods would would you like to take? [north, south, east, west]")
if direction == "North":
    print("You are safe, you get back home.")
    sleep(delay)
elif direction == "South":
    print("You met the cannibal tribe")
    isDead=True
elif direction == "West":
    print("You fell off a cliff.")
    isDead=True
else:
    print("You got bitten by a poisonous snake.")
    isDead=True
if isDead == True:
     print("Oh no! you are dead. Sorry good luck next time. Hit the run button to play this game again.")
     quit()
