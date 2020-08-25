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
# TEAM 1
direction = input("Which direction are you thinking to take now? [North, South, East, West]")
if direction == "East":
    print("You meet up with a Mariachi band who then starts following you")
    sleep(delay)
    print("They begin to play and it's so loud that your location is compromised")
    print("You are approached by a rogue team of explorers.")
    print("They rob you of your resources and leave you for dead")
    dead = True
elif direction =="West":
    print("You stumble into a pit of mutated venomous snakes")
    sleep(delay)
    print("Your chances of survival = 0")
    dead = True
else:
    #lucky choice
    print("You somehow manage to make it out alive and land on a cotton candy trampoline that leads you to a mysterious place.")
    sleep(delay)
    print("Good luck")
if dead == True:
    print("Tough luck. Enjoy the afterlife.:)")
    quit()

#########################################################################################################
# TEAM 2
Name = input(" What is you are name, warrior? ")
Choice = (input(" What is your choice of sword today, warrior? [Cane or Claymore ] "))
dead = False
if Choice == "Claymore":
    print(" Good choice! " + Name)
    sleep(delay)
    print(" You ready to begin your day ")
    sleep(delay)
    print(" This sword is known to be one of the deadliest ")
    quit()
elif Choice == "Cane":
    print(" Every warrior who have chosen this sword has died ")
    sleep(delay)
    print(" and that will be your fate ")
    print(" You have one more chance to make the right decision ")
    sleep(delay)
    Choice2 = int(input(" pick a number between 10 and 100 "))
    if Choice2 < 20:
        print(" You have lived to see another day ")
        print(" You ready to begin the day ")
    else:
        print(" you have made the wrong decision twice ")
        sleep(delay)
        sleep(delay(print(" you deserve to die in unimaginable way")))
        print(" You are no warrior, you shall be hang ")
        dead = True


else:
    print(" I guess you are not ready for an adventure today...")

if dead == True:
    print(" Just like the ones before you, your fate has been chosen ")
    quit()


else:
    print(" I guess you are not ready for an adventure today...")

if dead == True:
    print(" Just like the ones before you, your fate has been chosen ")
    quit()

#########################################################################################################
# TEAM 3
print("You continue along...")
sleep(delay*2)
print("You encounter a Thief mid-robbery, but he's having some trouble")
sleep(delay)
action = input("What do you do? [Stop/Run/Help]")
if action == "Stop": #good choice
    print("You attempt to stop the thief...")
    sleep(delay)
    print("You tackle the thief and pin him to the ground, and wait for the police.")
    sleep(delay)
    print("When the police arrive, they thank you for your service with a pink-sprinkled donut")
elif action == "Help": #bad choice
    print("You decide to help the thief...")
    sleep(delay)
    choice = int(input("Choose how much money you hold [whole number]"))
    if choice >= 1000000:
        sleep(delay*2)
        print("As the you run away, you are to slow and are shot down by the police")
        print("As you lie there dying you regret being greedy and taking too much money")
        dead = True
    else:
        print("You are quick enough to get away from the police")
        sleep(delay)
        print("Good Job, you weren't greedy and got away with some money")
        sleep(delay*2)
else: #neutral choice
    print("You run away from the scene not wanting to get involved, and continue on your journey")

# TODO Don't forget to check if your user is dead at the end of your chapter!

if dead:
    print("Oh no you died, you should have tried harder")
    print("press the green button to try again")
    quit()
#########################################################################################################
# TEAM 4
direction=input ("Which pathway would you like to take? [Rocky/Bumpy/Smooth/Round]")
if direction == "Rocky":
   #Good choice
    print("You see an open door and can see sunlight shining through.")
    sleep(delay)
elif direction == "Bumpy":
    #Neutral choice
    print("You run into a wall with a creepy painting.")
    sleep(delay)
if direction == "Smooth":
    #Bad choice
    print("As you walk through the pathway you see an valuable gemstone.")
    sleep(delay)
    print("Once you grab it the floor opens and you fall through.")
    print("Beneath you there is a sea of hungry piranhas.")
    dead= True
elif direction == "Round":
    #Neutral choice
    print("You stumble upon a locked door.")
    sleep(delay)

if dead == True:
    print("You are now dead, better luck next time. Maybe you should have chose another path.")
    quit()
#########################################################################################################
# TEAM 5
print("Within the cave there are blood thirsty vampire bats that are sleeping.")
sleep(delay)
print("You must make the choice to sliver into one of the many parts of the cave")
sleep(delay)
choose = input("Where do you choose to go? [left/center/right]")
if choose == "left":
    #Good choice!
    print("You move through the dark depths of the cave safely without waking the bats")
    sleep(delay)
    print("You see a light at the end of the treacherous cave")
    print("You've escaped!")
elif choose == "center":
    #Bad choice :(
    print("You trip over rocks and cut your knee open!")
    sleep(delay)
    print("You awaken the bats with the smell of your blood")
    sleep(delay)
    weapon=input("You pick up a sharp stick. How many bats can you take on at once?")
    weapon=int(weapon)
    if weapon < 2:
        print("You were attacked from behind and the bats ate you")
        dead = True
    elif weapon >= 2 and weapon <=5:
        print("You have managed to fight off the blood thirsty bats and you have survived")
    elif weapon > 5:
        print("You take on more bats than you can handle and become overwhelmed and die")
        dead = True


else:
    #Neutral choice
    print("Down this path, you get lost within the dark depths of the cave")
if dead == True:
    print("You've died :(")
    quit()
#########################################################################################################
# TEAM 6
my_destination = input("Which destination would you like to go? [Beach/McDonald's/Carnival]")
if my_destination == "McDonald's" or my_destination == "The Beach" or my_destination == "Amusement Park":
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
    elif my_destination == "Amusement Park":
        # if they choose amusement park!
        # Bad choice...
        print("You've arrived at the Amusement Park and it's BEAUTIFUL!!")
        print('')
        print("You see a crowd of people...what's going on??")
        print('')
        print("OH MAN! There's a kid and an old man fighting!!!")
        print('')
        my_choice = input("Do you want to stop them??")
        if my_choice == 'yes' or 'no':
            if my_choice == 'yes':
                print("You try to save the boy!")
                print("OH NO! THE OLD MAN HIT YOU IN THE HEAD WITH HIS CANE!!")
                print("You die from a concussion...")
                dead = True
            else:
                print("Guess that's none of your business...")
                print('')
                print("You need to use the restroom!")
                print('')
                print("You go into the nearest porta potty.")
                # Cue omninous music...
                print('')
                print("Oh no...you hear thunder while doing your business!!")
                print('')
                print("OH MY GOODNESS! THE DOOR WON'T OPEN!!")
                print('')
                print("OOHH NOO! THE WIND IS MOVING THE PORTA POTTY!!")
                print('')
                print("DEAR GOD!!! IT'S A HURRICANE!!!")
                print('')
                print("YOU'RE BEING LIFTED INTO THE AIR!!!")
                print('')
                print("YOU'RE FALLING!!!")
                print('')
                print("You tragically died from the impact")
                print('')
    elif my_destination == "the beach" or my_destination == "The Beach" or my_destination == "beach":
        # good Choice!!!
        #
        print("YOU FINALLY GOT OUT!")
if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()
#########################################################################################################
# TEAM 7
print("\n")
print("""Suddenly the earth beneath you rumbles..out of thin air three radiant portals emerge""")
print("\n")
sleep(delay *2)

print("""The light from the portals illuminates the cave but you reflexively close your eyes 
      in response to the harsh light.""")
print("\n")
print("""Few minutes pass and attempt again to get a better look at the portals. Light permeates through your
      partially opened eyes. To your surprise, the portals each lead to luxury stores""")
sleep(delay*2)
print("\n")
print("A voice bellows to you, leaving you slightly shaken")
sleep(delay)
print("\n")
print("Choose your luxury store wisely, unworthy adversary!")
store = input("Which store would you like to go?[Gucci / Chanel / Prada]")
if store == "Gucci":
    # Bad choice
    print("Welcome to the Gucci store,",username,"!")
    print("You begin to seach for your wallet ")
    wallet_location = input("Where is your wallet?[Pocket/Purse/Hand]")
    if wallet_location == "Pocket" or wallet_location == "Purse":
        print("Tough luck! You do not have any money, Please leave the store!")
    elif wallet_location == "Hand":
        print("You just spent $100,000 at Gucci...Your mom is going to kill you!!")
        dead = True
        if dead == True:
            print("Your mom killed you, please wear black at the funeral.")
            quit()
elif store == "Chanel":
    sale = input("Chanel is having a massive sale! Which items are you buying?[Shirts/Purses/Perfumes]")
    if sale == "Shirts" or sale == "Purses" or sale == "Perfume":
        print("You got over $40,000 worth of luxury items, for only $10,000")
        print("You are so Lucky!!!")
else:
    print("You have entered Prada ")
if store == "Prada":
    print("Welcome to Prada,",username,",Let me check to see if you have a membership with us?")
    print("\n")
    sleep(delay *2 )
    print("It appears that you do not have a membership with us..")
    sleep(delay)
enroll = input("Would you like to enroll?[Yes/No]")
if enroll == ("Yes"):
    print("The entry fee is $3000 and we have many on sale")
    print("\n")
    print("Thank you for your membership!")
    print("You shop around the store and gather your items and prepare to pay..")
    sleep(delay)
    print("\n")
    print("Welcome 50th customer, as a reward all of your items are free of charge!")
elif enroll == ("No"):
    print("Thank you for your time.")
    print("\n")
    sleep(delay)
    print("""As you make your way out of the store, a loose the ceiling of slap breaks apart from the topmost floor
    and it instantly flattens you""")
    print('\n')
    dead == True
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()
#########################################################################################################
# TEAM 8
path = input("Where would you like to go now that you've escaped the cave? [Bridge/Tower/Forest/River]")

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
    print("But, you're starving... And you come across a bush with blue berries! (That's blue berries, not blueberries.")
    berry_number = input("How many berries would you like to eat?")
    if berry_number > 10:
        print("Great! You're not starving and you continue your path through the forest unharmed.")
    else:
        print("Oops! Too many... berries... You start to... feel... dizzy.")
        dead = True
else:
    # Neutral Choice
    print("You don't find anything, but now might be a good time to rest.")
    sleep (delay)

if dead == True:
    print("Oh no, you died. Try again by hitting the green play button.")
    quit()
#########################################################################################################
# TEAM 9
print("")
print("")
print("You wake up on the top of a very tall mountain"
)
print("A storm is approaching and you have to get down as soon as possible")
print("In front of you there is a motorcycle and jeep")
sleep(delay)
print("You quickly have to make the decison if you would rather walk and slowly but safely get to safety,"
      "take the motorcycle that would be quicker but more dangerous or take the jeep that will travel slowly over the "
      "terrain but can probably withstand the storm")
print("")
print("")
transportation = input("What form of transportation would you prefer? [walk/motorcyle/car]")
if transportation == "walk":
    print("You start your walk and everything seems okay, but you can see the storm catching up rapidly")
    print("After a few minutes the rain catches up to you but you don't start to worry because you may be able to "
          "find shelter before the lightning commences")
    sleep(delay)
    print("Lightening starts and you are dead")
    dead = True
    print("After the storm is over you're still stuck and you have to wait for help")
elif transportation == "motorcycle":
    print("As the storm approaches rapidly, you quickly hop on the fastest vehicle")
    print("You have a couple close calls but you outpace the storm and make it to safety")
else:
    print("You're traveling down the mountain")
    print("It's been hours but you don't seem to be getting anywhere")
    print("You decide you are lost")
    print("You need to find help quick!")
    print("")
    sleep(delay)
if dead == True:
    sleep(delay)
    print("Unfortunately the storms rough conditions were too much for you")
    quit()
#########################################################################################################
# TEAM 10
print()
print("welcome", username, "to the forest leading to Grandmothers house.")
sleep(delay)
print("You are walking to grandmas house, in front of you lies three paths")
print("There are three paths infront of you. One leads you safely, one takes you through a shortcut, one is a new path that youve never explored before")
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

if dead == True:
    print("The wolf ate you, Better luck next time. Click the green button to try again")
    quit()
#########################################################################################################
# TEAM 11
dead = False
direction = input( "Would you like to continue Forward into the cave, or better Back?")
if direction == "Forward":
    print('')
    sleep(delay *3)
    print("Oh No!")
    sleep(delay * 4)
    print('')
    print("While you were walking forward into the cave, you fell to an endless hole")
    sleep(delay *3)
    print("You keep falling and falling...!!!")
    sleep(delay *3)
    print("Years went by, until you died. \n")
    dead = True
elif direction == "Back":
    sleep(delay * 4)
    print("You start walking on the direction that you followed to come in the cave")
    sleep(delay * 3)
    print("Suddenly you see a door on your left side")
    door_decision = input("Would you like to open the door?Yes or No?")
    if door_decision == "Yes":
        sleep(delay * 4)
        print("You found the treasuuree!!!")
        sleep(delay * 2)
        print("Suddenly you see there is another room!")
        sleep(delay * 2)
        print("You go into the room and you find yourself into a beautiful garden.")
    else:
        sleep(delay * 4)
        print("You keep walking to the direction that you came from, and you end up outside.")
else:
    sleep(delay * 2)
    print("Please answer the question with either Forward or Back in order to continue the story. Thank you!")
    direction = input()
    if direction == "Forward":
        print('')
        sleep(delay * 3)
        print("Oh No!")
        sleep(delay * 4)
        print('')
        print("While you were walking forward into the cave, you fell to an endless hole")
        sleep(delay * 3)
        print("You keep falling and falling...!!!")
        sleep(delay * 3)
        print("Years went by, until you died. \n")
        dead = True
    elif direction == "Back":
        sleep(delay * 4)
        print("You start walking on the direction that you followed to come in the cave")
        sleep(delay * 3)
        print("Suddenly you see a door on your left side")
        door_decision = input("Would you like to open the door?Yes or No?")
        if door_decision == "Yes":
            sleep(delay * 4)
            print("You found the treasuuree!!!")
            sleep(delay * 2)
            print("Suddenly you see there is another room!")
            sleep(delay * 2)
            print("You go into the room and you find yourself into a beautiful garden.")
        else:
            sleep(delay * 4)
            print("You keep walking to the direction that you came from, and you end up outside.")

if dead == True:
    quit()
#########################################################################################################
# TEAM 12
print("OH NO! There's a sudden horrible screeching sound from up above!")
sleep(delay)
print("It's a massive CAVE BAT!!!")
sleep(delay)
print("And it's heading straight for you!!!")
sleep(delay)
choice = input("What will you do? [Run/Duck/Snatch]")

if choice == "Snatch": # the good choice
    print("SICK! You snatched that bat! It is now your sidekick.")
    sleep(delay)

if choice == "Run": # the bad choice
    print("that is a wrong choice, you were about to die. You will get one more chance to survive.")
    sleep(delay)
    Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    Second_choice= input("pick a number between 1 and 10")

    if Second_choice > "5":
        print(" right choice, you survived for now ")
    else:

         print("The bat caught you with it's weird long talons and scratched your eyes out. You died from your injuries.")
    sleep(delay * 2)
    dead = True

else:
# the neutral
    print("Hmm...you survived the beast. Carry on...")
    sleep(delay)

if dead == True:
    print("Bruh.")
    sleep(delay)
    print("Hit the green run button to try again.")
    quit()

#########################################################################################################
# TEAM 13
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

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()
#########################################################################################################
# TEAM 14
dead = False
print("")
print("You wake up to several sounds...")
print("One coming from behind, one from something running to your right, and the other from a blazing fire to your left.")
print("")
sound = input("Which sound do you choose to follow? [Behind/Left/Right] ")

if sound == "Behind" or sound == "behind":
    # Neutral Choice
    print("You're running away from your fears...this will not get you far in life.")
    print("")
    sleep(delay)
elif sound == "Left" or sound == "left":
    # Bad Choice...
    print("")
    print("You arrive at a Devil Convention.")
    sleep(delay*2.5)
    print("")
    print("Part of the celebration is to roast you...")
    print("")
    sleep(delay*2.5)
    print("First by roasting you with offensive jokes about your life, then literally roasting you.")
    sleep(delay*3)
    print("")
    print("In order to survive, you have one option...")
    sleep(delay*3.5)
    print("")
    print("")
    print("Join their cult.")
    print("")
    print("")
    sleep(delay*2.5)
    choice = input("Would you like to accept the invitation to join th cult? [yes/no] ")
    if choice == "yes" or choice == "Yes":
        print("")
        print("Congratulations, you have a new family.")
        print("You're officially a devil.")
        print("")
        sleep(delay)
    else:
        print("")
        print("Congratulations, you died.")
        dead = True
else:
    # Great choice
    print("You see your deceased Grandma running...")
    sleep(delay*3.5)
    print("You then embrace each other and talk about the days when you sucked your thumb.")
    print("")
    print("You are so happy.")
    sleep(delay*3)
    print("")
    sleep(delay)

#########################################################################################################
# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
