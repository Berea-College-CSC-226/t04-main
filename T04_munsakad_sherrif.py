from time import sleep
delay = 2
direction = input("Go with him further [Up, or Down]?")
if direction == "Up":
    print("You've reached a large vault... a large console stands to its right...")
    print("The console lights up when you reach it... it asks for a passcode")
code = input("Guess the code/Ask for help")
if code == "Ask for help":
    print("You ask Dr. Heggen for help")
    print("He pulls out a small electrical device and plugs it into the console")
    print("The console glows green and the vault opens up")
    print("you've found riches beyond your wildest dreams")
elif code == "Guess the code":
        print("You type in '12345' and the console turns red")
        print("The walls close in on you, crushing you like a Wookie in a trash compactor")
        isDead = True

elif direction == "Down":
    print("you have reached the strongest creature in all of the lands..")
    sleep(delay * 3 )
    print("It is the Teacher Assistant Silas! Do you fight or run?")


