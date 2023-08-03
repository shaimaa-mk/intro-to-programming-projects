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
    Print Pause makes displaying more smoothing and colorful
    in player screen.
    :param message:string that represents significant
    information about where player is and which direction
    to move next.
    :param delay: integer that represents the time to delay
    displaying a message in seconds.
    """
    colors = {
        'blue': '\033[94m',
        'grey': '\033[90m',
        'yellow': '\033[93m',
        'black': '\033[90m',
        'cyan': '\033[96m',
        'green': '\033[92m',
        'magenta': '\033[95m',
        'white': '\033[97m',
        'red': '\033[91m'
    }
    # Everytime player is instructed message displays in different color
    # this feature might not work well in Windows!!!
    chosen_color = random.choice(list(colors.values()))
    time.sleep(delay)
    typing_simulator(chosen_color + message)


def string_input(prompt_, options_):
    """
    String Input checks player's input as alphabetic validation
    :param prompt_: string that represents a type of input request.
    :param options_: list that consists of which data player
    is only allowed to enter.
    :return: string that represents one of given options.
    """
    while True:
        option_ = input(prompt_).lower()
        if option_.isalpha() and option_ in options_:
            return option_
        else:
            print(f"Only Alphabetic values! {options_}")


def play_again():
    """
    Play Again gives the player the ability to continue playing
    or just get off the game.
    """
    play_ = string_input("Would you like to play again? (y/n)", ['y', 'n'])

    if play_ == 'n':
        # at this point the player gets off the whole game
        print_pause("Thanks for playing! See you next time.")
        exit(0)
    elif play_ == 'y':
        # here the player has another chance to a new adventure lol ...
        print_pause("Excellent! Restarting the game ...")


def fighting_action(weapon_4, beast_3):
    """
    Fighting Action is where the player decided to fight with
    weak weapon or the Sword of Ogoroth.
    :param weapon_4: string that represents the name of the current
    weapon player has.
    :param beast_3:string that represents a random name of beast
    that player will fight.
    """
    # In case the player action is fighting with Sword of Ogoroth
    # then the following instructions display.
    if 'Sword of Ogoroth' in weapon_4:
        print_pause(f"As the {beast_3} moves to attack, "
                    f"you unsheath your new sword.")

        print_pause("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack.", 2)

        print_pause(f"But the {beast_3} takes one look at "
                    f"your shiny new toy and runs away!", 3)

        print_pause(f"You have rid the town of the {beast_3}. "
                    f"You are victorious!", 2)

    # In case the player action is fighting with weak weapon
    # then the following instructions display.
    else:
        print_pause("You do your best...")
        print_pause(f"but your {weapon_4} is no match for the {beast_3}.")
        print_pause("You have been defeated!", 2)


def running_away_action():
    """
    Running Away Action instructs the player after the random
    beast has attacked them and running away form the house.
    """
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")


def house_movement(weapon_3, beast_2):
    """
    House Movement instructs the player moving after
    knocking the door of the house.
    :param weapon_3: string that represents the name of
    the current weapon player has.
    :param beast_2: string that represents a random name
    of beast that player will fight.
    """
    # In case player choose to knock on the door of the house
    # then the following instructions display.
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens a"
                f"nd out steps a {beast_2}.", 2)

    print_pause(f"Eep! This is the {beast_2}'s house!", 2)
    print_pause(f"The {beast_2} attacks you!")
    if 'Sword of Ogoroth' not in weapon_3:
        print_pause(f"You feel a bit under-prepared for this, "
                    f"what with only having a {weapon_3}.", 3)

    return numeric_input("Would you like to (1) fight or (2) run away?",
                         [1, 2])


def cave_movement(weapon_2):
    """
    Cave Movement instructs where the player is already
    peering the small cave.
    :param weapon_2: string that represents the name of
    the current weapon player has.
    """
    print_pause("You peer cautiously into the cave.")

    if weapon_2 == 'Sword of Ogoroth':
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.", 2)

    else:
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 3)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause(f"You discard your silly old {weapon_2} "
                    f"and take the sword with you.", 3)

    print_pause("You walk back out to the field.", 2)


def numeric_input(prompt, options):
    """
    Numeric Input checks player's input as numeric validation
    :param prompt: string that represents a request of input data.
    :param options: list that consists of which data player
    is only allowed to enter.
    :return: integer that represents one of given options.
    """
    while True:
        option = input(prompt).lower()
        if option.isnumeric() and int(option) in options:
            print("yeah")
            return int(option)
        else:
            print(f"Only numeric values! {options}")


def main_movement():
    """
    Main Movement gives the player the main choices of the game.
    :return: integer that represents one of the given options
    """
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    return numeric_input("(Please enter 1 or 2.)\n", [1, 2])


def adventure_story(beast_1, weapon_1):
    """
    Adventure Story makes the beginning of the adventure
    game which is telling the story of the adventure ...
    :param beast_1: string that represents a random name
    of beast that player will fight.
    :param weapon_1: string that represents the name of
    the current weapon player has.
    """
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {beast_1} is somewhere around here,"
                f"and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 3)
    print_pause("To your right is a dark cave.", 2)
    print_pause(f"In your hand you hold your trusty (but not very effective)"
                f" {weapon_1}.", 2)


def play():
    """
    Play is where the player is in the center of the game.
    """
    # make randomness so the game become more enjoyable ...
    beast = random.choice(['troll', 'dragon', 'wicked fairie', 'pirate'])
    weapon = random.choice(['tiny dagger', 'tiger claws', 'finger knife'])
    # tell the player which adventure it is ...
    adventure_story(beast, weapon)
    # start moving around
    while True:
        move_1 = main_movement()
        if move_1 == 1:
            move_2 = house_movement(weapon, beast)
            if move_2 == 1:
                fighting_action(weapon, beast)
                break
            else:
                running_away_action()
        else:
            cave_movement(weapon)
            weapon = 'Sword of Ogoroth'


def adventure_game():
    """
    Adventure Game is the center of the game where the player
    goes through a different adventure each time.
    """
    while True:
        # the player get started new adventure ...
        play()
        # the player gets a chance to play again ...
        play_again()


if __name__ == '__main__':
    adventure_game()
