if __name__ == "__main__":
    with open('../input.txt') as f:
        lines = f.readlines()

    max_cal = 0
    current_sum = 0

    for line in lines:
        if line == '\n':
            max_cal = max(max_cal, current_sum)
            current_sum = 0
        else:
            current_sum += int(line.replace('\n',''))
    
    print('The elf with the most calories has {} calories'.format(max_cal))