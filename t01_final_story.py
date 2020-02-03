######################################################################
# Author: Spring 2020 Class
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

delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!
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
#FIXME: TEAM 1

print("\nYou have found a room that appears to be some goblin's kitchen.")
print("Inside the kitchen are some strange meats, and a kiwi.")
choice = input("Do you eat something, or continue on?[meat/kiwi/continue] ")
if choice == "kiwi":
    print("\nYou feel revitalized. ")
elif choice == "meat":
    print("\nDaring aren't you? You do understand goblins haven't invented refrigeration yet right?")
    choice = input("That meat looks rather spoiled, are you sure about eating it? [0=no, 1=yes] ")
    if int(choice) > 0:
        sleep(delay * 3)
        dead = True
        print("\nYou have died of dysentery. ")
        quit()
    else:
        print("Good call. You continue into the labyrinth.")
else:
    print("\nThat was probably wise. You continue into the labyrinth\n")

# TODO Don't forget to check if your user is dead at the end of your chapter!

#########################################################################################################
#FIXME: TEAM 2

print(
    "There is a thin beam of light coming from a hole near the top. From what you can tell, you're somewhere underground.")
print()
sleep(delay)
print("You can see a river in front of you. It's wide and fast, and the current looks dangerous.")
print("On the other side there is a passageway that leads to another room.")
print("There are some stepping stones, but they are far apart. It would be easy to miscalculate a jump.")
print("Far above your head, you see a stone bridge. You might be able to climb up to it and cross.")
sleep(delay*3)
print()
print("You can only see three options.")
print()
sleep(delay)
print("1- Try to wade across the river")
sleep(delay)
print()
print("2- Try your luck hopping across the stepping stones.")
sleep(delay)
print()
print("3- Try to climb your way to reach the stone bridge")
direction = input("Through which method do you wish to continue? [Wade/Hop/Climb]")

if direction == "Hop"" Hop"" Hop ""Hop ""hop"" hop""hop "" hop ":
    print("You decide to cross the river to the passageway on the far side through using the stepping stones")
    sleep(delay)
    print("When crossing the stepping stones you are having some trouble")
    print("The river has made the stones slick and them being spaced apart makes them difficult to cross")
    sleep(delay*2)
    print("Upon the jumping from the last stone to the riverbank closest to the far passageway you slip")
    sleep(delay*3)
    print("Somehow, miraculously you manage to just barely grab the edge of the riverbank but the river is strong")
    sleep(delay*4)
    print("Fighting the current you are close to being swept away, but your will to survive is stronger")
    print("You pull yourself onto the riverbank and take a deep breath knowing that you barely escaped death")
    print("You are tired, but you continue forward into the passageway in hopes of an escape")
    sleep(delay)

elif direction == "Climb"" Climb""Climb "" Climb ""climb""climb "" climb"" climb ":
    print("Knowing that it is perhaps the hardest way out you start climbing your way up to the stone bridge")
    sleep(delay)
    print("It is a treacherous climb but you reach the stone bridge without too much trouble when you start feeling")
    print("A Crawling Sensation")
    sleep(delay*3)
    print("A swarm of spiders starts climbs onto your hands and before you react they reach your elbows")
    print("Out of shock, fear and pain your grip on the bridge loosens and you start fall")
    sleep(delay)
    print("The light in the cavern is gone, you feel cold, and the pain fades away")
    dead = True
    sleep(delay*5)
else:
    print("Forgoing any other thoughts you decide to charge forth and wade through the river")
    sleep(delay)
    print("The river tries to sweep you away, but you are pretty sure you are better than it so you go on")
    sleep(delay*2)
    print("Apparently you were wrong and you start getting swept downstream while uttering a string of curses")
    print("You pass out...")
    sleep(delay*2)
    print("You wake up in a cavern full of glowing moss and only one entryway")
    print("In the room's center there is a fire pit with a blue flame within")
    print("You make use of the fire to dry off")
    sleep(delay*3)
    print("The sight of the beautiful moss fills you with determination, and the heat of the fire gives you strength.")
    sleep(delay*3)
    print("Once you are well rested and dry you leave the cave")


if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
#FIXME: TEAM 3

direction2 = input("Which direction would you like to go this time? [UP/DOWN/LEFT/RIGHT]")

if direction2 == "RIGHT":
    # The worse choice possible
    print("I don't think you wanted to go deeper into the cave did you?")
    print("You will surely get eaten by bats...eeekkk!")
    print("...and snakes too...hssssss!")
    print("I pity you!")
    dead = True
    sleep(delay)
elif direction2 == "LEFT":
    # Good Choice
    print("Can you see the sun?")
    print("You found your way out!")
    print("Food and water are awaiting for you at the exit!")

else:
    #Neutral
    print("You are not going anywhere!")
    print("You are going to bump your head and crack it open or break your tailbone if you do this.")
    print("Ouch!")
    print("You are stuck here forever and ever!")
    sleep(delay)

if dead == True:
    print("Oh no! You kicked the bucket without making a bucketlist!")
    quit( )

#########################################################################################################
#FIXME: TEAM 4

direction = input("You were walking and faced 5 portals in front of you with different colors. Which portals will you choose? [Blue/Red/Yellow/Black/White]")

if direction == "Blue":
    print("Wooww! Great choice! There is a box of GOLD waiting for you behind this portal!")
    sleep(delay)

elif direction == "Red":
    print("The sound of tigers deprived of food for weeks surrounds you.")
    sleep(5)
    print("The smallest footstep could trigger them and send them into a frenzy.")
    sleep(5)
    print("You try to step away but you trip and cut yourself.")
    sleep(5)
    print("With the smell of blood in the air, the tigers pounce, ripping apart your flesh.")
    sleep(5)
    print("You are dying, but you can still save your life by solving the challenge")
    sleep(5)
    print("If you are smart enough, you can still survive!")
    sleep(5)
    print("So, ready for the challenge?")
    sleep(5)
    logic = input("Look at this series: 80, 10, 70, 15, 60, ... What number should come next?")
    if logic == "20":
        print("Wonderful! With the help of your logical skills you survived!")
        sleep(5)
        print("You are in the farm now. Continue your journey!")
    else:
        dead = True

else:
    print("You are in the farm now. Continue your journey!")

if dead == True:
    print("Sorry! You died and this is the end of your story////  Try again by hitting the green play button.")
    quit()

#########################################################################################################
#FIXME: TEAM 5

sleep(3)
print("You close your eyes for a brief second. As you do, you feel the wind swirl violently around you.")
sleep(4)
print("You open your eyes to find yourself in the middle of a dark forest.")
sleep(3)
from random import* #Code needed to import randomness
Escape = False #Used to check if the player has escaped yet
while(Escape == False and dead == False):
    DoorA = randint(1, 3) #Assigns a random number to DoorA
    DoorB = randint(1, 3) #Assigns a random number to DoorB
    DoorC = randint(1, 3) #Assigns a random number to DoorC
    while ((DoorA == DoorB) or (DoorB == DoorC) or (DoorC == DoorA)): #Rerolls all values of the doors until they aren't equal.
        DoorA = randint(1, 3)
        DoorB = randint(1, 3)
        DoorC = randint(1, 3)
        #print("Another Iteration" + "\n")
    #print(str(DoorA) + str(DoorB) + str(DoorC))
    print("Every instinct you have is telling you to get out.")
    print("You start walking through the forest until you spot something in the distance.")
    sleep(5)
    print("You see a row of doors in the bark of trees that could lead you out of the forest." +
          " Which door do you enter (Door A, B, or C)?")
    Choice = input("Pick one ")
    if(Choice.upper() == "A"):
        print("You go through Door A")
        sleep(2)
        if(DoorA == 1):
            print("You find a long windy path and decide to follow it.")
            sleep(delay * 3)
            print("You've died of starvation")
            sleep(3)
            dead = True
        elif(DoorA == 2):
            print("You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
            sleep(3)
            print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                  "until the morning.")
            sleep(5)
            print("You wake up to find yourself in the middle of a dark forest.")
            sleep(1)
        else:
            sleep(1)
            print("You follow a long tunnel")
            sleep(2)
            Escape = True
    elif(Choice.upper()=="B"):
        print("You go through Door B")
        sleep(2)
        if(DoorB == 1):
            print("You find a long windy path and decide to follow it.")
            sleep(delay * 3)
            print("You've died of starvation")
            dead = True
        elif(DoorB == 2):
            print("You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
            sleep(3)
            print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                  "until the morning.")
            sleep(5)
            print("You wake up to find yourself in the middle of a dark forest.")
            sleep(1)
        else:
            sleep(1)
            print("You follow a long tunnel")
            sleep(2)
            Escape = True
    elif(Choice.upper()=="C"):
        print("You go through Door C")
        sleep(2)
        if(DoorC == 1):
            print("You find a long windy path and decide to follow it.")
            sleep(delay*3)
            print("You've died of starvation")
            dead = True
        elif(DoorC == 2):
            print("You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
            sleep(3)
            print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                  "until the morning.")
            sleep(5)
            print("You wake up to find yourself in the middle of a dark forest.")
            sleep(1)
        else:
            sleep(1)
            print("You follow a long tunnel")
            sleep(2)
            Escape = True
    else:
        print("You pass out from thinking too hard. Good job.")
        sleep(2)
        print("You wake up to find yourself in the middle of a dark forest.")
        sleep(2)
if(dead== False):
    sleep(1)
    print("Yay you Escaped!")
#########################################################################################################
#FIXME: TEAM 6

doors = input("which doors you want to open? [A/B/C/D]")
import time
if doors == "A":
    # this is a very bad choice
    print("There is Samara standing with a Axe and she is not friendly")  # Samara Morgan is a scary character from the ring movie
    print("seems she is very angry and start running towards you")
    sleep(delay)
elif doors == "B":
    # this a good choice
    print("There is a treasure hidden in one of the thousand boxes")
    sleep(delay)
    print("There are danger warning signs on some of the boxes")
    print("seems the best option is not to open the boxes and stay in the room for safety or go back to the main area to choose another door to find the exit")


    print("You select one of the random boxes.")
    time.sleep(4)
    print("Congratulations!! you got the treasure")
elif doors == "C":
    # this door is another bad choice
    print("This door doesnot seem to be safe, because there are groups of hungry zombies in the room ready for attack")
    print("The door is closed and there is no way out, you are trapped!!")
    print("You try to fight the zombies with the broom stick, the only weapon in the room to fight the zombies")
    print("They eat you, you are gone! They are still hungry. ")
    print("Nice try though. try next time wisely!!")
    dead = True
else:
    # This the exit
    print("This is your way out of this haunted house. Well done.")
if dead == True:
    print("You have been sucked dry by the hungry zombies. Try again by hitting the green play button")

#########################################################################################################
#FIXME: TEAM 7

username = input("What's your name?")

print()
print("Welcome,",username,)
sleep(delay)
print("You have now randomly teleported to a village")
print("There are two people approaching you")
print("Someone who seems to want to sell you something and someone who wants to ask for money")
choice = input("Who do you want to talk to? [Seller or Beggar]: ")

if choice == "Seller":
    print("The Seller tackles you and steals all your money")
    sleep(delay)
    print("You are now a beggar and can no longer feed yourself properly; therefore, you die of starvation")
    dead = True

elif choice == "Beggar":
    print("You have chosen the generous route. Good Karma comes your way.")
    print("You leave the village in good spirits")

else:
    print("Please choose who you would like to talk to")

if dead == True:
    quit()
#########################################################################################################
#FIXME: TEAM 8

delay = 1.0
username= input("what is your name, idiot?")
print("welcome ",username,"to the portal" )
direction= input("Before you stand two doors, pick your destiny, door 1 or door 2, what's it gonna be, stupid?")

if direction == "door 1":
    print("You ended up in an old shack infested with rabid raccoons.")
    sleep(delay)

    print("You were mauled, but you bravely fended them off")
    sleep(delay*2)
    print("losing a lot of blood and a finger in the process.")

elif direction== "door 2":
    print ("You are in the house of sins, The Ladies of the Night")
    sleep(delay)
    print("you could not pay for the services")
    sleep(delay*5)
    print("too bad, you got yourself killed")
    dead= True
if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
#FIXME: TEAM 9

if direction  == "West":
    print("You stumble upon a pile of treasure ")

    question = input("Do you take all the treasure? (Yes/No")
if question == "Yes":
    print("You are greedy and get attacked by a mob of mummies.")
if question == "No":
    print("You are encountered by a mummy that allows you to take as much gold as you can fit in your pockets. Good job for not being greedy.")
    print("")

#########################################################################################################
#FIXME: TEAM 10

door_options = input("do you want find a treasure?Enter[door1/door2/door3/door4]")
# oh..lucky choice
if door_options == "door1":
    print(" you find a box full of pirate lost treasure, Congratulations for being brave..")
    sleep(delay)
# bad option
elif door_options == "door2":
    print("wrong destination, you saw a lion sleeping  and  you  fake dead. ")
    sleep(delay)
    print(" lion think  you are a bad meat to eat but want to know you are dead.")
    print(" oh! the lion is approaching you and waking up s not a good idea.")
    print("the lion find out you are breathing, Goodbye my friend the lion eats you.")
    dead = True

else:
    # Neutral choice
    print("Oh! you opened a wrong door and you fall into a pit, you are crying that you need help.")
    sleep(delay)


if dead == True:
    print("you are dead, click on the green play button to resurrect. if you want to play again.")
    quit()
#########################################################################################################
#FIXME: TEAM 11

if direction == "North":
    print("The stranger recognises this part of the cave. They could come in handy. ")
    sleep(delay)
    print()
    print("You have come across another split in the cave. The other person is starting to act weird. ")
    print("You can go East or West. The stranger seems to want to go West, but do you trust them? Choose wisely. ")
    sleep(delay)
    print()

trustworthy = input("Do you find them trustworthy enough to trust their advice to go West? [Yes/No]")

# Good choice
if trustworthy == "Yes":
    print("Lets hope this is the right thing to do...")
    sleep(delay)
    print("You find a chest")
    sleep(delay)
    print()
    print("You open it. It's filled with treasure!")
    sleep(delay)
    print()
    print("When you open the treasure, a boulder moves and reveals another path with light at the end.")
    print()
    sleep(delay * 3)
# Bad Choice
if trustworthy == "No":
    print("You decide to not trust the stranger and head East instead. ")
    sleep(delay * 2)
    print("The cave seems to be unstable and weak compared to the previous part of the cave.")
    sleep(delay * 2)
    print("The stranger sees a pretty rock in the cave side and decides to try and pull it loose. ")
    print()
    sleep(delay * 3)
    print("The rock comes loose. Suddenly rocks start coming loose from the ceiling of the cave. The stranger started "
          "a collapse in the cave system.")
    print("You can't move fast enough to escape the falling rocks and get crushed. ")
    print()
    dead = True

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
#FIXME: TEAM 12

instrument = input("Which instrument would you like to play? [Piano/Guitar/Bass/Drums]")

if instrument == "Piano":
    #Correct choice
    print("You have chosen the beautiful melodic instrument of Beethoven. You will be able to seduce any woman or mans as soon as you play...")
    sleep(delay)
elif instrument == "Bass":
    #Wrong choice
    print("You have chosen a demonic instrument. Begin to play the instrument you have chosen")
    sleep(delay)
    print("BOOM!!!!! As soon as you begin to play, the strings un-wire and wrap themselves around your neck")
    print("I bet you can't breathe now, can you? HAHAHAHAHA")
    sleep(delay)
else:
    #Regular choice
    print("The musician Gods have granted you passage to continue. Play on!")
    sleep(delay)

if dead == True:
    print("Wow you suck! Too bad buddy. Next time don't die")
    quit()

#########################################################################################################
#FIXME: TEAM 13

direction = input("Which cave tunnel do you want to go down? [Left/Right/Straight]")
if direction == "Left":
    # Good choice!
    print("You have found a baby dragon. It's fire can keep you warm and it can lead you out of the cave.")
    sleep(delay)
elif direction == "Right":
    # Oh no...BAD CHOICE!
    print("Oh no. You have run into 100 duck-sized horses.")
    sleep(delay)
    print("They are vicious and out for blood.")
    print("They begin to stampede and knock you off your feet...never to be seen again.")
    dead = True
else:
    # Neutral choice
    print("You find yourself in a mineshaft, not seeing a way out. While quite interesting, still not the way out.")
    sleep(delay)
if dead == True:
    print("Oopsy. You made a whoopsy. Better luck next time! Play again by hitting the green play button.")
    quit()
#########################################################################################################
#FIXME: TEAM 14

doors = input("You come across three doors. Which door will you open? The left, middle, or right door?")
print()
if doors == "Left":
    print("As you walk, you trip on a rock.")
    print("In front of you, there was a water well.")
    print("You fall into the well and start calling for help.")
    sleep(delay)

    print()
    dead = True
elif doors == "Middle":
    print("In front of you is a long tunnel.")
    print("You walk for hours and hours, but never come to an end.")
    print("Eventually, you pass out from exhaustion, and your world goes black.")
    print()
    sleep(delay)
else:
    print("You walk into a grass field, and as you walk, you see a farm off into the distance.")
    print("You see people milling about near the farm, and decide to walk towards it.")
    print("Your journey takes a little bit of time.")
    print()
    sleep(delay)

if dead==True:
    print("You've died. RIP")
    print("That's the end of your story.")
    quit()

#########################################################################################################
#FIXME: TEAM 15

print("You are walking through a field, and seemingly out of nowhere a forest appears before you.\n")
sleep(delay * 2)
print("You know that you have a few options, but one must be made.")
print("Would you like to... \nA: Go around the outskirts of the forest, B: Go into the forest, or C: Just stand there")
forest_choice = input("[A,B,C]")

if forest_choice == "A":
    # Good Choice
    print("You make it around the forest with no consequence.")
    sleep(delay)
elif forest_choice == "B":
    # A very bad choice
    print("As you enter the forest you realize that something seems a little off.")
    sleep(delay)
    print("As you make your way deeper into the woods you find that it becomes progressively harder to breathe in the\n"
          "air.")
    sleep(delay)
    print("Suddenly as if all at once you realize that you are suffocating. You fall to the ground clasping at your \n"
          "throat.")
    dead = True
else:
    # Neutral choice that makes your character look stupid
    print("You stand there... ")
    sleep(delay * 3)
    print("Boredom fills your mind...")
    sleep(delay * 3)
    print("Eons pass by as you wait at the edge of the woods. Eventually you forget why you are standing there.")
    sleep(delay * 3)
    print("You blink, and suddenly the forest disappears. \n")
    sleep(delay)
if dead == True:
    print("Whoops, you died in the forest. Start over by clicking the green play button. ")
    quit()
#########################################################################################################
#FIXME: TEAM 16

wait = 2.0
dead = False
username = input("Who dares to enter this holy place?")
print()
print("Welcome,", username, "to Wakanda.")
sleep(wait/2)
choice = input("What are you here for?")
print()
print("Oh!", username, " you are in luck, we happen to have", choice, "in Wakanda.")
sleep(wait*2)
print("But before we attend to you, you must drink from these bowls.")
print("The red bowl, the blue bowl, and the green bowl.")
print("But beware!! One of these bowls will kill you. So, choose wisely!")
print()
sleep(wait)
#########################################################################################################
#FIXME: TEAM 17

chosen = input("Which bowl do you wanna drink from? [Red/Blue/Green]")

if chosen == "Red":
    # Bad choice
    print("Sorry but we are gonna make you a good funeral.")
    sleep(wait)
    dead = True
elif chosen == "Blue":
    # Not a good choice.
    print("Sorry but we cannot get you what you want")
    print("You must leave this place at once!")
elif chosen == "Green":
    # Good choice
    print("Congratulations! You have the chance to see the king of Wakanda.")
    print("He has the power to give you the", choice, ".")
else:
    # Good Choice
    print("Sorry, we do not have your request.")
    print("However, thank you for your interest.")
if dead:
    print("Oh no! Better luck next time! Try again by hitting the green button")
    quit()
#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
