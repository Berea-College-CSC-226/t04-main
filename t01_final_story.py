######################################################################
# Author: Fall 2024 Class
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
#   NOTE: T01 wasn't completed by your class. You are modifying a previous classes' T01!
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
question = ""
if direction == "North":
    print("It's a wizard!")
    question = input("""What do you ask the wizard(1,2,3)?
    1)What are you doing here? 
    2)Can you help me?
    3)Turn me into a frog\n: """)
    sleep(delay)
if question == "1":
    print("""This is my Wizard Cave! I practice my spells! Do you wish to observe one of them? 
    Of course you do! The wonder of magic is for everyone! ANURA METAMORPHOS!!! *poof* """)
    frog = True
elif question == "2":
    print("""I can transform you into a frearsome creature! A malevolent devourer, 
    feared by insects both land and air. ANURA METAMORPHOS!!! *poof*""")
    frog = True
elif question == "3":
    print("""I have spent endless hours practicing just for this! In my wizard cave! 
    ANURA METAMORPHOS!!! *poof*""")
    frog = True

if frog == True:
    sleep(delay)
    print("You are a frog now. You're not dead, but you can't do anything either. RIBBIT!!!")
    print("""You have reached the "secret" frog ending. Congradulations!""")



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
delay = 1.0
direction = input("Which direction would you like to go? [North/South/East/West]")

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    print("The preson gets closer to you. You get scared of them and, and if they may harm you")
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
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TEAM 12
direction = input("[Tavern/Inn/Reform/Run]")

if direction == "Inn":
    # Good choice!
    print("You wander into an Inn, where a gambling man at a corner table offers you "
          "a gold nugget in exchange for playing a game of Russian Roulette.")
    sleep(delay)
    print("Upon closer inspection you realize the revolver's chambers are all full. "
          "Regardless, you choose to entertain the idea.")
    print()
if direction == "Tavern":
    # Good choice!
    print("Although you referred to the building as a tavern initially, closer inspection reveals to you"
          "that this particular subset of business is referred to as a 'saloon' in a western context.")
    sleep(delay)
    print()
if direction == "Saloon":
    # Good choice!
    print("In your infinite wisdom you have chastised the narrator for their improper use of the term 'tavern'."
          "He notes this and allows you to carry on.")
    sleep(delay)
elif direction == "Run":
    # Oh... Bad choice
    print("Your reputation proceeds you. Such is the shame of your cowardice that "
          "you immediately suffer psychological strain.")
    sleep(delay)
    print("Like that television scene from the next century's hit movie 'Scanners' your "
          "brain expands and presses against the wall of your skull.")
    sleep(delay * 2)
    print("Your death is instantaneous and cheesy as all get-out, yet you can't help but "
          "wonder what impact your inexplicable headsplosion will have on creative writing "
          "going into the future.")
    dead = True
elif direction == "Reform":
    # Oh... Bad choice
    print("The powers of camaraderie, friendship and all adjacent terms for socially "
          "agreeable behaviour come together to stop your tyranny before it begins.")
    sleep(delay * 2)
    print("Unfortunately, this also means you lose control of the player character.")
    sleep(delay * 2)
    print("They die of natural causes, lead poisoning, shortly after attempting "
          "to intervene in a bank robbery sometime in the year 1890.")
    dead = True
else:
    # Neutral choice
    sleep(delay)
if dead == True:
    sleep(delay*2)
    print("You are dead. This was probably fully deserved.")
    print("Hopefully the metaphysical emissary intervenes on your behalf in the Yama's courtroom.")
    print("Oh wait, nevermind, you've already been pardoned. Please restart.")
    quit()
#########################################################################################################
# TEAM 13
user_direction = input("You come at across three tunnels.... (Choose forward, left, or right): ")
sleep(delay)

if user_direction == "left" or user_direction == "Left":
        print("You hit a den in which a bear lives in...")
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
            print("Congrats you didn't die.")
        elif number_picked > 14:
            sleep(delay)
            print("You picked wrong...")
            dead = True

elif user_direction == "right" or user_direction == "Right":
        sleep(delay)
        print("You find an exit and reach a hill that overlooks a waterfall")
        print("Everything seems peaceful.")
else:
        print("You walk forward...")
        sleep(delay)
        print("Nothing happens...")

if dead == True:
        print("You died... Sorry")
        quit()
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
if direction == "North":
    #Bad choice! Sacrifice room!
    print("The north room is dimly lit by lanterns with red fire.")
    print("Five people in black robes are gathered around an altar.")
    print("Their argument quiets as you walk in.")
    sleep(delay)
    print("'Oh, how perfect,' one says. 'You have been Forgiven, Yuxila.'")
    print("Stone rises from the floor to block your exit.")
    sleep(delay)
    print("You are captured by the cultists. You are dead.")
    dead = True
elif direction == "South":
    #Bad choice! Ritual room!
    print("You see a glowing circle on the floor. Robed figures stand around it and chant.")
    print("You do not recognize their words.")
    sleep(delay)
    print("A pressure builds in the room. It is too much.")
    print("Your heart bursts open inside your chest.")
    print("You are dead.")
    dead = True
elif direction == "East":
    #Good choice! Dorms!
    print("The room you emerge into has a low stone ceiling. Bunked beds line the walls for fifty meters.")
    print("You walk carefully down the length of the room. Your breath is the loudest sound you hear.")
    sleep(delay * 2)
    print("At the end of the room is a kitchen and a door. There is no window.")
    print("You steel yourself and open the door as quietly as you can.")
    sleep(delay)
    print("The door leads outside. You are free.")
elif direction == "West":
    #Neutral choice. Armory.
    print("This room is lined with weapons. Most are ornate daggers, hundreds of them hang on hooks lining the walls.")
    print("You see glowing runes on many of the daggers. Several do not have runes.")
    dagger = input("Do you take a dagger? [Yes/No]")
    if dagger == "Yes":
        print("You observe several daggers without runes. You take the one that looks unassuming.")
        print("The sound of a bell rings through the caves. You tense.")
        sleep(delay)
        print("Robed figures flood the room. You attempt to fend them off, but you are overwhelmed.")
        print("You are dead.")
        dead = True
    elif:
        print("This room looks suspicious. You return quietly to previous room.")

if dead == True:
    print("You have been sacrificed to the Great Devourer.")
    quit()

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
if direction == "North":
    print("The man steps out of the shadows and offers a handshake. 'Hi! I'm Fred!'")
    handshake = input("Shake the man's hand? (Yes/No)")
    if handshake == "Yes":
        print("""The man smiles. 'I came here to be alone, but I met someone friendly! Here, I'll show you how to leave the cave.'""")
    if handshake == "No":
        print ("The man punches your head off.")
        dead = True
if direction == "East":
    print("Now you can see two ways. One of them is filled with bones and another without any light. ")
    print("You are sitting in this room for hour and a half and your body temperature slowly drops.")
    choice = input("You need to make a choice. Will you tread the bones or follow the darkness? (Bones/Darkness) ")
    if choice == "Bones":
        print("You are slowly going towards the light. You can almost see the exit, but somehow you stepped on the slippery rock and bashed your brain out on the concrete.")
        dead = True
    if choice == "Darkness":
        print("You fall into a pit and land in a tree outside the cave.")


if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button.")
    quit()



#########################################################################################################
# TEAM 19

bridge = input("You come across three bridges do you want to take the [Left/Middle/Right] path?")

if bridge == "Left":
    print ("You walk across a stone pathway confronted with a beautiful waterfall at the end: [+5 inspiration]")
    sleep(delay)

#if they go left: You come across a beautiful waterfall: [+5 inspiration]

elif bridge == "Middle":
    print ("You walk across a chasm and the wooden bridge breaks and you are about to fall: [THINK FAST]")
    sleep(delay)

    rope = float(input("Quick! Catch yourself using a rope! Determine its length in feet by picking a number between [1] to [20]"))

    if rope > 13:
        print("Phew! You managed to grab the rope just in time before the fall! Congratulations: [+5 Survival Skills]")
    else:
        print("Oh no! Your hand slips and you fal backwards into the chasm: [DEAD]")
        dead = True


#elif they go middle: You walk across a chasm and the wooden bridge breaks and you fall: [DEAD]

else:
    print ("You walk safely across a plain bridge: [0 inspiration]")
    sleep(delay)
#else they go right: You walk safely across a plain bridge: [0 inspiration]

if dead == True:
    print("Oh no! You did not make it to the end: [GAME OVER]")
    quit()



#########################################################################################################
# TEAM 20

elif direction == "East":
    print("You run until you see a bright light ahead of you, there are two paths both heading towards what appears to"
          "be freedom, which do you choose?")
    sleep(delay)
    direction = input("Left/Right")

if direction == "Left":
    print("You run left towards the bright light it looks like freedom you sprint in joy exited for your freedom.")
    sleep(delay)
    print(
        "As soon as you hit the exit you run straight off a cliff and fall into an ocean where a hungry pack of ducks")
    print("has been waiting for their meal.")
    dead = True
if dead == True:
    print("You died a very funny and unfortunate death")
    quit()

elif direction == "Right":
    print("You find the magical city of gold, no wonder the reflection was so bright, you are blessed with riches and")
    print("your own castle for the rest of your life.")
    sleep(delay)

# ------------------------------------------------------------------------------------------------------------

if direction == "West":
    print("You hear chanting coming from the west side of the cave, you can't help but wander that way hoping to find")
    print("some help. You see 12 men in fancy robes dancing around a fire in the middle of the cave floor, it looks")
    print("like a sacrifice, what will you do?")
    sleep(delay * 2)

    direction = input("Approach them Yes/No")

    if direction == "Yes":
        print("You approach them interested in their ritual and they welcome you with open arms giving you a robe and")
        print("and a pair of shoes, you join them in their corny dance and have become a member of the Illuminati")
        sleep(delay)

    if direction == "No":
        print("You try to sneak away hoping to avoid their weird games but they catch you and toss you in the fire!")
        dead = True
    if dead == True:
        print("You burn and die in their fire, becoming another part of their sick ritual.")
        quit()

#########################################################################################################
# TEAM 21

    print()
    print("Welcome", username, "! Now it's time to answer some math questions!")
    sleep(delay)
    print("In order to proceed you must get all three of the following questions correct.")
    print("You are now in a math class by yourself so focus and be engaged.")
    print()
    sleep(delay * 2)
    print("What is the square root of positive four? √(4)")
    print("\n")
    sleep(delay)

    answer = input(
        "Which answer would you like to choose? Respond with the corresponding capital letter. [A. -2/ B. 2/ C. 8]")

    if answer == "B":
        print("Great! You got this one correct. You have been teleported to Mount Olympus!")
        sleep(delay)
    elif answer == "A" or answer == "C":
        print("Almost! The gods are being lenient and have given you a second chance! Try Again.")
        answer = input("Input another letter answer.")

        if answer == "B":
            print("Great! You got this one correct. You have been teleported to Mount Olympus!")
        else:
            print(
                "The Math gods looked at you and gave you a cold stare. How could you enter an incorrect option even after two chances.")
            sleep(delay)
            print(
                "You felt a cold shiver down your spine and looked up to see a very enraged Math god named Algebrais.")
            dead = True

    else:
        print(
            "The Math gods looked at you and gave you a cold stare. How could you enter an option that doesn't exist?")
        sleep(delay)
        print("You felt a cold shiver down your spine and looked up to see a very enraged Math god named Algebrais.")
        dead = True

    if dead == True:
        print(
            "Uh Oh! The Math gods are very upset that you dont know the answer to this basic math question. You were struck by lightning ad banished to never do math again! Better luck next time.")



#########################################################################################################
# TEAM 22
talk = input("Do you wish to talk to them? [Yes/No]")

if talk == "Yes":
    print("It seems they're just as lost as you are!")
    sleep(delay)
    print("You agree to help each other find your way out of this cave, and they have tools to help")
else:
    print("Due to your silence and shadowy figure in the dark, they mistake you for a beast!")
    chance = input("How many steps do you take towards the person? Enter an integer")
    if chance > 7:
        print("They are startled by your rapid approach!")
        print("They charge at you head on and you trip and fall.")
        sleep(delay * 2)
        print("You keep falling?")
        sleep(delay)
        print("It seems you fell over a cliff, you're still falling and you don't know when you'll hit the gro-")
        dead = True
    else:
        print("They get closer to you and see you're a human too!")
        print("They agree to help you using tools from their backpack")

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

tool = input("Which tool do you think will help? [Torch/Shovel/Compass]")

if tool == "Torch":
    print("You light the torch, and now you can see!")
    sleep(delay)
    print("It appears the cave leads into a well, and when you get closer you see light at the surface!")
elif tool == "Shovel":
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
    dead = True
else:
    print("You pull out the compass, maybe if you follow one direction it'll lead somewhere eventually!")
    sleep(delay)
    print("...")
    sleep(delay)
    print("......")
    sleep(delay * 2)
    print("You can't see the compass, it's way too dark, maybe something else will help")
    tool = input("What do you want to try now? [Torch/Shovel]")
    if tool == "Torch":
        print("You light the torch, and now you can see!")
        sleep(delay)
        print("It appears the cave leads into a well, and when you get closer you see light at the surface!")
    elif tool == "Shovel":
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
        dead = True

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()


#########################################################################################################
# TEAM 23

direction = input("Which part of Country in Africa would you like to visit? [Uganda/Congo/Ghana/Zimbabwe/Nigeria]")

if direction == "Uganda":
    # This is a horrible choice
    print("Yoweri Museveni, President of Uganda unfortunately does not like outsiders in his country.")
    print("You can choose to visit another country.")
    dead = True

elif direction == "Congo":
    print("Currently in congo there is a war.")
    print("In eastern DR Congo, a crisis of rare violence has been going on for more than two decades.")
    print("The DRC is currently facing one of the world's worst humanitarian and food insecurity disasters, and has become the second largest internally displaced people's crisis globally.")
    dead = True


else:
    print("Africa is a beautiful continet")
    print("you can go anywhere you wanna go, across the globe, and over sea's!")

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!

if dead == True:
    print("Your'e dead congo is currently going through a crisis")
    quit()

#########################################################################################################
# TEAM 24

print(
    ''' Before you can approach the shrouded individual, the cave's eerie silence is broken by shouting. "By my name, I am Dave the magical CHEESE WIZARD!!! What is thy business here!?"''')
sleep(delay)

purpose = input("What is your purpose here? [Justice/fame and fortune/escape]")

if purpose == "Justice":
    print('''"Then go"''', username,
          '''" and take some cheese for the journey." Dave the cheese wizard vanishes and you are left alone once more. Thanks Dave, very cool."''')

elif purpose == "fame and fortune":
    print(
        '''"You are unworthy!" You are bludgeoned to death by an angry wizard with a comically large wheel of cheese. sorry"''',
        username, "luck does not appear to be on your side.")
dead = True

else purpose == "escape":
print(
    "your attempt to run is met with hostility. A block of cheese is summoned beneath you and you trip breaking your neck. Sorry",
    username, "Dave is more powerful than you know.")
dead = True
# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
if dead == True:
    print("Oh no! You died. It's a skill issue! Try again by hitting the green play button. ")
    quit()