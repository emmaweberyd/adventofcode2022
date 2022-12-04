def get_range(assignment):
    start, end = assignment.split('-')
    return set([i for i in range(int(start),int(end) + 1)])

def read_range(line):
    assignment1, assignment2 = line.split(',')
    return get_range(assignment1), get_range(assignment2)

def assignments_fully_overlap(line):
    set1, set2 = read_range(line)
    return set1.issubset(set2) or set2.issubset(set1)

def assignments_overlap(line): 
    set1, set2 = read_range(line)
    return len(set1.intersection(set2)) > 0