

from time import sleep

delay = 1.0


def team_14_adv():
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


def main():
    team_14_adv()


main()
