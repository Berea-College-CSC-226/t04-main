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

DELAY = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!


def start_story():
    """
    Introduction text for the story.
    Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(DELAY)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(DELAY * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(DELAY)
    return user


def end_story(user):
    """
    This is the ending to the story.
    Don't modify this function, either.

    :param user: the user's name
    :return: None
    """
    print(
        "Congratulations, " +
        user +
        ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(DELAY * 5)
    print("Now go play again.")


def kill_if_dead(is_alive):
    """
    Simple function to check if you're dead

    :param is_alive: A boolean value representing livelihood.
    :return: None
    """
    if not is_alive:
        quit()


###################################################################################
###################################################################################

def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """

    direction = input(
        "Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(DELAY)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(DELAY)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(DELAY * 2)
        print("He eats you. You are delicious.")
        return False     # kill the user!
    else:
        # Neutral choice
        print(
            '''You're in another part of the cave. It is equally dark, and equally uninteresting. 
            Please get me out of here!''')
        sleep(DELAY)
    return True       # User survives all other scenarios


###################################################################################
###################################################################################
###################################################################################

# TEAM 1


def team_1_adv(username):
    """
    https://docs.google.com/document/d/1PLwoW15mirjgG_MOtOCZAjJRucTlYP_teVuck7RF2q0/edit?usp=sharing
    Boone Riley
    Alain Irumva
    :return: None
    """

    delay = 1.0

    print("Luckily, you have a flashlight; should you use it?")
    choice_2 = input("Yes/No? ")

    if choice_2 == "Yes":
        # Good choice
        print("You discover a friendly person that offers you some food.")
        return True
    elif choice_2 == "No":
        # Bad choice
        print("You hear footsteps..")
        sleep(delay)
        print("They notice you and start screaming. In a panic you fall and hit your head on a rock")
        return False
    else:
        print("The cave is swarming with bats!")
        print("You start running..")
        sleep(delay)
        print("Suddenly, you see some light, you run toward the light")
        sleep(delay)
        print("After running forever, you make it out of the cave")
        sleep(delay)
        return True

###################################################################################

"""
https://docs.google.com/document/d/108h3SPtRrmczVZA4hlFLuJwX7khldLwqS6nj7syq3XQ/edit?usp=sharing
Elom Amuzu
Bright Feitshop
Alicia Bacani
"""

def team_2_adv(username):

    from time import sleep

    delay = 1.0
    dead = False
    username = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", username, ", to the choices of life.")
    sleep(delay)
    print("Before you lie two paths. One path leads to an afterlife, (paradise)")
    print("The other, certain death(HELL). Choose wisely.")
    print()
    sleep(delay * 2)
    print("You are in a dark cave. You can see nothing and the cold is treacherous.")
    print("Staying here is certainly not wise and the enemy might come for you. You must find your way out.")
    print("\n")
    sleep(delay)

    choices = input("what choices can you make to save yourself from damnation[pray/sleep/curse/worship]")

    if choices == "pray":
    # Good choice!
        print("You are still trapped in the dark, but angels of the lord are with you, I hope they're friendly...")
        sleep(delay)
        print("The lord is now with you. The game has ended")
        sleep(delay)


    elif choices == "sleep":
        # terrible choice!
        print("you hear the cry and shouts of people from the outly world, screaming in agony")
        sleep(delay)
        print("it looks like your life choices have paid off")
        print("now take your rewards")
        sleep(delay)
        print("...dead")
        dead = False

    elif choices == "curse":
        print("why would you do that bro")
        sleep(delay)
        print("lol you die now")
        print(username, "... dead")

    elif choices == "worship":
        print("your are now one of them...")
        sleep(delay)
        print("you're still alive, but you are nothing but food to them")
        sleep(delay)

        newchoice = input("what do you do? [ run or fight ]")

    if newchoice == "run":
        dead = True
    if newchoice == "fight":
        dead = True
        print("nice try...")
        sleep(delay)
        print("you are now dead")
    return False
###################################################################################


def team_3_adv(username):
    """
    https://docs.google.com/document/d/1YgssT-6X6hYabxt9GOj8BR_o4MrywcEW7nYmwUGPkYY/edit?usp=sharing
    DANIEL RUKWASHA
    BHUSHAN SAH
    """

    direction=input("What is the direction[North/South/East/West] ")
    if direction == "North":
        yes_no = input("Do you want to talk to him (yes/no)?")
        if yes_no == "yes":
            # good choice
            print("he claims he knows where the treasure is and has no use for it")
            return True
        elif yes_no == "no":
            print("the man yells at you and starts charging you")
            return False
    # neutral path continue
    # good
    elif direction == "East":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        DELAY
        return True
    elif direction == "South":
        # Oh... Bad choice
         print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
         DELAY
         print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
         print("Running seems like a good idea now. But... it's really, really dark.")
         print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
         print("He eats you. You are delicious.")
         return False
    else:
        print( "You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        DELAY
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        return False


###################################################################################


def team_4_adv(username):

    """
    This function is a pick your own adventure story that sets you as a NBA player your goal is to win
    the game by picking the best options.
    """

    print("Welcome, Knicks yall play Cade n nem at MSG!")
    sleep(5)
    print("Cade gon have 30 either way yall just go out there and have fun.")
    print("Make sure KAT don't chuck no 3's!")
    sleep(5)

    kat = random.randint(1, 3)

    if kat == 1:
        print("Kat took a free throw!")
        return True
    elif kat == 2:
        print("kat dunked on Tobias!")
        return True
    elif kat == 3:
        print("kat shoots a 3 point shot!")
        choice = input("you have 2 seconds left of the clock to score 1 point you have 3 options! "
              "A. try and foul to get a free throw. B. make a layup. C. make a crazy half court shot. what do you choose (A, B, or C)?")
        if choice == "A":
            print("The team did not foul you.")
            return False
        elif choice == "B":
            print("you could not make the shot before the buzzer rang.")
            return False
        elif choice == "C":
            print("you some how made the half court shot winning your team the game.")
            return True
        else:
            print("That was not an option!")
            return False


###################################################################################


def team_5_adv(username):
    """
    https://docs.google.com/document/d/1dzAfok-haJ2YMxQP-wVvN76Y-88vlwHmhbum4cHUhDc/edit?usp=sharing
    Jayden Fleming
    Artem Kurasov
    :return: Bool
    """

    alive_team_5 = True

    print("After your previous adventure, you seek another path.")
    print("You're walking up the side of a mountain, desiring the title of 'Greatest Adventurer'...")
    sleep(DELAY)
    print("Legends say that those who climb the mountain never return.")
    sleep(DELAY)

    input("Press Enter to roll for dexterity:")
    roll_value = random.randrange(2)

    if roll_value == 0:
        sleep(DELAY * 3)
        print("Nothing happens! You carry on walking up the mountain....")
    else:
        sleep(DELAY * 3)
        print("Oh no! You tripped on a vine! Like an idiot!")
        sleep(DELAY)
        print("You fall hundreds of meters to the depths of the Underground onto a bed of yellow flowers.")
        sleep(DELAY)
        print("You, somehow still alive, look around to see the smiling face of a particularly stupid-looking flower.")
        sleep(DELAY)
        print('??????: "Howdy! I\'m FLOWEY. FLOWEY the FLOWER! Hmmm... You\'re new to the UNDERGROUND, aren\'tcha? Golly, you must be so confused. \nSomeone ought to teach you how things work around here! I guess little old me will have to do."')
        sleep(DELAY)
        print("What do you want to do?")
        sleep(DELAY)
        while True:
            try:
                choice_flowey = input("\n\tA:Stomp on the stupid flower \n\tB:Accept its suspicious offer \n\tC:Decline its suspicious offer (trust me, bro)\n\t")
                choice_flowey = choice_flowey.lower()
                if choice_flowey == "a":
                    sleep(DELAY * 3)
                    print("You killed it.")
                    sleep(DELAY)
                    print(username, ", you are a meanie, and you killed it...")
                    sleep(DELAY)
                    print("You are evil and I don't trust you")
                    sleep(DELAY)
                    print("Flowey might have been a father of over fifteen thousand seeds. (true--look it up)")
                    sleep(DELAY)
                    print("Go away, be ashamed")
                    sleep(DELAY)
                    print("You moved on with your adventure...somehow. With no remorse.")
                    sleep(DELAY * 3)
                    break
                elif choice_flowey == "b":
                    sleep(DELAY * 3)
                    print("You accepted the flower's offer.")
                    sleep(DELAY)
                    print("(I can't believe you trusted it.)")
                    sleep(DELAY)
                    print("FLOWEY: \"REALLY? You accept my offer?\" ")
                    sleep(DELAY)
                    print("FLOWEY: \"Let me show you defend yourself in this world.\" ")
                    sleep(DELAY)
                    print("You enter into a fight with the stupid-yellow flower, where it taught you how to navigate the UNDERGROUND.")
                    sleep(DELAY)
                    print("You now, feeling prepared to FIGHT some monsters, go on your merry way throughout the UNDERGROUND.")
                    sleep(DELAY * 3)
                    break
                elif choice_flowey == "c":
                    sleep(DELAY * 3)
                    print("You rejected the offer.")
                    sleep(DELAY)
                    print("He is mad.")
                    sleep(DELAY)
                    print("You are scared")
                    sleep(DELAY)
                    print("You. Are. In. Danger.")
                    sleep(DELAY)
                    print("FLOWEY: \"DIE.\"")
                    sleep(DELAY)
                    print("The ground shakes. This flower, a fifth of your size, extends from beneath you in all directions. \nGiant pinchers made of flesh and teeth form from within an overgrown mass of stupid-yellow flowers and sit on either side of you. \nPinchers which, with the force of fifteen-thousand flowers, slam shut.")
                    sleep(DELAY)
                    alive_team_5 = False
                    break
                else:
                    sleep(DELAY * 3)
                    print("Please choose ONLY a,b,c")
            except ValueError:
                print(" ")

    if not alive_team_5:
            print("Woops. You died. Bummer.")
            sleep(DELAY * 3)

    return alive_team_5

###################################################################################


def team_6_adv(username):
#    Ahmed Abdoun
#    Leroy Freeman
#    https://docs.google.com/document/d/1nit5AfdSdOhGkO80dlZA_cJudYernRZ7Rr9f37wTdO8/edit?usp=sharing
    pass
    print("A ball lays at your foot you must kick the ball in the direction of the path you want to take.")
    direction = input("Which direction would you like to kick the ball? Left, Right, Middle?")

    if direction == "Left":
        # safe
        print("WOWWWWWW WHAT A SHOT, GOALLLLLLLLLLL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! You find a path out.")
        return True
    elif direction == "Right":
        # dead
        print("YIKES! THAT WAS A HORRIBLE SHOT, SHOT SAVED. A HUGE BALL ROLLS TOWARDS YOU AND CRUSHES YOU.")
        return False
    else:
        # neutral
        print("YOU ALMOST MADE BUT SADLY DIDN'T, WOMP WOMP. Ball rolls back to you.")
        return True

    #if dead == True:
     #   print("Sadly, you have failed and DIED! Run the game again and try again.")
      #  quit()

###################################################################################


def team_7_adv(username):
    """
     TEAM 7
     Mekiyan Bynum, Habiba Sorour.

     Gogole Doc: https://docs.google.com/document/d/1ivbYwafpyseBenlWDQZk8Gup2o7gaRnLvWJuRMxk74g/edit?tab=t.0#heading=h.f6tumop9n7at

     Guy is friendly and rescues us from the cave. They take you back to the town famed to have a secret treasury
     of unimaginable worth. but first, he takes you to a tavern. he offers you two drinks, one is poisonous
     and the other one contains elixir of the gods which grants you immortality.
     you can choose either one or you refuse to drink and missout on the treasure.
    """
    delay = 1


    print("There seems to be someone in the cave with you. He has sensed your presence here")
    sleep(delay)
    print("The man assures you that you are safe and casts a spell on you")
    sleep(delay * 3)
    print("You wake up in a busy tavern")
    print("'I'm the mage responsible for the security of this locked city', he says")
    sleep(delay)
    print("everyone you see here is allowed to live by our supreme commander based on their intelligence")
    sleep(delay * 2)
    print("but you're a guest, so it's okay. Here, have a drink")

    sleep(delay)

    while True:
        drink = input("Accept the drink from the stranger? There are two drinks 'red/blue/decline'")
        drink = drink.lower()
        if drink == "red":
            print("It tastes disgusting, but you feel fine")
            sleep(delay)
            print("a wonderful strength courses through your body. you feel rested to continue your adventure")
            sleep(delay)
            is_alive = True
            break
        elif drink == "blue":
            print("You can physically feel your stomach burning down")
            sleep(delay)
            print("You look to the mage and he smirks at you. 'You unworthy fool', he says")
            sleep(delay)
            print("Enjoy your sweet death, you are not worthy to live in our evil society")
            is_alive = False
            break
        elif drink == "decline":
            print("The mage looks at you with surprise")
            sleep(delay)
            print("This tavern is famous for its drinks. but it's okay if you wish to deprive yourself")
            is_alive = True
            break
        else:
            print ("Wrong response. Please choose red, blue, or decline")

    if not is_alive:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")

    return is_alive


###################################################################################


def team_8_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_9_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_10_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_11_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_12_adv(username):

    #https://docs.google.com/document/d/1B-Nr_mc_V-Xk_KcmRgWRgC649HkO5_ke6ch4Fy4-ImU/edit?usp=sharing
    #Mildred Catalina Gonzalez Molina
    #return:none
    dead=False
    base = input(
        "Which base would you like to bake?"
        " Vanilla, Chocolate, Red Velvet: "
    )
    delay=1
    if base == "Vanilla" or base=='vanilla':
        # Good choice!
        print(
            "Oh. Vanilla. I hate vanilla. But whatever! Whatever you like is ok. Just don't give me the final result.")
        sleep(delay)
    elif base == "Chocolate" or base=='chocolate':
        print("Hmm. Chocolate. Be mindful with the sugar.")
        sleep(delay)
    elif base == "Red Velvet" or base=='red velvet':
        print("OOOH I love red velvet!! You can't go wrong with it!")
    else:
        # Neutral choice
        print(
            "Um... We only have vanilla, chocolate, and red velvet. Anything else is sold out. I will just give you the red velvet.")
        base = "Red Velvet"
        sleep(delay)

    sugar = int(input("How many cups of sugar would you like in your cake? [#]: "))

    if sugar <= 2:
        print("That does not sound sweet enough.")
        print("When you bite into your cake, it tastes so bad that you die of sadness.")
        dead = True
    elif sugar == 3 or sugar==4:
        print("That seems like the right amount!")
        print("Wow! You made an amazing cake! And for me? Thank you! You can't have a piece.")
    elif sugar >= 5:
        print("Okay, that seems excessive")
        print(
            "When you bite into the cake, you can feel your glucose levels spiking. You get a heart attack from how sweet it is.")
        dead=True

    return dead

def main():

    """

    te

    The main function, where the program starts. No modifications are needed here!
    :return: None
    """
    team_12_adv("gonzalezmolinam")
    quit()

    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story()
    for i in range(len(paths)):
        is_alive = paths[i](user)  # Runs each function in the paths list
        kill_if_dead(is_alive)

    end_story(user)


if __name__ == "__main__":
    main()