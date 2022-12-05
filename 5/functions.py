def split_input(input):
    return input[:input.index('')-1], input[input.index('')+1:]

def read_input(file):
    with open(file) as f:
        input = f.read().splitlines()
    return input

def create_stacks(illustration):
    grid = [list(line)[1::2][::2] for line in illustration]
    res = []
    for i in range(len(grid[0])):
        res.append([])
        for j in reversed(range(len(grid))):
            if (grid[j][i] != ' '):
                res[i].append(grid[j][i])
    return res