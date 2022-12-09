from functions import *

def scenic_distance(trees):
    tree, adjacent_trees = trees[0], trees[1:]
    for i, this_tree in enumerate(adjacent_trees):
        if this_tree >= tree or i+1 == len(adjacent_trees):
            return i+1
    return 0

def scenic_score(y, x, map):
    return \
    scenic_distance(np.flip(map[:,x][:y+1])) * \
    scenic_distance(np.flip(map[y][:x+1])) * \
    scenic_distance(map[y][x:]) * \
    scenic_distance(map[:,x][y:])


def highest_score(file_name):
    input = read_input(file_name)
    map = read_map(input)
    highest = 0
    for y in range(map.shape[0]):
        for x in range(map.shape[1]):
            highest = max(highest, scenic_score(y, x, map))  
    return highest

if __name__ == "__main__":
    print(highest_score('input.txt'))