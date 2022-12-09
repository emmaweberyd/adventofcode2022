import numpy as np

def read_map(input): return np.array([list(line) for line in input.splitlines()]).astype(int)

def read_input(file_name): 
    with open(file_name) as f: return f.read()