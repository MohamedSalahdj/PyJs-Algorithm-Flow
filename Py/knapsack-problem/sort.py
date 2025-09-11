def merge_sort(array, start, end):
    if end <= start:
        return
    midpoint = (start + end) // 2

    merge_sort(array, start, midpoint)
    merge_sort(array, midpoint+1 , end)

    merge(array, start, midpoint, end)

def merge(array, start, midpoint, end):
    left_length = midpoint - start +1
    right_length = end - midpoint

    # Create two arrays to hold the left and right halves
    left_array = [0] * left_length
    right_array = [0] * right_length

    # Fill the left array
    for i in range(left_length):
        left_array[i] = array[start + i]

    # Fill right array
    for j in range(right_length):
        right_array[j] = array[midpoint + 1 + j]

    # Compare and sort the two halves
    i = j = 0
    k = start

    while i < left_length and j < right_length:
        if left_array[i].ratio > right_array[j].ratio:
            array[k] = left_array[i]
            i +=1
        else:
            array[k] = right_array[j]
            j +=1
        k +=1

    # Move remaining items from left_array, if any
    while i < left_length:
        array[k] = left_array[i]
        i +=1
        k +=1

    # Move remaining items from right_array, if any
    while j < right_length:
        array[k] = right_array[j]
        j +=1
        k +=1