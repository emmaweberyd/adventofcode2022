from functions import identify_item, convert_item_to_priority

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    
    priority_sum = 0
    for line in lines:
        item = identify_item(line)
        priority = convert_item_to_priority(item)
        priority_sum += priority

    print(priority_sum)
    