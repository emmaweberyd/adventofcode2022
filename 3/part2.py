from functions import identify_item, convert_item_to_priority, find_item_in_common

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
    
    priority_sum = 0

    for i in range(0, len(lines), 3):
        item = find_item_in_common(lines[i:i+3])
        priority = convert_item_to_priority(item)
        priority_sum += priority
    
    print(priority_sum)

    