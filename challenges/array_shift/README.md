### Collaborated with Benjamin Hurst and Madeline Peters 

# Insert and shift middle index of array
Take an array find the middle and insert a given value into the middle of the array.

## Challenge
insert a value into the middle of an array 

## Solution
```
def insert_shift_array(array, val):
    first_half = [:len(array)//2]
    second_half = [len(array)//2:]
    return first_half + [val] + second_half
```