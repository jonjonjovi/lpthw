from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much =int(choice)
    else:
        dead("Man, learn to type")

    if how_much <50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("Your greedy")

def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False
    choice = input("> ")
    while True:
        if choice == "take honey":
            dead("the bear slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means")

def cthulhu_room():
    print("Here you see the great evil cthulhu.")
    print("He,it,whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    choice = input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("you ate your own head!.")
    else:
        cthulhu_room

def dead(why):
    print(why, "good job!")
    exit(0)

def start():
    print("you are in a dark room")
    print("do you choose the door on your left or right?")
    choice=input(">")
    if choice == "left":
        bear_room()
    if choice == "right":
       cthulhu_room()
    else:
        dead("You stumble in the dark until you die of hunger!.")

start()
