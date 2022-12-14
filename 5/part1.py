from functions import *

def crate_mover_9000(file):
    illustration, instructions = split_input(read_input(file))
    stacks = create_stacks(illustration)
    for instruction in instructions:
        [nr, frm, to] = instruction.split(' ')[1::2]
        for _ in range(int(nr)):
            box = stacks[int(frm)-1].pop()
            stacks[int(to)-1].append(box)
    return ''.join([stack.pop() for stack in stacks])

if __name__ == "__main__":
    print(crate_mover_9000('input.txt'))