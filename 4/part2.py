from functions import *

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
    
    count = 0
    for line in lines:
        if assignments_overlap(line):
            count += 1
    print(count)