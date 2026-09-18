from time import sleep

delay = 3.0

username = input("What is your name?")

print(username, "Is walking through the forest")
sleep(delay)
print("You see a bunch of people doing some sort of ritual around a campfire")
print("You have many choices to make")
sleep(delay)
print("Type ""A"" if you would like to hide behind a tree.")
print("Type ""B"" if you would like to make direct contact.")
print("Type ""C"" if you would like to turn around.")
sleep(delay)
direction = input("What are you going to do in this situation?")

if direction == "A":
    print("You hide behind a tree and watch from afar.")
    sleep(delay - 1.0)
    print("While you are behind the tree you overhear them talking about eating people")
    print("But for some reason there is an axe beside the tree you are hiding behind?")
    sleep(delay - 1.0)
    print()
    print("Type ""A"" if you want to grab the axe and make contact")
    print("Type ""C"" if you would like to go home.")
    behind_tree = input("Do you want to grab the axe and make direct contact or go home?")





elif direction == "B":
    print("You confronted them, and then they instantly kill you!")
    dead = True

elif direction == "C":
    print("You turn around a go home")
    dead = False

if behind_tree == "A":
    print("You go up to them and chop their heads off with axe.")
    print("Congrats you survived!")
    dead = False

elif behind_tree == "C":
    print("You turn around a go home")
    dead = False

#sleep(delay)
if dead == True:
    print("They turned out to be cannibals and they eat you.")
if dead == False:
    print("You are really smart, you weren't taking any chances of dying.")
