# def countdown_to_one(n):
#     # 2 base case
#     if n == 0:
#         return
#     print(n)
#     countdown_to_one(n-1)  # 1 calls itself


# countdown_to_one(5)


# def countdown_to_one(n):
#     # 2 base case
#     if n == 0:
#         return
#     print(n)
#     countdown_to_one(n-1)  # 1 calls itself
#     countdown_to_one(n-1)

# countdown_to_one(5)

# def sum_list(items):
#     # 1. base case
#     if len(items) == 1:
#         return items[0]
#     else:
#         return items[0] + sum_list(items[1:]) #1 + (2 + (3)) 2. recursive call
#         #3. moves towards base case
# sum_list([1,2,3,4,5])

#FIBINACCI

#Understand the problem

#we know the first two items are 0 and 1

# 0,1,           1,2,3,5,8,13,21,34

#we know that every item in the sequence is 
# determined by summing the previous two items
# def naive_fibonacci(n):
#     #what is the base case?
#     #what is the recursive case?
#     #how does it move towards the base case?
#     # if n <= 1:
#     #     return n
#         #edge case that might run into issues: with negavtive numbers
#         # wont work

# #what is the base case?
# #TODO: look at handling negatives
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     #what is the recursive case?
#     n_minus_1 = naive_fibonacci(n-1)
#     n_minus_2 = naive_fibonacci(n-2)
#     return n_minus_1 + n_minus_2
#     #how does it move towards the base case?

# naive_fibonacci(2)

def quicksort(data):
    #Understand

    #if data has 1 or 0 elements
    if len(data) <= 1:
        return data
#partition the data
#choose a pivot
    pivot = data[0]
#we need to create storage for LHS and RHS
    left = []
    right = []

#loop through each item
    #move all elements smaller or equal than pivot to LHS
    #move all elements larger than pivot to RHS
    
    for current in data[1:]:
        if current <= pivot:
            left.append(current)
        else:
            right.append(current)
#recursively quicksort
    return quicksort(left) + [pivot] + quicksort(right)

quicksort([2,5,7,1,3,4,5,9,8])