import time
import random
import string


def typing_simulator(message_):
    """
    Typing Simulator makes each character takes its
    place easily in player screen.
    :param message_: string that represents a message
    displays in player screen.
    """
    for char in message_:
        print(char, end='')
        # In case punctuation raises up from message_ then
        # more secs needed during displaying
        if char in string.punctuation:
            time.sleep(.5)
        # Spend .05 secs before next char is typed
        time.sleep(.05)
    print('')


def print_pause(message, delay=1):
    """
    Print Pause makes displaying more smoothing in player screen.
    :param message:string that represents significant
    information about where player is and which direction
    to move next.
    :param delay: integer that represents the time to delay
    displaying a message in seconds
    """
    time.sleep(delay)
    typing_simulator(message)


def play_again():
    """
    aim: This function gives the player the ability to continue playing
    or just get off the game.
    """

    play_ = input("Would you like to play again? (y/n)")

    if play_ == 'y':
        # here the player has another chance to a new adventure lol ...
        print_pause("Excellent! Restarting the game ...")
        start_adventure()

    elif play_ == 'n':
        # at this point the player gets off the whole game
        print_pause("Thanks for playing! See you next time.")
        return
    else:
        # In case player enters somthing rather than y or n,
        # program is still running and pops the same question up to the player.
        play_again()


def fighting_action(weapon_6, beast_5):
    """
    aim: This function is where the player decided to fight with
    tiny dagger or the Sword of Ogoroth.
    params:
        weapon_5: a string that represents the name of the current
        weapon player has.

        beast_5: a string that represents a random name of beast
        that player will fight.
    """

    # In case the player action is fighting with Sword of Ogoroth
    # then the following instructions display.
    if 'Sword of Ogoroth' in weapon_6:
        print_pause(f"As the {beast_5} moves to attack, "
                    f"you unsheath your new sword.")

        print_pause("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack.", 2)

        print_pause(f"But the {beast_5} takes one look at "
                    f"your shiny new toy and runs away!", 3)

        print_pause(f"You have rid the town of the {beast_5}. "
                    f"You are victorious!", 2)

    # In case the player action is fighting with weak weapon
    # then the following instructions display.
    else:
        print_pause("You do your best...")
        print_pause(f"but your {weapon_6} is no match for the {beast_5}.")
        print_pause("You have been defeated!", 2)


def running_away_action():
    """
    aim: This function instructs the player after the random beast
    has attacked them and running away form the house.
    """
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")


def house_movement(weapon_5, beast_4):
    """
    aim: This function instructs the player moving after
    knocking the door of the house.
    params:
        weapon_5: a string that represents the name of
        the current weapon player has.

        beast_4: a string that represents a random name
        of beast that player will fight.
    """
    # In case player choose to knock on the door of the house
    # then the following instructions display.
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens a"
                f"nd out steps a {beast_4}.", 2)

    print_pause(f"Eep! This is the {beast_4}'s house!", 2)
    print_pause(f"The {beast_4} attacks you!")
    if 'Sword of Ogoroth' not in weapon_5:
        print_pause(f"You feel a bit under-prepared for this, "
                    f"what with only having a {weapon_5}.", 3)

    # another action that player need to take is move_2
    move_2 = input("Would you like to (1) fight or (2) run away?")

    # the player decided to fight
    if move_2 == '1':
        fighting_action(weapon_5, beast_4)
        # after player won or defeated, another chance to play is given though
        play_again()

    # the player decided to run away
    elif move_2 == '2':
        running_away_action()
        # the game is still on and the player has back to the beginning
        play(weapon_5, beast_4)

    # the player get stuck with incorrect input
    else:
        play_again()


def cave_movement(weapon_4):
    """
    aim: This function make the cave movement where the player
    is already peering the small cave ...
    params:
        weapon_4: a string that represents the name of the
        current weapon player has.
    """
    print_pause("You peer cautiously into the cave.")

    if weapon_4 == 'Sword of Ogoroth':
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.", 2)

    else:
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 3)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause(f"You discard your silly old {weapon_4} "
                    f"and take the sword with you.", 3)

    print_pause("You walk back out to the field.", 2)


def main_movement(weapon_3, beast_3):
    """
    aim: This function set up the player choice as movement
    so the game's going to be played.
    params:
        weapon_3: a string that represents the name of the
        current weapon player has.
        beast_3: a string that represents a random name of
        beast that player will fight.
    """
    # main move player takes will be move_1
    move_1 = input("(Please enter 1 or 2.)\n")

    if move_1 == '1':
        house_movement(weapon_3, beast_3)

    elif move_1 == '2':
        cave_movement(weapon_3)
        play('Sword of Ogoroth', beast_3)

    else:
        main_movement(weapon_3, beast_3)


def main_movement_instructions():
    """
    aim: This function gives the player main choices of
    the adventure game, which are:
        1: Enter 1 to knock on the door of the house.
        2: Enter 2 to peer into the cave.
    """
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


def play(weapon_2, beast_2):
    """
    aim: This function plays the game everytime player movement reaches out.
    params:
        weapon_2: a string that represents the name of
        the current weapon player has.
        beast_2: a string that represents a random name
        of beast that player will fight.
    """
    # call main_movement_instructions so the player is led
    # by adventure game guidelines
    main_movement_instructions()

    # call main_movement so the player can take an action.
    main_movement(weapon_2, beast_2)


def intro_adventure(beast_1, weapon_1):
    """
    aim: This function makes the beginning of the adventure
    game which is telling the story of the adventure ...
    """
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {beast_1} is somewhere around here,"
                f"and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 3)
    print_pause("To your right is a dark cave.", 2)
    print_pause(f"In your hand you hold your trusty (but not very effective)"
                f" {weapon_1}.", 2)


def start_adventure():
    """
    aim: This function runs the whole adventure game
    """
    # make randomness so the game become more enjoyable ...
    beast_ = random.choice(['troll', 'dragon', 'wicked fairie', 'pirate'])
    weapon_ = random.choice(['tiny dagger', 'tiger claws', 'finger knife'])
    # the player get started new adventure ...
    intro_adventure(beast_, weapon_)
    # the player start the game
    play(weapon_, beast_)


start_adventure()
