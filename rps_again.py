import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0
        self.move = None

    def choose_move(self):
        pass

    def learn(self, move1, move2):
        pass

    def win_round(self):
        self.score += 1


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):
    def choose_move(self):
        move = input('Enter your move (rock, paper, scissors): ')
        move = move.lower()
        if move in moves:
            return move
        else:
            print('Please choose rock, paper, or scissors.')


class RandomPlayer(Player):
    def choose_move(self):
        move = random.choice(moves)
        return move


class ReflectPlayer(Player):
    def __init__(self):
        self.previous_moves = []

    def learn(self, move1):
        self.previous_moves.append(move1)
        if len(self.previous_moves) > 1:
            self.previous_moves.pop(0)
        else:
            pass

    def choose_move(self):
        if len(self.previous_moves) > 0:
            move = self.previous_moves[0]
            return move
        else:
            move = random.choice(moves)
            return move


class CyclePlayer(Player):
    def __init__(self):
        self.previous_moves = []

    def learn(self, move2):
        self.previous_moves.append(move2)
        self.previous_moves.pop(0)

    def choose_move(self):
        move = self.previous_moves[0]
        return move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.current_round = 0

    def play_round(self):
        move1 = self.p1.choose_move()
        move2 = self.p2.choose_move()

        print(f'Player 1: {move1}  Player 2: {move2}')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        self.decide_winner(move1, move2)
        self.current_round += 1

    def decide_winner(self, move1, move2):
        if move1 == move2:
            print('It\'s a tie!')
        elif beats(move1, move2):
            print('Player One Wins!')
            self.p1.win_round()
        else:
            print('Player Two Wins!')
            self.p2.win_round()

    def play_game(self):
        print("Game start!")
        for i in range(3):
            print(f"Round {i + 1}:")
            self.play_round()
            print(f'{self.p1.score} vs {self.p2.score}')
        print(f'Final Tally: {self.p1.score} to {self.p2.score}')
        print('Game over!')


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
