######################################################################
# Author: Emily Lovell & Scott Heggen       TODO: Change this to your names
# Username: lovelle & heggens               TODO: Change this to your usernames
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

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.
injured = 0          # You start with 100% of your limbs! When this reaches two, you die!
flashlight = 0       # You have no source of light!
antisoftlock = 0     # For loops
checkGlint = 0       # Tracking!
checkPool  = 0       # ^


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
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]" )

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
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# Christson Alfaro

direction = input("Where do you want to go today?. Choose carefully hahaahhaha [Wakanda, New York, Asgard, Gotham City]")

if direction == "Asgard":
    # Well done!
    print()
    print("Wow, I'm shocked!. Good Choice!")
    print()
    print()
    sleep(delay)
    print("Thor deems you worthy to fight by his side! Welcome to Asgard", username,)
    sleep(delay)
elif direction == "Gotham City":
    #oh.. bad choice
    print()
    sleep(delay * 2)
    print("You find yourself in an dark alley, you hear two gunshots *bang, bang*")
    sleep(delay * 2)
    print("A man runs past you, no witnesses he says...")
    sleep (delay *2 )
    print ("*Bang*")
    print(username,"You're Dead")
    dead = True

elif direction == "Wakanda":
    #interesting choice
    print()
    name = input ("Are you a Wakanda citizen ?")
    if name == "Yes":
        sleep (delay *2 )
        print("Welcome back, your family missed you", username,)
    else:
        sleep (delay *2 )
        print ("You can't find Wakanda. You only see a rhino here")
        print("He looks friendly but this is boring")
        sleep (delay *2 )
else:
    #neutral choice
    print("You are in New York. Not much for you to do here")
    sleep (delay *2 )
    print("Press the green button so you can see if you have better luck next time")
    sleep(delay * 2)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# toktobaeva & coxb

print ()
print ()
direction = input ("As a Berean, no matter where you end up, you have to constantly make this hard decision: Go to dining or Go do homework, what do you say? [Go to dining/Go do homework]")
if direction == "Go to dining":
    # Good choice!
    print ()
    print("you get tired of this trivial cave and leave and head to dining to meet up friends")
    print ()
    sleep(delay*3)
elif direction == "Go do homework":
    # Bad choice!
    print ()
    sleep (delay*3)
    print("You think you are making the right choice to conform to this capitalist world.")
    sleep(delay*3)
    print ()
    print("When you, at heart, are a leftist Marxist")
    sleep(delay*3)
    print ()
    print("You know you shouldn't be enslaved by the instiution that is generally accepted in the form of")
    sleep(delay*3)
    print ()
    print("'all american college'")
    sleep(delay*3)
    print ()
    print("You graduate with a degree.")
    sleep(delay*3)
    print ()
    print("Work an 8-5 job.")
    sleep(delay*3)
    print ()
    print("Have two children.")
    sleep(delay*3)
    print ()
    print("Get old.")
    sleep(delay*3)
    print ()
    print("And, when sitting at your white wood porch, looking at your old pictures, quietly sob realizing...")
    sleep(delay*3)
    print ()
    print("that you should have gone to the dining hall")
    sleep(delay*3)
    print ()
    print ("You die a victim of this machine.")
    print ()
    print ()
    dead = True
else:
    sleep (delay)
    print ()
    print("You are not a true Berean.")
    print ()
    sleep(delay)
if dead == True:
    sleep(delay)
    print("Oh no. You are dead. Bye.")
    quit()

money = int(input ("How much is your family income?"))
if money < 30000:
    sleep (delay)
    print ()
    print ("Berea, berea, beloved")
elif money > 30000:
    sleep (delay)
    print ()
    print ("you don't belong here")
    dead = True
else:
    sleep (delay)
    print ("illiterate. bye. *middle finger emoji* *clown emoji* *middle finger emoji*")
if dead == True:
    print ("go back to the centre college where you belong.")
    quit ()

#########################################################################################################
# cullomn & coreass

print()
print("You wake up in the middle of the night to footsteps coming down the hallway.")
sleep (delay * 2)
print()
print("You could hide in the closet, go out the window, or go investigate.")
print()

choice = input("What do you want to do? (Please type closet, window, or investigate)")

if choice == "window":
    #good choice
    print()
    print("You managed to land safely in a bush. And run to a neighbor's house to call the police.")
    sleep(delay)

elif choice == "investigate":
    #bad choice
    print("While trying to investigate, you heard a loud bang.")
    print()
    sleep(delay)
    print("You got so startled that you tripped and fell down the stairs. Better luck next time!")
    dead = True

else:
    # Neutral Choice
    print("After finding your way to the closet, the footsteps enter your room")
    print()
    print("You see the shadows of the invader's feet in front of the door.")
    sleep(delay)
    print()
    print("The footsteps slowly leave your room, and downstairs you hear the front door close.")
    print("You are safe and alone, but are they coming back?")

if dead == True:
    print()
    print("Sorry you died, have a nice funeral! If you want to play again hit the green button.")
    quit()

#########################################################################################################
# Morgan's & Matilda

#Sleep is between the lines to make it so a wall of text doesn't appear at once.
print("You hear some sort of... Odd sound. Is that a dripping sound?")
sleep(delay)
print("It sounds like it's coming from a side path, though you were remaining on the main one.")
sleep(delay)
print("It might be rain from outside. Or, maybe even an underground oasis.")
sleep(delay)
print("Or, perhaps, something a lot more dangerous...")
sleep(delay * 2)
direction = input("What do you do? [Ignore, Investigate, Run like hell]")

if direction == "Ignore":
    #Good choice!
    print("You carry on down the path, ignoring the strange sound.")
    sleep(delay)
    print("As you walk, you hear the sound of water rushing behind you.")
    sleep(delay)
    print("Glancing back, you notice that water had suddenly burst from the side tunnel into the other.")
    sleep(delay)
    print("Good thing you avoided that. Close call.")

elif direction == "Investigate":
    #Bad choice!
    print("You decide, for some reason, to go check out the suspicious dripping sound.")
    sleep(delay)
    print("As you walk, you feel the droplets of water soak into your shirt, and a roaring sound fills you ears.")
    sleep(delay * 2)
    print("... Shit.")
    sleep(delay * 2)
    print("A sudden rush of water drags you along, and though you try and fight the current, it's no use.")
    sleep(delay)
    print("Guess this is the end.")
    dead=True

else:
    #Guess what? TWO BAD ENDS. AHAHHAHA.
    print("Rather than doing either option that would be somewhat sensible, you make a horrible decision.")
    sleep(delay)
    print("Breaking out into a sprint, you start to run from that location.")
    sleep(delay)
    print("Frankly, the cave's floors are slick from water.")
    sleep(delay)
    print("You trip and fall, hitting your head on the rocky floor.")
    sleep(delay)
    print("As you start to lose consciousness, you hear the sound of a creature moving somewhere nearby.")
    sleep(delay)
    print("You're perfect prey like this.")
    dead=True

if dead == True:
    sleep(delay)
    print("Ha! Guess that's the end. Good job, sucker.")
    quit()

#'s Chapter
print(" You hear an odd sound. You feel your way around and see that there are two options.")
print (" Option 1: Investigate  ")
print ( "Option 2: Scale the cave wall and go through an opening in the cave")
print ("Option 3:Stay where you are")
direction= input(" Which choice do you make? [ Option 1, Option 2, Option 3]")
if direction == "Option 1":
   print (" The odd sound belonged to an animal. You made for a tasty meal")
   dead=True
   sleep(delay)
elif direction== "Option 2":
   print (" You made  it to another part of the cave!")
   sleep(delay)
   print (" Unfortunately, you trip over a boulder, fall back through the opening, and you are now injured")
   dead=False
else:
    print (" The noise is getting louder and you are still in danger.")
    sleep(delay)
    print ("However, it appears the darkenss of the cave is keeping you alive...for now ")
    dead= False
if dead == True:
    print(" Looks like you've reached the end of the road. Better luck next time!")
    quit()

#########################################################################################################
# Dunn & Dovranov
direction = input("Where do you want to go?  [North/South/East/West]" )

if direction == "East":
    # Bad Choice
    print("You followed the light and it led to another person that was lost.")
    print("Slowly approaching the other person you fall and they now know they are not alone.")
    print("You are now injured and the other person is leaving you because of the noise.")
    print("After they have left you fall asleep.")
    sleep(delay)
    print("You awaken to the noise of bear that is approaching closer to you.")
    print("Unfortunately, you can't walk and the bear is close to you.")
    print("The bear is hungry and is looking for a delicious meal.")
    print("The bear begins to eat you.")
    print("You have one more chance to live. You see a rock.")

    userinput = input ("Can you grab it? [Yes/No]")

    if userinput == "Yes":
        print("You hit the bear and it runs off.")
    elif userinput == "No":
        print("The bear ate you.")
    else :
        print("The bear ate you.")

    dead = True



elif direction == "West":
    # Good choice
    print("You are walking in the dark and you stumble across something on the ground.")
    print("You bend over and pick it up.")
    print("It is a flashlight!")
    print("However, you are still in the dark but now you have a flashlight to see more with so you do not fall.")
    sleep(delay)

else:
    # Neutral choice
    print("You found a place to stay for the night until daytime.")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Try again by hitting the green play button.")
    quit()

#########################################################################################################
# lovelle

direction = input("Which direction would you like to go? [North/South/East/West] ")

if direction == "East":
    # Good choice
    print("You come upon an underground lake, fed by a glistening stream.")
    print("The sound of the water soothes your troubled nerves.")
    sleep(delay)
elif direction == "South":
    # Bad choice
    print("Ever so suddenly, you find yourself surrounded by ogres twice your size.")
    print("They realize you are harmless and you catch your breath. It seems they might let you pass...")
    sleep(delay * 3)
    print("They strike up a song, ready to continue on their way.")
    print("Oh, but how loud their voices are! And you aren't feeling so good...")
    sleep(delay * 3)
    print("The leader asks you to rank the quality of their singing, on a scale of 1 to 10.")
    rating = int(input("What do you say? Choose wisely; your life depends on it... "))
    if rating < 10:
        print("You fall to the ground, feeling the power of a cursed song. Looks like your time is up, friend.")
        dead = True
    else:
        print("The ogre thanks you for the complement and sends you on your merry way.")
else:
    # Neutral choice
    print("Phew, you're still on solid ground. But still in the dark. Think fast!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. And what a shame it had to happen this way.")
    print("Better luck next time - try again by hitting the green play button!")
    quit()

#########################################################################################################
# Eppersonb & Barnetth

print()
print(username, "continues on their quest")
sleep(delay)
print("You continue your path in the forest")
print("As you walk through the forest, you encounter a bear wearing a fez and sunglasses.")
print(
    "You notice that the fez has the name 'Bosco' labeled on it. You deduce that this is the famous runaway circus bear, Bosco the Bear.")
sleep(delay)
print()
print("However, Bosco has took notice of you and stands on his hind legs and takes interest in you.")
print("You must make a choice, or it could end very badly for you!")

choice = input("What would you like to do? [Entertain or Fight?]")

if choice == "Fight":
    #Good Choice!
    print("You choose to engage in fisticuffs with Bosco the Bear. This seems like a very bad idea.")
    print()
    sleep(delay)
    print("Luckily for you, Bosco the Bear lived in the circus his whole life. He does not know how to fight.")
    print("Feeling intimated, Bosco the Bear flees. Dropping his fez and glasses.")
    print()
    print("You are free to continue on your journey while rocking the fez and glasses. Well at least you look nice.")
    print()
elif choice == "Entertain":
    # Bad Choice
    print("Bosco the Bear is not amused with your performance.")
    print()
    sleep(delay)
    print("He ran away from the circus because he hated that life.")
    print("Your entertainment reminded him of that hatred. How inconsiderate of you.")
    print()
    sleep(delay)
    print("In a fit of rage, Bosco the Bear kills you with his bare hands.")
    print()
    dead = True
else:
    #Neutral Choice
    print("Bosco the Bear is confused by your actions.")
    print("Bosco the Bear does not see you as a threat and leaves.")
    print()
    print("You are free to continue on your journey.")
    print()

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hiting the green play button. ")
    quit()

#########################################################################################################
# Guillermo & Tanner

#We pick it up from the point where you are in a dark room with a stranger. What happens next?
decision = input("The stranger tells you that he knows the way out, but you have to follow his every word. What is your decision? [I trust you/No way, No thank you] ")

if decision == "I trust you" :
    #Good choice!
    print("The stranger is overcome with joy, and hands you flashlight and a ham sandwich.")
    sleep(delay)

elif decision == "No way" :
    #Bad choice...
    print("Your unwillingness to trust the stranger angers him. He begins to chase you through the dark cave, and you find a place to hide. You hide there for several days.")
    sleep(delay)
    print("After several days of hiding, you begin to fell fatigued. You lose consciousness, and the stranger is able to find your body and he dismembers you.")
    dead = True

else:
    print("You respectfully decline his offer, and decide to wonder around in the dark by yourself. You wonder in the dark for hours, and make no progress. ")
    sleep(delay)

if dead == True:
    print("You died, oh no! Try again by hitting the green button.")
    quit()

#########################################################################################################
# hilljac & nudgarrobot

direction = input("Which direction would you like to go? [North/South/East/West]" )

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

         #branching good path
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
            if dead == True:
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
        if dead == True:
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
        #TODO Flesh out choices for flashlight-enabled play!
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
        while antisoftlock == 0:
            choice = input("[Follow wall]/[Venture into dark]/[Retreat through tunnel]")
            if choice == "Follow wall":
                print("Placeholder text, you follow the wall.")
                antisoftlock = antisoftlock + 1
            elif choice == "Venture into dark":
                print("Placeholder text, you leave the wall and walk into the inky blackness.")
                antisoftlock = antisoftlock + 1
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

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# jamalie & juem

direction = input("There is a river in your path, what would you do to cross the river? (swim, make a bridge,etc)")
sleep(delay)
if direction == "make a bridge":
    # this is the best choice!
    print("Well done, you have made a wise choice")
    print("you reward is that you will survive and explore more of the jungle")
    sleep(delay)
elif direction == "swim":
    # surprisingly, this is a bad choice!
    print("Oh,no! Just like Goblet of Fire, there are deadly mermaids looking for fresh blood")
    print("you will be dragged down the ocean to be eaten at a feast")
    sleep(delay*3)
    print("Now you're in their territory, you see some Gillyweeds just next to where you're trap")
    sleep(delay*3)
    print("You should be careful with eating Gillyweed")
    direction = int(input("You have the option to eat between 1-3 strands of Gillyweed, what will you do?"))
    if direction <= 2:
        # Good idea
        print("Good job! now you have more strength and you can breath under water!")
        sleep(delay*3)
        print("fight them and survive")
    elif direction > 2 and direction <= 3:
        # this is a bad idea
        print("Too much Gillyweed will cause suffocation!")
        dead = True
        sleep(delay*5)
    else:
        # We would like the user to use whole number
        print("Since you did not choose from the given numbers, your only chance is to fight and survive")
else:
    # this is a neutral choice!
    print("Well done for the creativity! you crossed the river!")
    sleep(delay*3)
    print("but...")
    sleep(delay*3)
    print("you got injured for the hard work, so you can't move on and you need to rest by the river")
    sleep(delay)
if dead == True:
    print("oops.. I guess that's all for you!")
    sleep(delay*3)
    print("you were not very successful this time")
    sleep(delay*3)
    print("see you in your next journey")

#########################################################################################################
# nashab & phillipsvi

print()
print("To your left, you notice a house. Curious... Looking around more, you see a cat behind you.")
print("The cat has seven tails and a missing eye. You ponder for a moment. You feel sleepy.")
sleep(delay * 2)
print()

direction = input ("What will you do? [House/Cat/Sleep]")

if direction == "House":
    #bad choice
    print("You decide that you need help and make your way towards the house. The path is a bit rocky though...")
    sleep(delay)
    print("...")
    sleep(delay)
    print("......")
    sleep(delay)
    print(".........")
    sleep(delay * 2)
    print("Oh no! You tripped on a rock! It was so shocking, you die before you hit the ground.")
    dead = True

elif direction == "Cat":
    # neutral choice
    print("The cat is just so damn intriguing, you can't help but examine it.")
    print("You stretch out your hand, and the cat nuzzles you, its several tails twitching affectionately.")
    print("This is nice, but accomplishes nothing.")
    sleep (delay)
    print()
    print ("You waste time loving the cat, but nothing gets done.")
    sleep (delay)
    dead == False

else:
    print ("You disregaurd that because you fell asleep.")
    sleep (delay * 5)
    print ("You awake feeling refreshed.")
    dead == False

if dead == True:
    print("What a sad way to die.")
    quit()

#########################################################################################################
# prattw & phillipsde

print()
print('An eerie box lays before you, and for some reason you are drawn to it.')
print()
print('As you draw closer you hear a voice in your head...')
print()
print('"In order to receive the treasures of the box you must reveal your deepest and darkest secret"')

choice = input('Will you reveal your secret? [Yes/No]')

if choice == "Yes" or choice == "Y":
    secret = input('Speak now and reveal the truth.')
    print(secret)
    print("The box opens and you reach inside to retrieve your treasure...")
    sleep(delay)
    print()
    print('''It's a flower with petals made of fire and a note that says, "It's a me, copyright."''' )
    sleep(delay)
    print()
    print('Confused by the note, you take your reward and move on.')
    print()
    sleep(delay)
elif choice == "No" or choice == "N":
    death = input('Will you open the box? [Yes/No]')
    if death == "Yes":
        print('You attempt to open the box but you become consumed by a deadly darkness that envelops your body.')
        print()
        print('You died. LOL')
        revive=input("would You like to restart")
        if revive=="Yes":
            riddle=input("What starts with 'e' ends with 'e' and contains one letter? "
                  "[a/an]")
            if riddle=="envelope":
                    print("you live good job but you don't get the treasure")
        if revive=="No":
            print("ah its your choice")
            quit()
    elif death == "No":
            print('You decide not to open the box.')
            print()
            print('You feel like you have avoided some mysterious danger but missed out on some sweet loot.')
else:
    print("You walk away")
#hi

#########################################################################################################
# mayerss & kinyunaa

jump = input("which direction would you like to go?[jump/stay/parachute]")

if jump == "jump":
    #bad choice
    print("you fall from the sky and land on your head..")
    print("your skull burst open and your brains spread everywhere")
    print("your chances of survival are zero")
    print("youre dead meat")
    dead = True
    sleep(delay)

elif jump == "parachute":
    #good choice
    print("Open your parachute at approximately 1000 feet and you avoid injury")
    print("Congratulations you passed your parachute test today!")


else:
    print("you decided to stay. so now you are alone in the cave and have to find your way out")

if dead == True:
    print("You died at least you dont have to take 226 anymore :)")

#########################################################################################################
# stettner & vankirk

direction = input(" You see a ladder in front of you and hear Water to the right. Do you want to go for a Swim or Climb the ladder? "
                  "[Swim, Climb]")
print()
if direction == "Climb":
    print(" When you reach the top of the ladder you come face to face with a demented clown")
    print("The clown jumps at you causing you to fall back and break your right arm but as you were falling you caught a glimpse "
          "of a tunnel to your left.")
    sleep(delay)

    direction == input (" Would you like to take a Hike or go for a Swim? [Hike, Swim]")

elif direction == "Swim":
    print("As you go into the water you see a faint outline of a hole accros from you and you begin to swim towards it.")
    print("With your nose almost even with the watter you are able to fit through the hole.")
    sleep(delay)


if direction == "Hike":
    sleep(delay)
    print("As you go down the path to your left, you hear a large form coming for you. "
          "You start running instinctively but you are not fast enough... ")
    dead = True

else:
    print("That was not an option!")
dead= True

if dead == True:
    sleep(delay)
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# stetzera and whitfordr

print()
print("A figure emerges from the shadows, hunched and withered. Her single good eye turns to face you -- a witch!")
sleep(delay)
print("Two more eyes blink out of the darkness, the witch's black cat slinking their way out from around the hem of her dress.")
sleep(delay)
#Exposition for the upcoming choices.

choice = input("The witch stares at you, blocking the way forward. What do you do? [Pet the cat/Attack the witch/Run away]")

if choice == "Pet the cat":
    #Cats always equal best choice.
    print("You kneel down, holding out a hand to the cat.")
    print("The kitty pads forward, sniffing at you...")
    sleep(delay *5)
    print("The little black cat purrs.")
    print("With a throaty laugh the witch shuffles to the side, apparently trusting her cat's judgement. You're free to go!")

elif choice == "Attack the witch":
    #What sort of idiot attacks a mysterious woman with a cat? How rude.
    print("Fearing for your life -- it's a witch, who trusts witches? -- you pull out a dagger from the sheathe at your belt.")
    print("With a echoing bellow you rush forward, only to find yourself frozen in place.")
    print("A hex!")
    dead = True

elif choice == "Run away":
    #Arguably the most rational.
    print("Not your circus, not your monkeys.")
    print("You just turn around, avoid eye contact and meander back into the darkness of the cave from whence you came.")

else:
    #Neutral/indecisive choice.
    print("You find yourself full of strange thoughts, pulled backwards into the labyrinth once more.")
    sleep(delay)

if dead == True:
    print("Your muscles lock up, which, unfortunately, includes your heart.")
    sleep(delay)
    print("As your lifeless body falls to the ground, the witch and cat both turn, melting back into the shadows of the cave.")
    print("Serves you right for attacking a mostly-defenseless old woman.")
    print("Better luck next time! Try again by hitting the green play button.")
    quit()


#########################################################################################################
print()
print("Deeper in the cave, you hear the sound of someone crying!")
sleep(delay)
print("As you investigate the noise, you discover that it is coming from a little girl in a pink dress.")
sleep(delay)

choice = input("She looks up at you tearfully, huddled against the wall. What do you do? [Pick her up/Interrogate her/Back away slowly]")

if choice =="Interrogate her":
    print("Frankly you find this to be a bit suspect. What's a little kid doing in some kind of creepy magic cave?")
    sleep(delay)
    print("You point an accusatory finger at her and ask what her deal is")
    print("she immediately stops crying and looks grumpy instead. She sticks her tongue out at you and turns into a bat, flying away")
    print("Welp. guess you dodged that bullet.")

elif choice =="Back away slowly":
    print("Ok you never signed up to be a childcare service. This is someone else's problem. You turn and leave")
    sleep(delay)
    print("The little girl looks at you incredulously but doesn't stop you")


elif choice =="Pick her up":
    print("Despite your best efforts to calm her, the girl keeps crying. ...but after a moment, her cries begin to change.")
    sleep(delay)
    print("you realize she is laughing just as sharp fangs pierce your neck. You fall to the ground in surprise")
    print("As you look up, you realize that her eyes have turned deep red! Vampire!")
    dead = True

else:
    print("Before you can decide what to do about the little kid, the ground collapses beneath you")
    sleep(delay)
    print("You find yourself in a totally different tunnel. A bit startled, but miraculously unhurt.")

if dead == True:
    print("As your consiousness fades away, her giggles continue.")
    print("This is what you get for trying to help kids lost in caves apparently")
    print("Better luck next time! Try again by hitting the green play button.")
    quit()

#########################################################################################################
# westth & whitakerj

Move = input("You see a cell phone up ahead. Do you want to pick it up, leave it where it is, or try to watch youtube videos? Type pick up, leave it or youtube, please. ")

if Move == "pick up" or "Pick up":
    #This will be good later on. To call for help.
    print("Since you did not turn it on this could be helpful in the future.")
    sleep(delay)
elif Move == "youtube" or "Youtube":
    #Oh no... this isn't going to be good
    print("Loud volume came out of the speakers, it was a bears mating call, the bear was NOT happy that you were not another bear.")
    sleep(delay)
    dead = True
else :
    #Nothing happens, the volume doesn't turn on and you can't call for help later
    print("You left the phone. Oh well.")

if dead == True:
    print("Oh no, your dead by a mating bear.")
    quit()
