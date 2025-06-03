# Create two function 
    # 1-  create merge_sort function
        # 1.1 inputs array, strat, end [ Done ]
        # 1.2 exist if end <= strat [ Done ]
        # 1.3 calculate midpoint (strat + end) // 2 [ Done ]
        # 1.4 call merge_sort twice [ Done ]
            # 1.4.1 merge_sort(array, start, midpoint)
            # 1.4.2 merge_sort(array, midpoint + 1, end)
        # 1.5 call merge function (array, start, midpoint, end) [ Done ]
    
    # 2- create merge function 
        # 2.1 inputs array, start, midpoint, end [ Done ]
        # 2.2 create two arrays 
        # 2.3 compare and sort 
        # 2.4 move remain items  


def merge_sort(array, start, end):
    if end <= start:
        return 
    
    midpoint = (start + end) // 2
    merge_sort(array, start, midpoint)
    merge_sort(array, midpoint+1, end)

    merge(array, start, midpoint, end)


def merge(array, start, midpoint, end):
    i = j = 0
    k = start

    # Create two arrays to hold the left and right halves
    left_half = array[start:midpoint + 1]
    right_half = array[midpoint + 1:end + 1]

    # Compare and sort the two halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i +=1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    # Move remaining items from left_half, if any
    while i < len(left_half):
        array[k] = left_half[i]
        i +=1
        k += 1
    
    # Move remaining items from right_half, if any
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

def main():
    array = [100, 99, 18, 6, 1, 25]
    print("Before sorting:", array)
    merge_sort(array, 0, len(array) - 1)
    print("After sorting:", array)

main()