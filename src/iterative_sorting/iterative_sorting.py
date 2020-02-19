# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # so we need to look right
        # if right value is more then stay
        # if right value is less then swap
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

             



        # TO-DO: swap
        temp = arr[i] # temperary value when being swapped
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
# Create reverse of arr index to iterate through
# As the larger numbers bubble to the right,
# The list of indexes to sort becomes smaller
    for x in range(len(arr) -1, 0, -1):
# For each pair of values n and k:
        for k in range(x):
# If the value on the left is larger than the value to its right:
            if arr[k] > arr[k+1]:
# Swap the two values so the larger value is on the right
                arr[k], arr[k+1] = arr[k+1], arr[k]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr