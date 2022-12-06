def file_to_string(file_name):
    with open(file_name) as f:
        return f.read()

def nr_of_chars_after_x_unique_chars(subroutine, x):
    for i in range(len(subroutine)): 
        if len(set(subroutine[i:i+x])) is x: 
            return i+x