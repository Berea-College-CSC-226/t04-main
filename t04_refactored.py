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


def places_to_go():
    """
    https://docs.google.com/document/d/1ydkRlcWI9bj7BYYdBTKScwrTixQgIL6u_Hl1hY28p98/edit?usp=sharing
    The docstring is linked to the Google Doc for the Teamo4 Assignment of toktobaeva and alfaro
    The function places_to_go() you are faced with a decision to choose between cities: Wakanda, Asgard, New You or Gotham City
    :return: None
    """

    global dead
    direction = input("Where do you want to go today?. Choose carefully hahaahhaha [Wakanda, New York, Asgard, Gotham City]")

    if direction == "Asgard" or direction=="asgard":
        # Well done!
        print()
        print("Wow, I'm shocked!. Good Choice!")
        print()
        print()
        sleep(delay)
        print("Thor deems you worthy to fight by his side! Welcome to Asgard")
        sleep(delay)
    elif direction == "Gotham City" or direction=="gotham city":
        # oh.. bad choice
        print()
        sleep(delay*2)
        print("You find yourself in an dark alley, you hear two gunshots *bang, bang*")
        sleep(delay*2)
        print("A man runs past you, no witnesses he says...")
        sleep(delay*2)
        print("*Bang*")
        print("You're Dead")
        dead = True
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")


    elif direction=="Wakanda" or direction=="wakanda":
        # interesting choice
        print()
        name = input("Are you a Wakanda citizen ?")
        if name == "Yes":
            sleep (delay *2)
            print("Welcome back, your family missed you")
        else:
            sleep (delay*2)
            print ("You can't find Wakanda. You only see a rhino here")
            print("He looks friendly but this is boring")
            sleep (delay*2)
    else:
        # neutral choice
        print("You are in New York. Not much for you to do here")
        sleep (delay*2)
        print("Press the green button so you can see if you have better luck next time")
        sleep(delay*2)

    kill_if_dead(dead)






def team_2_adv():
    """
    Google Doc: https://docs.google.com/document/d/19jYjDRX_WR4pPynsAYmeglDpQWDvNVMDgYvd4EUWqm8/edit?usp=sharing
    Goes through the berea section of the story. Asks if you want to go to dining or go do homework.
    Choosing either will take you to two possibilities of being "dead" or being asked how much money you have.
    This choice then will make you "dead" or will continue on the "story" to the next function
    """
    global dead
    print()
    print()
    direction = input ("As a Berean, no matter where you end up, you have to constantly make this hard decision: Go to dining or Go do homework, what do you say? [Go to dining/Go do homework]")
    if direction == "Go to dining" or "go to dining":       # Good choice! asking if they want to go to dining
        print()
        print("you get tired of this trivial cave and leave and head to dining to meet up friends")
        print()
        sleep(delay*3)
    elif direction == "Go do homework" or "go do homework":  # Bad choice! asking if they want to do homework
        print()
        sleep(delay*3)
        print("You think you are making the right choice to conform to this capitalist world.")
        sleep(delay*3)
        print()
        print("When you, at heart, are a leftist Marxist")
        sleep(delay*3)
        print()
        print("You know you shouldn't be enslaved by the institution that is generally accepted in the form of")
        sleep(delay*3)
        print()
        print("'all american college'")
        sleep(delay*3)
        print()
        print("You graduate with a degree.")
        sleep(delay*3)
        print()
        print("Work an 8-5 job.")
        sleep(delay*3)
        print()
        print("Have two children.")
        sleep(delay*3)
        print()
        print("Get old.")
        sleep(delay*3)
        print()
        print("And, when sitting at your white wood porch, looking at your old pictures, quietly sob realizing...")
        sleep(delay*3)
        print()
        print("that you should have gone to the dining hall")
        sleep(delay*3)
        print()
        print("You die a victim of this machine.")
        print()
        print()
        dead = True
    else:                                                   #user inputs something other than the dining or homework asnwers
        sleep(delay)
        print()
        print("You are not a true Berean.")
        print()
        sleep(delay)
    if dead == True:                                        #end of the homework answer
        sleep(delay)
        print("Oh no. You are dead. Bye.")
        quit()

    money = int(input ("How much is your family income?"))   #ask what family income is
    if money < 30000:                                        #does the print if they asnwer with something below 30000
        sleep (delay)
        print()
        print("Berea, berea, beloved")
    elif money > 30000:                                      #does the print if they answer with something above 30000
        sleep(delay)
        print()
        print("you don't belong here")
        dead = True
    else:                                                    #catches any answers that are not the ones we want
        sleep(delay)
        print("illiterate. bye. *middle finger emoji* *clown emoji* *middle finger emoji*")
    if dead == True:
        print("go back to the centre college where you belong.")
        quit()

def team_3_adv():
    """
    This branch was created by Guillermo and Adam.
    Google Doc Link: https://docs.google.com/document/d/1B75UoewLi3qD1kfC3ptPuWox-RwT00VteOleVjZUbro/edit?usp=sharing
    :return:
    """

    decision = input("The stranger tells you that he knows the way out, but you have to follow his every word. What is your decision? [I trust you/No way, No thank you] ")
    global dead
    if decision == "I trust you":
        # Good choice! This will reward the user, and keep the user alive.
        print("The stranger is overcome with joy, and hands you flashlight and a ham sandwich.")
        sleep(delay)

    elif decision == "No way":
        # Bad choice... This will kill the user, and terminate the code.
        print("Your unwillingness to trust the stranger angers him. He begins to chase you through the dark cave, and you find a place to hide. You hide there for several days.")
        sleep(delay)
        print("After several days of hiding, you begin to fell fatigued. You lose consciousness, and the stranger is able to find your body and he dismembers you.")
        dead = True
        print("You died, oh no! Try again by hitting the green button.")
        quit()

    else:
        # Neutral choice, this choice will not help or hurt the user, and will keep them alive.
        print("You respectfully decline his offer, and decide to wonder around in the dark by yourself. You wonder in the dark for hours, and make no progress. ")
        sleep(delay)


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():
    """
    Google doc: https://docs.google.com/document/d/1BzQqW9mFzMhzRlAyL1DkV31Ps5QJOwXgqQtEBJ4gJAI/edit?usp=sharing
    Team 5's refactored chapter
    Originally by Dunn & Dovranov , refactored by Jacob Hill, Bryan Epperson, Susan Coreas
    :return: None
    """
    # Dunn & Dovranov
    # Refactored by Team 5

    global dead

    direction = input("Where do you want to go?  [North/South/East/West]")

    if direction == "East" or direction == "east":
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

        userinput = input("Can you grab it? [Yes/No]")

        if userinput == "Yes":
            print("You hit the bear and it runs off.")
        elif userinput == "No":
            print("The bear ate you.")
        else:
            print("The bear ate you.")

        dead = True

    elif direction == "West" or direction == "west":
        # Good choice
        print("You are walking in the dark and you stumble across something on the ground.")
        print("You bend over and pick it up.")
        print("It is a flashlight!")
        print("However, you are still in the dark but now you have a flashlight to see more with so you do not fall.")
        sleep(delay)

    elif direction == "North" or direction == "north":
        # Neutral choice
        print("You found a place to stay for the night until daytime.")
        sleep(delay)

    elif direction == "South" or direction == "south":
        # Neutral choice
        print("You found a place to stay for the night until daytime.")
        sleep(delay)

    else:
        print("That is not a direction! Please input a direction")
        team_5_adv()

    if dead == True:
        print("Oh no! You died. Try again by hitting the green play button.")
        quit()



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
    """
    Team 7's refactored chapter.
    Originally done by EppersonB and BarnettH, refactored by BarnettH and DunnA
    google doc link: https://docs.google.com/document/d/1PeAwI9PZtPMI5_4KJMAsPv3blZDpBLS_9ZuFGaBhayg/edit?usp=sharing
    :return: None
    """
    global dead
    print()
    print("You continue your path in the forest")
    print("As you walk through the forest, you encounter a bear wearing a fez and sunglasses.")
    print("You notice that the fez has the name 'Bosco' labeled on it. You deduce that this is the famous runaway circus bear, Bosco the Bear.")
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



def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():
    pass
    # TODO Add your code here


def team_10_adv():
    pass
    # TODO Add your code here


def cullomn_whitfordr(): # Refactored by Team 11
    """
    Journey to a house.
    https://docs.google.com/document/d/1trPAy_4RAI__kv4UXJYL8SUDABny1Yp-sSZgqdX9sFE/edit?usp=sharing
    :return:
    Print statements.  No return. None.
    """
    print()
    print("To your left, you notice a house. Curious,... Looking around more, you see a cat behind you.")
    print("The cat has seven tails and a missing eye. You ponder for a moment. You feel sleepy.")
    sleep(delay * 2)
    print()
    direction = input("What will you do? [House/Cat/Sleep]")

    if direction == "House" or direction == "house":
        # bad choice
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

    elif direction == "Cat" or direction == "cat":
        # neutral choice
        print("The cat is just so damn intriguing, you can't help but examine it.")
        print("You stretch out your hand, and the cat nuzzles you, its several tails twitching affectionately.")
        print("This is nice, but accomplishes nothing.")
        sleep(delay)
        print()
        print("You waste time loving the cat, but nothing gets done.")
        sleep(delay)
        dead = False

    else:
        print("You disregard that because you fell asleep.")
        sleep(delay * 5)
        print("You awake feeling refreshed.")
        dead=False

    if dead:
        print("What a sad way to die.")
        quit()

def westth_benningfield():
    """ inputs the room we were asked to refactor.
    link to our google doc: https://docs.google.com/document/d/11l9OqTJTGxCbiatW3S5czFA036_AvCPBq0RjwNz4eaA/edit?usp=sharing"""
    print()
    print('An eerie box lays before you, and for some reason you are drawn to it.')
    print()
    print('As you draw closer you hear a voice in your head...')
    print()
    print('"In order to receive the treasures of the box you must reveal your deepest and darkest secret"')

    choice = input('Will you reveal your secret? [Yes/No]')

    if choice == "Yes" or choice == "Y" or choice == "yes":
        secret = input('Speak now and reveal the truth.')
        print(secret)
        print("The box opens and you reach inside to retrieve your treasure...")
        sleep(delay)
        print()
        print('''It's a flower with petals made of fire and a note that says, "It's a me, copyright."''')
        sleep(delay)
        print()
        print('Confused by the note, you take your reward and move on.')
        print()
        sleep(delay)
    elif choice == "No" or choice == "N" or choice == "no":
        death = input('Will you open the box? [Yes/No]')
        if death == "Yes" or choice == "Y" or choice == "yes":
            print('You attempt to open the box but you become consumed by a deadly darkness that envelops your body.')
            print()
            print('You died. LOL')
            revive = input("would You like to restart")
            if revive == "Yes" or choice == "Y" or choice == "yes":
                riddle = input("What starts with 'e' ends with 'e' and contains one letter? ""[a/an]")

                if riddle == "envelope":
                    print("You live. Good job! However, you don't get the treasure.")
            if revive == "No" or choice == "N" or choice == "no":
                print("ah its your choice")
                quit()
        elif death == "No" or choice == "N" or choice == "no":
            print('You decide not to open the box.')
            print()
            print('You feel like you have avoided some mysterious danger but missed out on some sweet loot.')
    else:
        print("You walk away")
    pass
    # TODO Add your code here


def team_13_adv():
    # tori and jessie
    # https://docs.google.com/document/d/1oPzq92-44tG37zoKnEG_hnjtZtgnz1UUe1kYTGTp81A/edit?usp=sharing

    print()
    print("You find yourself on a cliff. There doesn't seem to be a path down. You chance a glance over the edge")
    print("Seems like a long way...")
    print()

    jump = input("What would you like to do?[jump/stay/parachute]")

    if jump == "jump" or jump == "Jump" or jump == "j" or jump == "J" or jump == " jump" or jump == " Jump" or jump == " j" or jump == "J":
        # bad choice
        print("You fall from the sky and land on your head...")
        sleep(delay)
        print("Your skull burst open and your brains spread everywhere")
        sleep(delay)
        print("Your chances of survival are zero.")
        sleep(delay * 2)
        print("You're dead meat.")
        print()
        dead = True
        if dead is True:
            print("You died, but at least you don't have to take 226 anymore. :)")
            quit()

    elif jump == "parachute" or jump == "Parachute" or jump == "p" or jump == "P" or jump == " parachute" or jump == " Parachute" or jump == " p" or jump == " P":
        # good choice
        print("You open your parachute at approximately 1000 feet and you avoid injury.")
        sleep(delay * 2)
        print("Congratulations, you passed your parachute test!")
        print()

    elif jump == "stay" or jump == "Stay" or jump == "s" or jump == "S" or jump == " stay" or jump == " Stay" or jump == " s" or jump == " S":
        print("You decided to stay. The wind is pretty fierce this high up.")

    else:
        print("What was that?")
        print()




def team_14_adv():
    """
    Team 14's refactored chapter.
    https://docs.google.com/document/d/165eAoj1XNMW9XfruJp3p0qiJc1H9ZdS3PNCT9htqiPQ/edit?usp=sharing


    """

    global dead

    direction = input("As you enter a new part of the cave you see a ladder in fron of you, you hear water to your right,"
                      "and see a tunnel to your right. Would you like to Swim, Hike, or Climb?"
                      "[Swim,Hike,or Climb]")

    if direction == "Swim":
        print("As you go into the water you see a faint outline of a hole accros from you and you begin to swim towards it.")
        print("With your nose almost even with the watter you are able to fit through the hole.")
        sleep(delay)

    elif direction == "Climb":
        print(" When you reach the top of the ladder you come face to face with a demented clown")
        print("The clown jumps at you trying to grab you and you slip and fall back down")
        sleep(delay)
        dead = True

    elif direction == "Hike":
        print("As you are walking down the new tunnel you hear something large following behind you!"
              "You become more and more scared and breakout into a sprint tryig to get away from whatever "
              "is following you...")
        print("You were not fast enough...")
        dead = True

    else:
        print("Sorry that was not an option please choose again.")
        team_14_adv()

    if dead == True:
        sleep(delay)
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button.")
        quit()
        # TODO Add your code here


def team_15_prattw_vankirkj():
    """
    Team 15's refactored chapter.
    Originally by stetzera and whitfordr, refactored by prattw and vankirkj.
    https://docs.google.com/document/d/15Vn_ovikxYFLnAGB2R_f8-kFiFdRDe6teK0p_NSIZzo/edit?usp=sharing
    :return: none
    """
    # stetzera and whitfordr
    # Refactored by Team 15
    global dead

    print()
    print("A figure emerges from the shadows, hunched and withered. Her single good eye turns to face you -- a witch!")
    sleep(delay)
    print("Two more eyes blink out of the darkness, the witch's black cat slinking their way out from around the hem of her dress.")
    sleep(delay)
    # Exposition for the upcoming choices.

    choice = input("The witch stares at you, blocking the way forward. What do you do? [Pet the cat/Attack the witch/Run away]")

    if choice == "Pet the cat" or choice == "pet the cat":
        # Cats always equal best choice.
        print("You kneel down, holding out a hand to the cat.")
        print("The kitty pads forward, sniffing at you...")
        sleep(delay * 5)
        print("The little black cat purrs.")
        print("With a throaty laugh the witch shuffles to the side, apparently trusting her cat's judgement. You're free to go!")

    elif choice == "Attack the witch" or choice == "attack the witch" or choice == "dab":
        # What sort of idiot attacks a mysterious woman with a cat? How rude.
        # the dab is a special easter egg :D
        print("Fearing for your life -- it's a witch, who trusts witches? -- you pull out a dagger from the sheathe at your belt.")
        print("With a echoing bellow you rush forward, only to find yourself frozen in place.")
        sleep(delay * 2)
        print("A hex!")
        dead = True

    elif choice == "Run away" or choice == "run away":
        # Arguably the most rational.
        print("Not your circus, not your monkeys.")
        print("You just turn around, avoid eye contact and meander back into the darkness of the cave from whence you came.")

    else:
        # Neutral/indecisive choice.
        print("You find yourself full of strange thoughts, pulled backwards into the labyrinth once more.")
        sleep(delay * 5)

    if dead:
        print("Your muscles lock up, which, unfortunately, includes your heart.")
        sleep(delay)
        print("As your lifeless body falls to the ground, the witch and cat both turn, melting back into the shadows of the cave.")
        print("Serves you right for attacking a mostly-defenseless old woman.")
        print("Better luck next time! Try again by hitting the green play button.")
        quit()

    # TODO Add your code here


def dovranovs_adventure():
    """
    This code gives user choices when user found a little crying girl and define what is gonna happen if user selects one of the options.




    https://docs.google.com/document/d/16R-KA0PvMLgTYy4DjvFSHpCJNWzw6fgGkAn_TYCmlr0/edit?usp=sharing
    # Originally by Team 16
    # Refactored by Sahet Dovranov

        """
    # Beginning description
    global dead
    print()
    print("Deeper in the cave, you hear the sound of someone crying!")
    sleep(delay)
    print("As you investigate the noise, you discover that it is coming from a little girl in a pink dress.")
    sleep(delay)

    # Giving choices to user and ask to pick one.
    choice = input("She looks up at you tearfully, huddled against the wall. What do you do? [Pick_her_up/Interrogate_her/Back_away_slowly]")

    if choice == "Interrogate_her":
        # Neutral choice.
        print("Frankly you find this to be a bit suspect. What's a little kid doing in some kind of creepy magic cave?")
        sleep(delay)
        print("You point an accusatory finger at her and ask what her deal is")
        print("she immediately stops crying and looks grumpy instead. She sticks her tongue out at you and turns into a bat, flying away")
        print("Well. guess you dodged that bullet.")
        dead = False

    elif choice == "Back_away_slowly":
        # Neutral choice.
        print("Ok you never signed up to be a childcare service. This is someone else's problem. You turn and leave")
        sleep(delay)
        print("The little girl looks at you incredulously but doesn't stop you")
        dead = False
    elif choice == "Pick_her_up":
        # Bad choice.
        print("Despite your best efforts to calm her, the girl keeps crying. ...but after a moment, her cries begin to change.")
        sleep(delay)
        print("you realize she is laughing just as sharp fangs pierce your neck. You fall to the ground in surprise")
        print("As you look up, you realize that her eyes have turned deep red! Vampire!")
        dead = True
    else:
        # Neutral choice.
        print("Before you can decide what to do about the little kid, the ground collapses beneath you")
        sleep(delay)
        print("You find yourself in a totally different tunnel. A bit startled, but miraculously unhurt.")
        dead = False

    if dead == True:
        print("As your consiousness fades away, her giggles continue.")
        print("This is what you get for trying to help kids lost in caves apparently")
        print("Better luck next time! Try again by hitting the green play button.")
        quit()

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
    paths = [scott_adventure, places_to_go(), team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, cullomn_whitfordr,
             westth_benningfield, team_13_adv, team_14_adv,
             team_15_prattw_vankirkj, dovranovs_adventure, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story(user)


main()
