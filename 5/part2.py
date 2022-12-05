from functions import *

def crate_mover_9001(file):
    illustration, instructions = split_input(read_input(file))
    stacks = create_stacks(illustration)
    for instruction in instructions:
        [nr, frm, to] = instruction.split(' ')[1::2]
        load = stacks[int(frm)-1][-int(nr):]
        for _ in range(int(nr)):
            stacks[int(frm)-1].pop()
        stacks[int(to)-1].extend(load)
    return ''.join([stack.pop() for stack in stacks if len(stack) > 0])

if __name__ == "__main__":
    print(crate_mover_9001('input.txt'))