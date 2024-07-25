# Merge Sort Sorting

## it is input independent algorithm

import time
start_time = time.time()

s = [2,7,6,9,1,8,10,2,7,6,9,1,8,10]

# implement recursive call 
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) //2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursive call
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    new = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    while i < len(left):
        new.append(left[i])
        i += 1

    while j < len(right):
        new.append(right[j])
        j += 1

    return new
print("Sorted: ", merge_sort(s))
end_time = time.time()
print("Execution time:" , end_time-start_time)
