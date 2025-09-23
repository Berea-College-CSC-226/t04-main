# TEAM 18
from time import sleep

delay = 2
dead = False
rich = False
way = input("Which path do you want to go? [Left, Right, Forward, Dead] ").strip().capitalize()
print(way)
if way == "Left":
    # Bad choice
    print("\n")
    print("You walked on the left path. This was the wrong way and you are stuck inside.")
    sleep(delay)
    print("You have no food and slowly starve.")
    dead = True

elif way == "Right":
    # Neutral choice
    print("\n")
    print("You continue walking on the right path and nothing happens.")
    sleep(delay)
    print("At least you are still alive!")
    print("\n")
elif way == "Dead":
    print("Game Over! You died.")
    exit()  # stops the program
    sleep(delay)
else:
    # Good choice
    print("\n")
    print("You chose the path forward and found $1,000,000")
    sleep(delay)
    print("You can do anything you ever wanted with all the money.")
    print("\n")
    rich = True

print("You walk out into an opening and see a man sitting down.")
sleep(delay)
print("He has a lot of things next to him including bread and a knife.")
sleep(delay)
print("Buy the knife, steal the bread, or continue?")
way = input("What are you gonna do? [Buy, Steal, Continue] ").strip().capitalize()

if way == "Buy":
    # Good choice if you are rich
    print("\n")
    print("You bought all the bread you're not hungry anymore.")
    sleep(delay)
    print("\n")
elif way == "Steal":
    # Bad choice
    print("\n")
    print("You tried to snatch the bread.")
    sleep(delay)
    print("Before you could run, the guy shoots you in the back of the head.")
    sleep(delay)
    print("So... no bread! And you died!")
    dead = True
elif way == "Continue":
    # Neutral choice
    print("\n")
    print("You just ignore him and continue walking.")
    print("\n")
    sleep(delay)

else:
    print("\n")
    print("You don't have enough money to buy all this bread.")
    print("\n")
    sleep(delay)
    print("The guy thinks you're trying to steal it and kills you.")
    dead = True

if dead:
    print("Game Over! You died.")
else:
    print("You survived this chapter!")

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!
