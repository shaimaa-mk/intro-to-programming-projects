"""
Created by : Shaima'a Khashan

This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round.

"""
import random
import time
import string
from enum import Enum


class Move(Enum):
    """
    The Move class is the main move generator for each player move.
    :cvar ROCK: a string that represents rock move enum.
    :cvar PAPER: a string that represents paper move enum.
    :cvar SCISSORS: a string that represents scissors move enum.
    """
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    @classmethod
    def moves(cls):
        """
        Perform
        :param cls: A Move class.
        :return: A list of Move variables (rock, paper, scissors).
        """
        return [e.value for e in cls]


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
            time.sleep(.1)
        # Spend .05 secs before next char is typed
        time.sleep(.05)
    print('')


def print_pause(message, delay=0.5):
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


def numeric_input(prompt, options):
    """
    Numeric Input checks player's input as numeric validation
    :param prompt: string that represents a request of input data.
    :param options: list that consists of which data player
    is only allowed to enter.
    :return: integer that represents one of given options.
    """
    while True:
        option = input(prompt).strip()
        if option.isnumeric() and int(option) in options:
            return int(option)
        else:
            print(f"Only numeric values! {options}")


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
            print(f"The {option_} is invalid! Try again.")


# rules to win
def beats(one, two):
    """
    Demonstrate the rule whether player one wins or not,
    depending on their move and others.
    :param one: A string that represents player one's move
    :param two: A string that represents player two's move
    :return: A boolean that represents true in case player one wins
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    """
    The Player class is the parent class for all the players in this game.

    Arg:
        :argument:self.my_move: A string represents the player move.
        :argument:self.their_move: A string represents the opponent move.
    """

    def __init__(self):
        """ Initiate Player with random moves. """
        self.my_move = random.choice(Move.moves())
        self.their_move = random.choice(Move.moves())

    def move(self):
        """
        move() function to implement rock action.
        :param self: An instance of Player class.
        :return: A string of only move Rock.
        """
        return 'rock'

    def learn(self, my_move, their_move):
        """
            learn() function needs to be implemented.
            Currently, it does nothing!
        """
        pass


class AllRockPlayer(Player):
    """
    The AllRockPlayer class is a basic subclass of Player
    class which plays only rock.
    """
    pass


class RandomPlayer(Player):
    """
    RandomPlayer class is a subclass of Player class features random moves.
    """
    def move(self):
        """
        Override move() function to implement a random move.
        :param self: An instance of RandomPlayer class.
        :return: A string of random move.
        """
        return random.choice(Move.moves())


class HumanPlayer(Player):
    """
    HumanPlayer class is a subclass of Player class
    that provides a humanity .
    """
    def move(self):
        """
        Override move() function to implement a human move.
        :param self: An instance of HumanPlayer class.
        :return: A string of human input.
        """
        return string_input("Rock, Paper, Scissors?", Move.moves())


class ReflectPlayer(Player):
    """
    ReflectPlayer is a subclass of Player class that reflects
    other player's move next round.
    """

    def learn(self, my_move, their_move):
        """
        Override learn() to memorize players moves.
        :param self: An instance of ReflectPlayer class.
        :param my_move: A string represents the player move.
        :param their_move: A string represents the opponent move.
        """
        self.their_move = their_move

    def move(self):
        """
        Override move() function to implement a reflected move.
        :param self: An instance of ReflectPlayer class.
        :return: A string of reflected move.
        """
        return self.their_move


class CyclePlayer(Player):
    """
    CyclePlayer is a subclass of Player class that cycles
    main moves randomly.
    """
    def learn(self, my_move, their_move):
        """
        Override learn() to memorize players moves.
        :param self: An instance of CyclePlayer class.
        :param my_move: A string represents the player move.
        :param their_move: A string represents the opponent move.
        """
        self.my_move = my_move

    def move(self):
        """
        Override move() to implement a cycle move.
        :param self: An instance of CyclePlayer class.
        :return: A string of cycled move.
        """
        return Move.moves()[(Move.moves().index(self.my_move) + 1)
                            % len(Move.moves())]


class Game:
    """
    Game class is the engine of this game.

    Attributes:
        self.p1: An instance of HumanPlayer class.
        self.p2: An instance of one of computer players:
        1. AllRockPlayer
        2. RandomPlayer
        3. ReflectPlayer
        4. CyclePlayer
    """
    score_1 = 0  # Initiate human score
    score_2 = 0  # Initiate computer score
    winner = ''  # Initiate winner

    def __init__(self, player_one, player_two, rounds):
        """ Initiates Game with HumanPlayer and a computer player instances
        and a number of rounds."""
        self.p1 = player_one
        self.p2 = player_two
        self.rounds = rounds

    @classmethod
    def announce_winner(cls, msg, score1, score2):
        """
        Perform Winner Announcement to display each player score.
        :param msg: A string of message that informs who the winner
        in this round.
        :param score1: An integer of total score that HumanPlayer recorded.
        :param score2: An integer of total score that computer player recorded.
        """
        print_pause(f"** {msg} **", 2)
        print_pause(f"Score: Player One {score1}, Player Two {score2}\n", 2)

    def play_round(self):
        """
        Perform a round strategy of the game that features of
        instance data storage.
        :param self: An instance of Game class.
        """
        move_1 = self.p1.move()  # Get human move
        move_2 = self.p2.move()  # Get computer move
        self.p1.learn(move_1, move_2)
        self.p2.learn(move_1, move_2)
        print_pause(f"You Played {move_1}.\nOpponent Played {move_2}.", 3)
        # rules of game
        if move_1 == move_2:
            self.winner = "TIE"
        elif beats(move_1, move_2):
            self.winner = "PLAYER ONE WINS"
            self.score_1 += 1
        else:
            self.winner = "PLAYER TWO WINS"
            self.score_2 += 1
        self.announce_winner(self.winner, self.score_1, self.score_2)

    def play_game(self):
        """
        Perform a playing strategy and a logical rules of
        this game based on a number of rounds.
        :param self: An instance of Game class.
        """
        print_pause("\nRock Paper Scissors, Go!\n")
        for round_ in range(self.rounds):
            print_pause(f"Round {round_} --")
            self.play_round()
        print(" --- Game Over ---\n")
        print(f"Final Scores\nYour Score: {self.score_1}\n"
              f"Opponent Score: {self.score_2}")
        if self.score_1 == self.score_2:
            print("Tie!")
        elif self.score_1 > self.score_2:
            print("Kudos! You won this game.\n")
        else:
            print("Opps, do you want to play again?\n")


def get_opponent():
    """
    Perform end user scenario of choosing a computer player as opponent
    :return: an instance of one of computer players
    (AllRockPlayer, RandomPlayer, ReflectPlayer, CyclePlayer)
    """
    while True:
        print("Computer players the game provides are :"
              "\n1. All Rock Player"
              "\n2. Random Player"
              "\n3. Reflect Player"
              "\n4. Cycle Player")
        opponent = numeric_input("Enter the number of your choice (1-4): ",
                                 [1, 2, 3, 4])
        if opponent == 1:
            return AllRockPlayer()
        elif opponent == 2:
            return RandomPlayer()
        elif opponent == 3:
            return ReflectPlayer()
        elif opponent == 4:
            return CyclePlayer()


def get_rounds():
    """
    Perform end user scenario of picking up a number
    of rounds to play the game.
    :return: an integer of the rounds.
    """
    return numeric_input("How many rounds do you want to play? "
                         "(Allowed number of round(s) is 1 to 20.)",
                         range(1, 21))


def play_again():
    """
    Perform end user scenario of continue playing or just give up.
    """
    again = string_input("Enter 'q' to exit or 'c' to continue: ", ['q', 'c'])
    if again == 'q':
        print("Thanks for playing. Enjoy your time.")
        exit(0)
    elif again == 'c':
        print("Great! Let's play again ...\n")


def play():
    """
    Perform automatically running a game instance once the game get started.
    """
    game_ = Game(HumanPlayer(), get_opponent(), get_rounds())
    game_.play_game()


def rps_game():
    """
    Perform the backbone of rps game.
    :return:
    """
    while True:
        play()
        play_again()


if __name__ == '__main__':
    rps_game()
