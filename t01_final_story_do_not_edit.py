######################################################################
# Author: Spring 2026 Class
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
######################################################################
from time import sleep

#########################################################################################################
# TEAM 1
print("Luckily, you have a flashlight; should you use it?")
choice_2 = input("Yes/No? ")

if choice_2 == "Yes":
    # Good choice
    print("You discover a friendly  person that offers you some food.")
elif choice_2 == "No":
    # Bad choice
    print("You hear footsteps..")
    sleep(delay)
    print("They notice you and start screaming. In a panic you fall and hit your head on a rock")
    dead = True
else:
    print("The cave is swarming with bats!")
    print("You start running..")
    sleep(delay)
    print("Suddenly, you see some light, you run toward the light")
    sleep(delay)
    print("After running forever, you make it out of the cave")
    sleep(delay)

if dead == True:
    print("Unfortunately, you met your bitter end because you panicked.")
    quit()
# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 2
from time import sleep

delay = 1.0
dead = False
username = input("What do they call you, unworthy adversary? ")
print()
print("Welcome,", username, ", to the choices of life.")
sleep(delay)
print("Before you lie two paths. One path leads to an afterlife, (paradise)".)
print("The other, certain death(HELL). Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing and the cold is treacherous.")
print("Staying here is certainly not wise and the enemy might come for you. You must find your way out.")
print("\n")
sleep(delay)
choices= input("what choices can you make to save yourself from damnation[pray/sleep/curse/worship]")

if choices== "pray":
    # Good choice!
    print("You are still trapped in the dark, but angels of the lord are with you, I hope they're friendly...")
    sleep(delay)
elif direction == "curse":
    #terrible chice!
    print("you hear the cry and shouts of people from the outly world, screaming in agony")
    sleep(delay)
    print("it looks like your life choices have paid off")
    print("now take your rewards")
    dead= True

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!

#########################################################################################################
# TEAM 3
#good path continue
if direction == "North":
    yes_no = input("do you want to talk to him (yes/no)")
    if yes_no == "yes":
        #good choice
        print("he claims he knows where the treasure is and has no use for it")
    elif yes_no == "no":
        print("the man yells at you and starts charging you")
        dead = True
if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()
#neutral path continue
direction2 = input("which direction would you like to go(back, left, right")

#good
if direction2 == "back":
    direction3 = input("Which direction would you like to go? [North/South/East/West]")
    if direction3 == "North":
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
        print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    if dead == True:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        quit()

#########################################################################################################
# TEAM 4
nba_team = "Knicks"

print("Welcome,", nba_team, "yall play Cade n nem at MSG")
sleep(delay)
print("Cade gon have 30 either way yall just go out there and have fun")
print("Make sure KAT don't chuck no 3's")
sleep(delay)
# TODO Make sure to add the additional check if the user makes the "bad" choice!
import random
kat = random.randint(1,3)

if kat == 1:
    print("Kat drove and dunked on Tobias Harris")
# TODO Don't forget to check if your user is dead at the end of your chapter!
#########################################################################################################
# TEAM 5
import random

print("After your previous adventure, you seek another path.")
print("You're walking up the side of a mountain, desiring the title of 'Greatest Adventurer'...")
sleep(delay)
print("Legends say that those who climb the mountain never return.")
sleep(delay)
roll = input("Press Enter to roll for dexterity:")
rollValue = random.randrange(2)

if rollValue == 0:
    sleep(delay*3)
    print("Nothing happens! You carry on walking up the mountain....")
else:
    sleep(delay*3)
    print("Oh no! You tripped on a vine! Like an idiot!")
    sleep(delay)
    print("You fall hundreds of meters to the depths of the Underground onto a bed of yellow flowers.")
    sleep(delay)
    print("You, somehow still alive, look around to see the smiling face of a particularly stupid-looking flower.")
    sleep(delay)
    print('??????: \"Howdy! I\'m FLOWEY. FLOWEY the FLOWER! Hmmm... You\'re new to the UNDERGROUND, aren\'tcha? Golly, you must be so confused. \nSomeone ought to teach you how things work around here! I guess little old me will have to do.\"')
    sleep(delay)
    print("What do you want to do?")
    sleep(delay)
    while True:
        try:
            choiceFlowey = input("\n\tA:Stomp on the stupid flower \n\tB:Accept its suspicious offer \n\tC:Decline its suspicious offer (trust me, bro)\n\t")
            choiceFlowey = choiceFlowey.lower()
            if choiceFlowey == "a":
                sleep(delay *3)
                print("You killed it.")
                sleep(delay)
                print(username, ", you are a meanie, and you killed it...")
                sleep(delay)
                print("You are evil and I don't trust you")
                sleep(delay)
                print("Flowey might have been a father of over fifteen thousand seeds. (true--look it up)")
                sleep(delay)
                print("Go away, be ashamed")
                sleep(delay)
                print("You moved on with your adventure...somehow. With no remorse.")
                sleep(delay*3)
                break
            elif choiceFlowey == "b":
                sleep(delay * 3)
                print("You accepted the flower's offer.")
                sleep(delay)
                print("(I can't believe you trusted it.)")
                sleep(delay)
                print("FLOWEY: \"REALLY? You accept my offer?\" ")
                sleep(delay)
                print("FLOWEY: \"Let me show you defend yourself in this world.\" ")
                sleep(delay)
                print("You enter into a fight with the stupid-yellow flower, where it taught you how to navigate the UNDERGROUND.")
                sleep(delay)
                print("You now, feeling prepared to FIGHT some monsters, go on your merry way throughout the UNDERGROUND.")
                sleep(delay*3)
                break
            elif choiceFlowey == "c":
                sleep(delay * 3)
                print("You rejected the offer.")
                sleep(delay)
                print("He is mad.")
                sleep(delay)
                print("You are scared")
                sleep(delay)
                print("You. Are. In. Danger.")
                sleep(delay)
                print("FLOWEY: \"DIE.\"")
                sleep(delay)
                print("The ground shakes. This flower, a fifth of your size, extends from beneath you in all directions. \nGiant pinchers made of flesh and teeth form from within an overgrown mass of stupid-yellow flowers and sit on either side of you. \nPinchers which, with the force of fifteen-thousand flowers, slam shut.")
                sleep(delay)
                dead = True
                break
            else:
                sleep(delay * 3)
                print("Please choose ONLY a,b,c")

        except ValueError:
            print(" ")
    if dead == True:
        print("Woops. You died. Bummer.")
        sleep(delay * 3)
        quit()


#########################################################################################################
# TEAM 6
print("A ball lays at your foot you must kick the ball in the direction of the path you want to take.")
direction = input("Which direction would you like to kick the ball? Left, Right, Middle?")

if direction == "Left":
    #safe
    print("WOWWWWWW WHAT A SHOT, GOALLLLLLLLLLL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! You find a path out.")

elif direction == "Right":
    #dead
    print("YIKES! THAT WAS A HORRIBLE SHOT, SHOT SAVED. A HUGE BALL ROLLS TOWARDS YOU AND CRUSHES YOU.")
    dead = True
else:
    #neutral
    print("YOU ALMOST MADE BUT SADLY DIDN'T, WOMP WOMP. Ball rolls back to you.")

if dead == True:
    print("Sadly, you have failed and DIED! Run the game again and try again.")
    quit()



#########################################################################################################
# TEAM 7


#Guy is friendly and rescues us from the cave. They take you back to the town famed to have a secret treasury
#of unimaginable worth. but first, he takes you to a tavern. he offers you two drinks, one is poisonous
#and the other one contains elixir of the gods which grants you immortality.
#you can choose either one or you refuse to drink and missout on the treasure.

#if you choose the poison, the mage offers you another attempt at assessing your intelligence
#he asks if you would like something sweet with it?
#option 1, he gives you molly to add to the drink which removes the poisonous effect
#option 2, you refuse the molly and drink the poisonous drink and die
#option 3, you change your mind and decide to leave the tavern and start a new life of peace instead

#########################################################################################################
print("There seems to be someone in the cave with you. He has sensed your presence here")
sleep(delay)
print("The man assures you that you are safe and casts a spell on you")
sleep(delay * 3)
print("You wake up in a busy tavern")
print("'I'm the mage responsible for the security of this locked city', he says")
sleep(delay)
print("everyone you see here is allowed to live by our supreme commander based on their intelligence")
sleep(delay *2)
print("but you're a guest, so it's okay. Here, have a drink")

sleep(delay)
drink = input("Accept the drink from the stranger? There are two drinks 'red/blue/decline'")
if(drink == "red"):
    print("It tastes disgusting, but you feel fine")
    sleep(delay)
    print("a wonderful strength courses through your body. you feel rested to continue your adventure")
    sleep(delay)
elif(drink == "blue"):
    print("You can physically feel your stomach burning down")
    sleep(delay)
    print("You look to the mage and he smirks at you. 'You unworthy fool', he says")
    sleep(delay)
    print("Enjoy your sweet death, you are not worthy to live in our evil society")
    dead = True
else:
        print("The mage looks at you with surprise")
        sleep(delay)
        print("This tavern is famous for its drinks. but it's okay if you wish to deprive yourself")

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TEAM 8


dead = False

username = input("What is your name? ")
print()
print("Welcome", username)
print()
print("Before you there are three doors, behind one of them will lead you to a path with lots of money, and behind the other two there is certain death. You must choose correctly if you want to live")
Choose_Door = input("Choose a door! [A, B, C]")
if Choose_Door == 'A':
    print("Correct Door! You found all of the money good job!")
elif Choose_Door =='B':
    print("Wrong door! You die!")
    dead = True
else:
    print("You found the way out but you get no reward")
#########################################################################################################
# TEAM 9

direction = input("Which direction would you like to kick the ball to? [top right/bottom right/top left/bottom left]")

if direction == "top left":
    # Good choice!
    print("GOALLLLL!!!")
    sleep(delay)
elif direction == "bottom left":
    # Oh... Bad choice
    print("Oops! The goalie caught the ball. ")
    sleep(delay)
    print("Your team lost the game")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    lost = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()
#########################################################################################################
# TEAM 10

if direction == "North":
    print("You see an old man with three strands of fine gray hair. He seems to be blind. What should you do?")
    print('''A: Leave him alone in the cave
    B: Approach him and ask him how to get out of this cave''')
    answer1 = input("Write the letter of your answer (A or B): ")
    if answer1 == "B":
        print("The man growls. He can feel your presence, but apparently, he's also deaf. What should you do?")
        print('''A: Run away.
            B: Run away!!!! ''')
        answer2 = input("Write the letter of your answer (A or B): ")
        print("The man says, 'How dare you leave me, lad? You'll pay for you did to me!'")
        if answer2 == "A":
            print("He stands up and quickly comes up to you, jabbing your back until you die.")
            dead = True
        if answer2 == "B":
            print("He stands up and tries to run after you, but he accidentally breaks his ankle. He can't move, so you just run away.")
            print("Apparently, you some light somewhere in the cave. You approach the light, and you see three doors. The doors have numbers on them?")
            number = input("Which door should you choose? 5, 6, or 7?")
            if number == "6":
                print("This is the wrong door. Go back to door 7.")
                number = input("Now you can go to door 5 or door 7. Which one should you choose?")
            if number == "5":
                print("Wow! Door 5 was actually the entrance to the underground shelter, and you find very friendly people, who heads you out of the cave.")
                print("YOU HAVE ESCAPED THE CAVE!!! CONGRATS 🎉🎉🎉🎉🎉")
            if number == "7":
                print("The door suddenly closes, and you feel that your body elevates upward to heaven.")
                dead = True
else:
    print("You see a ghost telling you that the only way out is the North. The ghost heads you to the North of the cave. You see an old man with three strands of fine gray hair. He talks to the ghost and takes off his knife, stabbing you into your heart. You're dead :(")

if dead == True:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        quit()
#########################################################################################################
# TEAM 11

 direction=input("Which  direction would you like to go? [N/S/E/W]")

if direction=="N":
    print("You are trapped more with no resources")
elif direction=="S":
    print("Good choice")
    sleep(delay)
    print("You got a friend with you with some resources")
    print("Run together to move to more safer place")
elif direction=="w":
    print("You are alone but you have some resources")
    print("Run as fast as you can as there is something behind you")
    sleep(delay)
else:
    print("OOPS, You Died")
    dead=True

if dead==True:
    quit()

#########################################################################################################
# TEAM 12
base = input("Which base would you like to bake? [Vanilla, Chocolate, Red Velvet]: ")

if base == "Vanilla":
    # Good choice!
    print("Oh. Vanilla. I hate vanilla. But whatever! Whatever you like is ok. Just don't give me the final result.")
    sleep(delay)
elif base == "Chocolate":
    print("Hmm. Chocolate. Be mindful with the sugar.")
    sleep(delay)
elif base == "Red Velvet":
    print("OOOH I love red velvet!! You can't go wrong with it!")
else:
    # Neutral choice
    print("Um... We only have vanilla, chocolate, and red velvet. Anything else is sold out. I will just give you the red velvet.")
    base = "Red Velvet"
    sleep(delay)


sugar = int(input("How many cups of sugar would you like in your cake? [#]: "))

if sugar <= 2:
    print("That does not sound sweet enough.")
    print("When you bite into your cake, it tastes so bad that you die of sadness.")
    death = True
elif sugar == 3:
    print("That seems like the right amount!")
elif sugar >= 5:
    print("Okay, that seems excessive")
    print("When you bite into the cake, you can feel your glucose levels spiking. You get a heart attack from how sweet it is.")
    death = True

if dead:
    print("Yup, that could have gone better. Better luck next time... :(")

if not dead:
    print("Wow! You made an amazing cake! And for me? Thank you! You can't have a piece.")
#########################################################################################################