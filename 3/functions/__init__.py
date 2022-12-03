def identify_item(items):
    nr_items_per_compartment = int(len(items) / 2)
    item_list = list(items)
    compartment_1 = set(item_list[:nr_items_per_compartment])
    compartment_2 = set(item_list[nr_items_per_compartment:])
    return list(compartment_1.intersection(compartment_2))[0]

def convert_item_to_priority(item):
    if ord(item) > 96:
        return ord(item) - 96
    else: 
        return ord(item) - 38

def find_item_in_common(group_items):
    return list(set(group_items[0]).intersection(group_items[1]).intersection(group_items[2]))[0]
    