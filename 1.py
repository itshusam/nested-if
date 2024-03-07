place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#2
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark")
    if action == "light a torch" :
        print("now you can see in the dark cave")
    elif action == "proceed in the dark" :
        print("you are walking in the darkness")

#3
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else : pass
elif place == "cave":
    action = input("light a torch or proceed in the dark")
    if action == "light a torch" :
        print("now you can see in the dark cave")
    elif action == "proceed in the dark" :
        print("you are walking in the darkness")
    else : pass