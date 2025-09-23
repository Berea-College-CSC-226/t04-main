#Team 14
from time import sleep

delay = 1.0
isDead = False
direction = input("Which direction do you want to go? [North,South]")

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
    try:
        numbertest = input("Pick a number 1-10 to try and survive.")
        numbertest = float(numbertest)
        if numbertest > 5 and numbertest <= 10:
            isDead = False
            print("You got lucky this time.")
        else:
            print("Unlucky, you're dead. Very sad")
            quit()
    except ValueError:
        print("Invalid input. You must enter a number.")
        quit()