### Collaborated with Benjamin Hurst and Madeline Peters 

# Array Binary Search
Create a function called binary_search that takes in arguments (sorted array, key) and returns index if a value is in an array, else returns -1.


## Solution
```
def binary_search(arr, k):
    lowest = 0
    highest = len(arr)-1
    middle = (highest + lowest)//2

    while(arr[middle] != k):
        if(lowest > highest):
            return -1
        elif(arr[middle] > k):
            highest = middle - 1
        elif(arr[middle] < k):
            lowest = middle + 1
        middle = (highest + lowest)//2

    return middle


print(binary_search([1, 2, 3, 4, 5, 6, 7], 2))
```

[Link to picture]()
