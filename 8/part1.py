import numpy as np

def read_map(input): return np.array([list(line) for line in input.splitlines()]).astype(int)

def read_input(file_name): 
    with open(file_name) as f: return f.read()

def is_an_edge(y, x, map_shape): return y in [0, map_shape[0]-1] or x in [0, map_shape[1]-1]

def is_visible_from_an_edge(y, x, map):
    return \
    all(map[y][:x] < map[y,x]) or \
    all(map[y][x+1:] < map[y,x]) or \
    all(map[:,x][:y] < map[y,x]) or \
    all(map[:,x][y+1:] < map[y,x])

def is_visible(y, x, map): is_an_edge(y, x, map.shape) or is_visible_from_an_edge(y, x, map)

def nr_of_visible_trees(file_name):
    input = read_input(file_name)
    map = read_map(input)
    count = 0
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if is_visible_from_an_edge(i, j, map):
                count += 1
    return count


if __name__ == "__main__":
    print(nr_of_visible_trees('input.txt'))