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

#########################################################################################################
# TEAM 3

#########################################################################################################
# TEAM 4

#########################################################################################################
# TEAM 5


#########################################################################################################
# TEAM 6



#########################################################################################################
# TEAM 7

#########################################################################################################
# TEAM 8

#########################################################################################################
# TEAM 9


#########################################################################################################
# TEAM 10

#########################################################################################################
# TEAM 11



#########################################################################################################
# TEAM 12

#########################################################################################################

