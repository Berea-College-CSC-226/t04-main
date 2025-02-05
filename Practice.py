import random
username = input('What is your name? ')
print()
print("Welcome,", username, ", to the labyrinth.")
print("Before you lie two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print("\n")

print("Up ahead is a lit chamber with 3 doors, one to the East, one to the North, and one to the West.")
cardinal = input("Which door will you choose? ")
isDead = True
if cardinal == "East":
    # GOOD !!!
    print("Fortune favors you! The door you have chosen is filled to the brim with treasures unimaginable in this world!")
elif cardinal == "North":
    # Not A Good Choice
    print("Behind the door lies a small snake that upon seeing you starts to grow!")
    print("As you run away, the snake chases you as it continues to grow, expanding to fill everything behind you as your path ahead leads to a dead end...")
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
    #BADCHOICE
    print("You are now in the middle of an island alone forever, enjoy !!!")
# TODO Make sure to add the additional check if the user makes the "bad" choice!
if isDead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

# TODO Don't forget to check if your user is dead at the end of your chapter!