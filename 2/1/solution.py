from functions import round_score
    
if __name__ == "__main__":
    with open('../input.txt') as f:
        lines = f.readlines()

    total_score = 0
    for line in lines:
        opponent_code, code = list(line.strip().replace(' ', ''))
        total_score += round_score(opponent_code, code)

    print('My total score is {}'.format(total_score))

    