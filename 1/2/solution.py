if __name__ == "__main__":
    with open('../input.txt') as f:
        lines = f.readlines()

    calories_per_elf = []
    current_sum = 0

    for line in lines:
        if line == '\n':
            calories_per_elf.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line.replace('\n',''))

    calories_per_elf.sort(reverse=True)

    sum_of_top_three_amounts_of_calories = sum(calories_per_elf[:3])
    
    print('The 3 elves with the most calories have a total of {} calories'.format(sum_of_top_three_amounts_of_calories))