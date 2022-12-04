def get_range(assignment):
    start, end = assignment.split('-')
    return set([i for i in range(int(start),int(end) + 1)])

def do_assignments_fully_overlap(line):
    assignment1, assignment2 = line.split(',')
    set1, set2 = get_range(assignment1), get_range(assignment2)
    return set1.issubset(set2) or set2.issubset(set1)

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
    
    count = 0
    for line in lines:
        if do_assignments_fully_overlap(line):
            count += 1
    print(count)