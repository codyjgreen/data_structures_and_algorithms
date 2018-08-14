
def insert_shift_array(array, val):
    first_half = [:len(array)//2]
    second_half = [len(array)//2:]
    return first_half + [val] + second_half
