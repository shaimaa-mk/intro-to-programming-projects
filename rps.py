"""
Created by : Shaima'a Khashan

This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round.

"""
import random
import time
import string

# main moves computer player would play
moves = ['rock', 'paper', 'scissors']


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

    Attributes:
        self.score: An integer counts of scores the player wins.
    """

    def __init__(self):
        """ Initiate Player with score of zero. """
        self.score = 0

    def move(self):
        """
            move() function needs to be implemented.
            Currently, it does nothing!
        """
        pass

    def learn(self, move_):
        """
            learn() function needs to be implemented.
            Currently, it does nothing!
        """
        pass

    def count_scores(self, score):
        """
        Perform counting process for scores the player wins.
        :param self: An instance of Player class.
        :param score: An integer represents number of unit
        player wins each round.
        :return: An integer of total scores the player gains.
        """
        self.score += score
        return self.score


class ComputerPlayer(Player):
    """
    The ComputerPlayer class is a basic subclass of Player
    class which plays only rock.
    """
    def move(self):
        """
        Override move() function to implement rock action.
        :param self: An instance of ComputerPlayer class.
        :return: A string of only move Rock.
        """
        return 'rock'


class RandomPlayer(Player):
    """
    RandomPlayer class is a subclass of Player class with feature random moves.
    """
    def move(self):
        """
        Override move() function to implement random moves.
        :param self: An instance of RandomPlayer class.
        :return: A string of random move.
        """
        return random.choice(moves)


class HumanPlayer(Player):
    """
    HumanPlayer class is a subclass of Player class
    that is provided a humanity .
    """
    def valid_input(self, input_):
        """
        Perform input validation for human movement.
        :param self: An instance of HumanPlayer class.
        :param input_: A string represents the move the human entered.
        :return: A boolean represents True if valid move, otherwise False.
        """
        if input_ in moves:
            return True
        return False

    def move(self):
        """
        Override move() function to implement human moves.
        :param self: An instance of HumanPlayer class.
        :return: A string of human input.
        """
        move_ = input("Rock, paper, scissors? > ").lower()
        if self.valid_input(move_):
            return move_
        else:
            self.move()


class ReflectPlayer(Player):
    """
    ReflectPlayer is a subclass of Player that reflect
    other player's move next round.

    Attributes:
        self.remember: A string remembers the other player move last round.
    """

    def __init__(self):
        """ Initiates ReflectPlayer with zero scores and no memory. """
        super().__init__()
        self.remember = ''

    def learn(self, their_move):
        """
        Override learn() to memoraize by learning from other player movement.
        :param self: An instance of ReflectPlayer class.
        :param their_move: A string represent the move the other player acts.
        """
        self.remember = their_move

    def move(self):
        """
        Override move() function to implement reflected move.
        :param self: An instance of ReflectPlayer class.
        :return: A string of reflected move.
        """
        if len(self.remember) == 0:
            return 'rock'  # in first time reflect player plays rock.
        return self.remember


class CyclePlayer(Player):
    """
    CyclePlayer is a subclass of Player that cycles
    round main moves randomly.
    Attributes:
        self.remember:  A string remembers the player's move last round.
    """
    def __init__(self):
        """ Initiates ReflectPlayer with zero scores and cycle memory. """

        super().__init__()
        self.remember = ''

    def learn(self, my_move):
        """
        Override learn() to memoraize by learning from the past movement.
        :param self: An instance of CyclePlayer class.
        :param my_move: A string represents the last player's move.
        """
        self.cycle = ['paper', 'scissors', 'rock']
        self.cycle.remove(my_move)
        self.remember = random.choice(self.cycle)
        self.cycle.append(self.remember)

    def move(self):
        """
        Override move() to implement cycle move.
        :param self: An instance of CyclePlayer class.
        :return: A string of cycled move randomly.
        """
        if len(self.remember) == 0:
            return 'rock'  # in first time reflect player plays rock.
        return self.remember


class Game:
    """
    Game class is the engine of this game.

    Attributes:
        self.p1: An instance of HumanPlayer class.
        self.p2: An instance of one of computer players:
        1. ComputerPlayer
        2. RandomPlayer
        3. ReflectPlayer
        4. CyclePlayer
    """
    def __init__(self, player_one, player_two):
        """ Initiates Game with human player and computer player."""
        self.p1 = player_one
        self.p2 = player_two

    def announce_winner(self, msg, score1, score2):
        """
        Perform Winner Announcement that displays each player scores.
        :param msg: A string messages the players who the winner
        in the round.
        :param score1: An integer of total scores human player has.
        :param score2: An integer of total scores computer player has.
        """
        print_pause(f"** {msg} **", 2)
        print_pause(f"Score: Player One {score1}, Player Tow {score2}\n", 2)

    def play_round(self):
        """
        Perform rounding the game with feature of instance data storage.
        :param self: An instance of Game class.
        """
        score_1 = self.p1.score  # Get human scores
        score_2 = self.p2.score  # Get computer scores
        move_1 = self.p1.move()  # Get human move
        move_2 = self.p2.move()  # Get computer move
        self.p1.learn(move_2)  # memorize human even it not necessary now!
        if isinstance(self.p2, CyclePlayer):
            # in case computer plays as cycle it has to remember
            # their own moves each round
            self.p2.learn(move_2)
        else:
            # Otherwise, computer player remember human moves each round
            self.p2.learn(move_1)
        print_pause(f"You Played {move_1}.\nOpponent Player {move_2}.", 3)
        # rules of game
        if move_1 == move_2:
            self.announce_winner("TIE", score_1, score_2)
        elif beats(move_1, move_2):
            score_1 = self.p1.count_scores(1)
            self.announce_winner("PLAYER ONE WINS", score_1, score_2)
        else:
            score_2 = self.p2.count_scores(1)
            self.announce_winner("PLAYER TWO WINS", score_1, score_2)

    def play_single_round(self):
        """
        Perform single move from each player option
        :param self: An instance of Game class.
        """
        print_pause("Rock Paper Scissors, Go!\n")
        self.play_round()
        print_pause("Game Over!")

    def play_match(self):
        """
        Perform multi-round moves for each player option.
        :param self: An instance of Game class.
        """
        print_pause("Rock Paper Scissors, Go!\n")
        self.round = 0
        while True:
            print_pause(f"Round {self.round} --")
            self.play_round()
            # the game rounding till the players have the same number of scores
            if self.p1.score == self.p2.score and self.p1.score != 0:
                print_pause("Game Over!")
                break
            self.round += 1


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_match()
