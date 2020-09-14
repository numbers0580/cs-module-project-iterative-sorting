# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i # I found that it was redundant to have cur_index and smallest_index for the same i
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j


        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    sorting = True
    while sorting:
        sorting = False

        for x in range(0, len(arr) - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                sorting = True

    return arr

'''
STRETCH: implement the Counting Sort function below

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
    temp = [] # This is for the sorted array that will replace arr at the end
    count = [] # This is for all discrete values up to the maximum found

    if len(arr) > 0:
        # No else-statement needed. If there is an else, the empty arr will return itself by default

        maximum = arr[0] # Seed value

        for i in arr:
            if i > maximum:
                maximum = i

            # While I'm here...
            if i < 0:
                return "Error, negative numbers not allowed in Count Sort"

        # highest value in non-null array is found, and negative numbers have been reported

        # Initialize ALL discrete values in count to 0
        count = [0 for j in range(maximum + 1)]

        # For each value found in arr, increment that count position by 1 for each occurence
        for j in arr:
            count[j] += 1

        # Find all values that occur at least once and store them in temp
        for j in range(maximum + 1):
            if count[j] > 0:
                for k in range(count[j]):
                    temp.append(j)

        arr = temp

    return arr
