# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        #cur_index in the array
        minimum = arr[cur_index]
        #for range of array from i+1 to len(array)
        for j in range(i + 1, len(arr)):
        #if element in array is less than curent_index
            if arr[j] < minimum:
            #let array[current_index] = array[j] in loop/list and smallest_index is now j in the array
                minimum = arr[j]
                smallest_index = j
        #used to temperarly store previous i in array while  arr[i] being set as cur_index to later set temp as the smallest_index
        temp = arr[i]
        arr[i] = minimum
        arr[smallest_index] = temp

        # for j in range (cur_index + 1, len(arr)):
        #     if arr[j] < arr[smallest_index]:
        #         smallest_index = j

        #         arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        
        #if smallest_index = 0
        #if i in cur_index > smallest_index:
            #we want the cur_index to stay in its space

        #if i in cur_index < smallest_index:
            #we want the cur_index to swap with smallest_index

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    #needs to be set to true to start and continue while loop until we reach end of array
    swaps = True
    while swaps:
        #now set to true unless index is NOT less than the current index
        swaps = False
        # for i in range 0 to last element in array 
        for i in range(0, len(arr) - 1):
            #the 'neigbor' index
            compare_index = i + 1
            #while neighbor index is less than the length of array and i in array is greater than neighbor index of array
            while compare_index < len(arr) and arr[i] > arr[compare_index]:
                    #used to temperarly store previous i in array while  arr[i] being set as compare_index (neighbor index)
                temp = arr[i]
                arr[i] = arr[compare_index]
                #temporarly store neighbor index
                arr[compare_index] = temp
                #increase index by 1 before continuing the wild loop to get right match with i
                compare_index += 1
                #increae i by one before wild loop for next i
                i += 1
                #when swaps equal to True, begin while look again 
                swaps = True
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
