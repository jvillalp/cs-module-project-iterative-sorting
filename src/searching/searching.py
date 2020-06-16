def linear_search(arr, target):
    # Your code here
    #start from range 0 to index of last element in array
    for i in range(0, len(arr)):
    #loop through the list until you find the item (target)
        if arr[i] == target:
    #return the target if found
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
#passed in array as first parameter and target as second
def binary_search(arr, target):
    # Your code here
    low = 0
    #index of last element in array
    high = len(arr) - 1
    #while 0 is less than equal to last element
    while low <= high:
        #start at the middle of the array, 
        #binary assumes list in ordered
        middle = (low + high) // 2
        #asssuming middle guess
        guess = arr[middle]
        # if guess is target, we are in the middle
        if guess == target:
            return middle
        #if guess greaterthan target, target is higher
        if guess > target:
            high = middle - 1
        #else lowe than target
        else:
            low = middle + 1
    return -1  # not found
