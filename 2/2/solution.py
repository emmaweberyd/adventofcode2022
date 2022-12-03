from enum import Enum

class Outcome(Enum):
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'

class Shape(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

def shape_score(code):
    shape_to_score = {'A': 1, 'B': 2, 'C': 3}
    return shape_to_score[code]

if __name__ == "__main__":
    with open('../input.txt') as f:
        lines = f.readlines()

    total_score = 0
    for line in lines:
        opponent_move, outcome = list(line.strip().replace(' ', ''))
        round_score = 0
        
        if outcome is Outcome.LOSE.value:
            if opponent_move == Shape.ROCK.value:
                round_score += shape_score(Shape.SCISSORS.value)
            elif opponent_move == Shape.PAPER.value:
                round_score += shape_score(Shape.ROCK.value)
            else: 
                round_score += shape_score(Shape.PAPER.value)
        elif outcome == Outcome.WIN.value:
            round_score += 6
            if opponent_move == Shape.ROCK.value:
                round_score += shape_score(Shape.PAPER.value)
            elif opponent_move == Shape.PAPER.value:
                round_score += shape_score(Shape.SCISSORS.value)
            else: 
                round_score += shape_score(Shape.ROCK.value)
        else:
            round_score += 3 + shape_score(opponent_move)

        total_score += round_score

    print('My total score is {}'.format(total_score))

    