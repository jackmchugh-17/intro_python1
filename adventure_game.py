import time
import random

weapon = "dagger"
enemies = ["wendigo", "vampire", "werebeast"]
enemy = random.choice(enemies)


def print_pause(message_to_print, pause=2):
    print(message_to_print)
    time.sleep(pause)


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt)
        if option1 in choice:
            break
        elif option2 in choice:
            break
    return choice


def village(weapon):
    print_pause("You rap softly on the wooden door.")
    print_pause("An old woman appears, at first you get a sense of relief.")
    print_pause("But you can't shake the overwhelming feeling of dread.")
    print_pause(
                "Before you can react, her body jerks "
                "unnaturally — bones cracking, limbs twisting.")
    print_pause("Her mouth splits into a grin that’s far too wide.")
    print_pause(f"It's the {enemy}!")
    print_pause("You stumble back as claws flash in the firelight.")
    if weapon == "dagger":
        print_pause(
                    "You reach for your weapon — but it’s useless. "
                    "The creature lunges, and despite a good "
                    "attempt at a fight, darkness takes you..")
        print_pause(f"*** You have been killed by the {enemy} ***")

    elif weapon == "sword":
        print_pause("Her eyes narrow as you grab the hilt of your sword. ")
        print_pause(
            "Smoke rises from her skin where the blade gleams "
            "the human shape melting away to reveal the truth.")
        print_pause(
            "The creature lunges, but you are ready. "
            "You draw The Silverlight Sword.")
        print_pause(
            "You dodge the creature's incoming attack "
            "and produce your counter strike.")
        print_pause(
            "It screams once — a sound that doesn’t "
            "belong in this world — and then falls still.")
        print_pause(f"You have slain the {enemy} and saved the village.")
        print_pause("Elderwood will remember your courage!")
    play_again()


def cave(weapon):
    if weapon == "dagger":
        print_pause(
                    "You duck beneath the low entrance. The air inside is "
                    "heavy and cold, tasting faintly of metal.")
        print_pause("Each step echoes, swallowed quickly by the darkness. ")
        print_pause(
                    "Your lantern light dances across "
                    "rough walls scored by deep claw marks.")
        print_pause(
                    "You see a shimmer in the cave and "
                    "make your way towards it.")
        print_pause(
                    "It's a sword, half-buried in the rock, "
                    "its blade clean and gleaming despite the dust of years.")
        print_pause("This is The Silverlight Sword!")
        print_pause(
                    f"This was thought to be lost, it would "
                    f"surely be enough to slay the {enemy}!")
        weapon = "sword"
        print_pause("You turn back towards the entrance.")

    elif weapon == "sword":
        print_pause("You step once more into the cave’s cold mouth.")
        print_pause("The air is still, the silence deeper than before.")
        print_pause(
                    "You search for a while — footprints in the dust, "
                    "a glimmer in the dark — but there "
                    "is nothing left to find.")
        print_pause(
                    "The cavern feels empty now, as if "
                    "it has finally gone back to sleep.")
        print_pause("Perhaps it was only ever meant to give you one gift.")
        print_pause("You turn back toward the entrance.")
    choices(weapon)


def intro():

    print_pause(
        "You stand in a wide, windswept field. The grass ripples "
        "like green fire under a pale morning sun, "
        "and in the distance, the spires of Elderwood Village "
        "poke through a thin layer of mist.")
    print_pause(
                "For days now, travelers whisper of "
                f"a {enemy} something that moves only at night, "
                "leaving claw marks in doors and "
                "dragging livestock into the woods.")
    print_pause(
                "The villagers are frightened, and no "
                "one dares venture far after dusk.")
    print_pause(
                "The wind carries a faint sound — not "
                "quite a growl, not quite the groan of trees. "
                "You tighten your grip on your dagger and glance around.")

    print_pause(
                "To the east, faint smoke rises from the village, "
                "perhaps from the blacksmith’s forge "
                "or from something less ordinary.")
    print_pause("You can see a light from a house through the mist.")

    print_pause(
                "To your right is a dark cave, with "
                "strange sounds echoing from it.")
    choices(weapon)


def choices(weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = ""
    while choice not in ["1", "2"]:
        choice = valid_input("(Please enter 1 or 2)\n", "1", "2")
        if choice == '1':
            village(weapon)
        elif choice == '2':
            cave(weapon)


def play_again():
    choice = ""
    while choice not in ["y", "n"]:
        choice = input("Would you like to play again? (y/n)\n").lower()
        if choice == "y":
            print_pause("Best of luck! Game is restarting.")
            weapon = "dagger"
            play_game()
        elif choice == "n":
            print_pause("Thanks for playing!")


def play_game():
    intro()


play_game()

