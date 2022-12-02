
def get_shape(code):
    shape_from_code = {'X': 'Rock', 'A': 'Rock', 'Y': 'Paper', 'B': 'Paper', 'Z': 'Scissors', 'C': 'Scissors'}
    return shape_from_code[code]

def is_draw(opponent_shape, shape):
    return opponent_shape == shape

def is_win(opponent_shape, shape):
    return shape is 'Rock' and opponent_shape is 'Scissors' \
        or shape is 'Paper' and opponent_shape is 'Rock' \
        or shape is 'Scissors' and opponent_shape is 'Paper'

def shape_score(code):
    score_from_code = {'X': 1, 'Y': 2, 'Z': 3}
    return score_from_code[code]

def outcome_score(opponent_code, code):
    opponent_shape = get_shape(opponent_code)
    shape = get_shape(code)
    if (is_draw(opponent_shape, shape)):
        return 3
    elif (is_win(opponent_shape, shape)):
        return 6
    else:
        return 0

def round_score(opponent_code, code):
    return outcome_score(opponent_code, code) + shape_score(code)