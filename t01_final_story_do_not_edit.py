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
dice_roll = input("You're scared. What would do you do?  [Run /Say Hello /Go Towards To Sound/ Look Around]")

if dice_roll == "Run":
    print("Goodbye",username,"The voice gets angry, screams, and you die!")
    # Do something, probably die. The bad thing happens
elif dice_roll == "Say Hello":
    print("Hello your bravery is commendable traveler.")
else:
    # This is the neutral thing that occurs.
    print("Nothing happened")

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 2

from time import sleep
delay = 2.0
(input("What is your name?"))
sleep(delay)
print("You find yourself in a tavern, surrounded by drunkards and bounty posters")
sleep(delay)
print("Decide what to do in the tavern: go to the bounty board, get a drink, or leave")
sleep(delay)
choice = (input("Chocolate milk, Bounty board, Leave"))
if choice == " Chocolate milk":
    print("Good choice! You have some great chocolate milk and your day continues as usual.")
elif choice == " Bounty board":
    print("You walk to the bounty board and one piece of paper catches your eye; the largest bounty in the nation.")
    sleep(delay)
    print("As you keep reading it, someone walks into the tavern.")
    sleep(delay)
    print("You turn around and see a giant man hovering over you; the same one on the poster.")
    sleep(delay)
    print("This is bad. He pulls out a knife and slowly approaches you.")
    fight = input("Pick a number 1 through 10: if you choose one of the right numbers, you will live.")
    if fight <="5":
        print("You try to counter his massive knife with your bare hands.. why? He promptly ends you.")
    elif fight>"5":
        print("You break left and scramble through the tavern door; you make it out, and have a relatively normal day.")
else:
    print("You leave. your day is alright, and you live.")

#
# # TODO Make sure to add the additional check if the user makes the "bad" choice!
#
# # TODO Don't forget to check if your user is dead at the end of your chapter!
#
##
#########################################################################################################
# TEAM 3
# TODO Add your part of the story here.
char= input("Choose the form that you wish to complete this quest. \n [Monster, Human or Goblin]")
if char == "Monster": #good choice
    print("You are a monster.\n")
    print("You use your sharp claws and venomous fangs to raid a village")
    sleep(delay*2)
    print("\n")
    print("You have obtained 3 Silver and 2 Gold")

elif char=="Goblin": #bad choice
    print("You are a Goblin")







# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


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
food = input ("choose what you want to eat today? [pasta/pizza/burger]")
if food == "pasta":
    #good choice
    print("you were lucky this time!")
    print("now you get free pasta and get to live")
elif food == "pizza":
    #bad choice
    print("this is poisoned!")
    print("you will experience death in 30 seconds!")
    print("you didn't make it")
    dead = True
elif food == "burger":
    #neutral choice
    print("Yikes! You will experience food poisoning")
    print("But don't worry, you will still live")
if dead == True:
    print("Oh no! You failed to pass this stage. Now you died!")
    quit()






# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 6
def team_6_adv():
    pass
    enrollment = input("Should you take CSC 226? [Yes/No/Not sure]")
    if enrollment == "Yes":
        print("That's a good choice!")
    elif enrollment == "No":
        print("Oh no! You cant graduate!")
        print("You have no job! GOOD JOB!")
    else:
        print("Let me show you what you can with a CS Degree!")
        quit()
def main():
    team_6_adv()

main()




# No == print ("Goodluck with your future endeavours")
#     print("Goodluck with your future endeavours")



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
print("you come across a lit section of the cave. You see 4 adventurers sitting around a fire. They notice you and motion for you to sit with them.")
destination = input("Where are you headed young traveler?")
sleep(delay)
print("I dont know where", destination, "is but one of my other party members might. Try asking one of them.")
sleep(delay)
person = input("Who will you ask? [Dwarven soldier/Beggar/Pirate]")
if person == 'Dwarven soldier'
print("I dont know the way their by memory alone but i do have a map. Let me give it to you. We're headed towards town anyways to get a new one.")
sleep(delay)
print("You have successfully escaped the cave and made it to", destination,"YIPEEE")
elif person == 'Beggar'
print("the Beggar doesnt seem to speak your language so you dont understand eachother.")
sleep(delay)
else person == 'Pirate'
print("Sure ill tell ya, once you win in a game of chance,Russian Roulette.")
sleep(delay)
print("\n")
print("You pull the trigger aaaaaaand... your dead, did ya expect the pirate to play fair?")
# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 17
Direction = input("There are three boxes in front of you: left, middle, and right. Which one would you like to pick?")

if Direction == "left":
    # Ooooooh... unfortunate.
    print ("Man, that sucks. ")
    sleep(delay)
    print ("You picked... the bomb!!")
    print ("BOOOOOOMMMM!!!")
    sleep(3)
    dead = True

elif Direction == "middle":
    # neutral
    print ("You get...")
    sleep(delay)
    print ("A pen with unlimited ink")
    sleep(delay)
    print ("Fun right...?")

else:
    # Noice
    print ("*drumroll*")
    sleep(delay)
    print ("YOU WIN THE GRAND PRIZE!!")
    print ("You get...")
    sleep(delay)
    print ("Two pens with unlimited ink: A black and red pen!")

if dead == True:
    print ("welcome to the afterlife my child. You have chosen wrong.")
    quit()




# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 18
way = input("Which path do you want to go? [Left, Right, Forward]")

if way == "Left":
    #Bad choice
    print("\n")
    print("You walked on the left path. This was the wrong way and you are stuck inside.")
    sleep(delay)
    print("You have no food and slowly starve.")
    dead = True
elif way == "Right":
    #Neutral choice
    print("\n")
    print("You continue walking on the right path and nothing happens.")
    sleep(delay)
    print("At least you are still alive!")
    print("\n")
else:
    #Good choice
    print("\n")
    print("You chose the path forward and found $1,000,000")
    sleep(delay)
    print("You can do anything you ever wanted with all the money.")
    print("\n")
    rich = True
sleep(delay)

print("You walk out into an opening and see a man sitting down.")
sleep(delay)
print("He has a lot of things next to him including bread and a knife.")
sleep(delay)
print("Buy the knife, steal the bread, or continue?")
way = input("What are you gonna do? [Buy, Steal, Continue]")

if way == "Buy":
    #Good choice if you are rich
    if rich:
        print("\n")
        print("You bought all the bread you're not hungry anymore.")
        sleep(delay)
        print("\n")
    else:
        print("\n")
        print("You don't have enough money to buy all this bread.")
        print("\n")
        sleep(delay)
        print("The guy thinks you're trying to steal it and kills you.")
        dead = True
elif way == "Steal":
    #Bad choice
    print("\n")
    print("You tried to snatch the bread.")
    sleep(delay)
    print("Before you could run, the guy shoots you in the back of the head.")
    sleep(delay)
    print("So... no bread! And you died!")
    dead = True
else:
    #Neutral choice
    print("\n")
    print("You just ignore him and continue walking.")
    print("\n")
    sleep(delay)


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 19
paths = input("Choose a path: [Left/Right/Center] ")

if paths == "Left":
    # neutral path
      print("You continue walking and are startled by a colony of flying foxes flying away. ")
      sleep(delay)

elif paths == "Center":
    # You'll regret that
    print ("A weird flapping sound occurs when walking. ")
    sleep(delay)
    print (" Sound like it's coming from a small animal. ")
    print (" You realize you've walked into the sleeping grounds of a vampire bat colony, and they're very hungry.")
    print ("The bats descend on you and suck your blood dry, killing you in a matter of hours. ")
    dead = True

else:
    #You'll be okay
    print ("You walk in a room with a giant treasure chest.")
    print ("The chest contains lost of gold and valuable jewels. ")
    print ("The chest also opens a path to the end of the cave")

if dead == True:
        print(" What a horrible way to die. Please try again by pressing play.")
        quit()



# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 20
your_name = input("what is your name: ")
print()
print("welcome,", your_name, " to the labyrinth")
make_choice = input("You are required to choose a path: North, South, West, East: ")
if make_choice == "North":  #Good Choice
    print("you are still in the dark, but someone is there to guide you")

elif make_choice == "South": #Bad Choice
    print("You made the wrong choice")
    print("your are in the dark, your have lost your way")
    print("")

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 21
direction = input("Which way would you like to go? [Left/Right/Straight Forward] ")
if direction == "Left":
# Uh oh! Bad choice!
print("Since it was dark you unaware of the cliff and fell off and plummeted to your death.")
dead = True
elif direction == "Right":
# Ooo Yes! Good choice.
print("As you walk through the cave you a light source.")
print("Congrats! You made it out the cave and into the forest.")
# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 22
partner = input("You see three figures appear before you. A wizard, a fairy, and a vampire.\nWho do you choose to help you out of this sticky situation? (Wizard/Fairy/Vampire)")
if partner == "Wizard":
    # Good choice
    print("The wizard looks at you with a serious expression on his face.")
    sleep(delay)
    print("He decides you are worthy.")
    print("He pulls out his staff and lights the way to the exit of the cave.")
    sleep(delay)
    print ("Upon leaving, he wishes you luck on your journey and gifts many magical items!")
    sleep(delay)
elif partner == "Fairy":
    # Neutral choice
    print("The fairy tells you to follow it and not to be slow.")
    print("She precedes to fly off very quickly and you have to run to keep up!")
    sleep(delay)
    print("After hearing the fairy chuckle, you realize the fairy is just leading you in circles repeatedly.")
    print("Such scoundrels they can be!")
else:
    # Bad choice, if they choose vampire or an option not given
    print("The vampire tells you that you made an interesting choice, so you can follow him in a very concerning tone.")
    sleep(delay)
    print("After someone how arriving at an even darker part of the cave, you feel a breeze and suddenly the vampire is behind you")
    sleep(delay * 2)
    number = input("Choose a number between 1 and 13, young mortal, to decide your fate. Choose correctly and I'll let you go, I think you know what happens if you choose incorrectly.")
    number_int = int(number)
    if number_int == 13:
        print("Well, well, well. You have chosen correctly, and I am a man of my word. Leave.")
    else:
        print("Not quite. The vampires favorite number is unlucky 13!")
        sleep(delay * 2)
        print("Maybe in another life.")
        print("As for this one though, the vampire handles that.")
        print("You feel his teeth sink into your neck.")
        sleep(delay * 2)
        print('As you feel your life force draining,')
        print('all you hear is the sound of the wizard and fairy asking each other, "Why on Earth did he choose to go with the vampire?"')
        sleep(delay * 2)
        dead = True


if dead == True:
    print("You have died")
    print("Maybe you should try again and choose a not so deadly option. Click the green play button to start over.")
    quit()



# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 23
print("You walk into the castle and you are starving for a yummy snack")
direction = input("You see an amazing dinner on the table what will you do? [Eat it/Leave it/Take a nibble] ")
if direction == "Eat it":
    #Bad choice
    print("You have been poisoned")
    sleep(delay)
    print("oops you have died")
elif direction == "Leave it":
    #Good choice
    print("You see handsome Prince Chef! Wow!")
    sleep(delay)
    print("You got a gourment dining course! Yummy!")
else direction == "Take a nibble":
    #Neutral choice
    print("You are half-full and you are ready to go home")
    sleep(delay)
    print("You are ready to go home")


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!



#########################################################################################################
# TEAM 24
choice = input("Which door will you enter?[red_door/green_door/blue_door]")
if choice == "red_door":
    print("you find a path, walk down it and continue your adventure")
    sleep(delay * 2)
elif choice == "green_door":
    print("you find a sack of gold and your way out")
else:
    print("when you first go through it seems clear")
    sleep(delay)
    print("you turn the corner")
    sleep(delay)
    print("freddy kruger is waiting for you")
    sleep(delay * 2)
    print("you try to run but there is no escape. he catches up to you quickly")
    sleep(delay * 2)
    print("giving you an untimely death")
    dead = True

if dead == True:
    print("this game was easy and you still died. Better luck next time")
    quit()

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!



#########################################################################################################
# TEAM 25
username = input("What is your nickname? ")
print("Hello,", username, ", welcome to our game!")
print("You have three choices: one good, another bad, and neutral.")
print("Good one leads to cute kittens, bad one leads to hungry lions, neutral leads to flowers.")
print("Good luck with your adventure!")
print("\n")
d = input("Which path would you like to go first, second, or the third? ")
if d == "first":
    print("Great choice! It seems you made a right choice, continue your way ;)")
elif d == "second":
    print("You chose neutral way, continue your path, but be extremely careful!!!")
    d1 = int(input('Now you are again seeing three trails, choose only one of them: 1, 2, 3  '))
    if d1 == 1:
        print('Good! You are in the field with flowers and kittens around you!')
    elif d1 == 2:
        print('Too bad! Here is a huge dangerous lion!! RUN!!!')
        print('I am so sorry, the lion was faster than you. You are dead :(')
        dead = True
    else:
       print('You are in the sky with the beautiful lions, which are not eating people, you re lucky! No kittens though')

else:
    print("Oops, I hear the roar! YOu are shaking, feeling desperate.")
    print("The lion is eating you with delight.")
    dead = True
if dead == True:
    print("Oh, no! You have just died in front of a lion!")
    quit()
# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 26
door = input("Choose one of the three doors. Blue, Red or Green?")

if door == "Green":
    #right choice
    print("You are on the right track. As you are walking you see a light ahead!")

elif door == "Red":
    #bad choice
    print("Oops... Wrong door")
    sleep(delay)
    print("As you are walking forward, the door behind you closes.")
    print("Gas starts to fill up the room and you have a hard time breathing")
    dead = True

else:
    #neutral choice
    print("The place you entered has a torch at the end of the room. Nothing interesting!")
    sleep(delay)


if dead == True:
    print("Oh no! You died. Try again.")
    quit()




# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 27
print("You've arrived at your final destination")
print("You have 4 options!")


level = input("Which level do you want to choose? (answer 1/2/3/4) ")


if level == "1":
   #Bad choice
   print("Oh no! There's a zombie. You almost died")
   print("We will give you one more chance!")
   floor = input("Which floor do you choose this time? (1-10) ")
   #1-5: good choice
   #6-8: bad choice
   #9-10: neutral
   floor = int(floor)

   if 1 <= floor and floor <=5:
       print("good choice")
   elif 6<= floor and floor <=8:
       print ("bad choice")
       dead = True
   else:
       print("neutral")



elif level == "2":
   #Good Choice
   print("Yay, There is a party with lots of food. Enjoy!")


else:
   print("There's a zombie but Look! There's also a door out there. Run fast!!")


if dead == True:
   print("You're dead!")
   quit()


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 28
direction = input("Which direction would you like to go now? [North/South/East/West]")
if direction.lower() == "east":
    print("You travel East")
    print("You find a lamp that is somehow still lit")
    print("You can now see the cave around you, you're still lost but at least you can see")
    print("You use this lamp to navigate out of the labyrinth.")
    print("You exit the labyrinth")
elif direction.lower() == "west":
    print("You travel West")
    print("You wander around in the dark when suddenly your foot slips")
    print("You fall...")
    for x in range(0, 3):
        print("and fall...")
        sleep(delay)
    dead = True
else:
    print("You go" + direction + " you go until you reach a wall and turn left")
    print("You make another left")
    print("and another left")
    print("You're not sure but you think you're right back where you started, just as lost before")

# TODO Make sure to add the additional check if the user makes the "bad" choice!
if dead == True:
    print("You died of starvation while falling. Better luck next time! Try again by hitting the green play button.")
    quit()
# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# TEAM 29
print("You wake up under the sand dunes in a cave.")
print("You can't see anything more than a meter in front of you.")
print("After walking for the better part of an hour you come to a fork in the path.")
print("Three paths lay before you")
path = input("Do you go Left/Right/Middle?\n")
if path == "Right":
    print("You trip over something on the ground.")
    print("You pick it up and discover it's a lantern")
    print("You continue on with light.")
elif path == "Left":
    print("The cave buckles as you're trapped under. You get crushed to death")
    dead = True
else:
    print("You journey on in the dark")

if dead == True: print("You have died, please try again")
quit()


# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!



#########################################################################################################
# TEAM 30


name = input("What is your name? ")
print(f'Welcome {name}  to the game: Choose you own Adventure')
print("You are stranded in a desert")
print("You find three roads")
print("You are thirsty and one of them leads to water")
print("The other two are dangerous")


road = input("Select the road, 1,2, or 3?")
if road == "1":
    print(f"Oh no, {name} fell in a pit of snakes! You died")
    quit()

elif road == "2":
    print(f"Congratulations {name}, you found water.")

else:
    print(f"{name} came across a den of lions. Good luck next time!")








# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!

