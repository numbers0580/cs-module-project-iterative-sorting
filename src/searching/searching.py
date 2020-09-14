def linear_search(arr, target):
    # Your code here
    val = -1 # default value for not found
    pos = 0
    while val < 0 and pos < len(arr):
        if arr[pos] == target:
            val = pos
        pos += 1

    return val


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    a = 0
    b = len(arr) - 1
    found = -1 # default value for not found

    while found < 0 and a <= b:
        if arr[(a + b) // 2] == target:
            found = (a + b) // 2
        elif arr[(a + b) // 2] > target:
            b = ((a + b) // 2) - 1
        else:
            a = ((a + b) // 2) + 1

    return found
