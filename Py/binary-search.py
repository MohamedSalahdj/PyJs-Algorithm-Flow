def binary_search(array, key):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if key == array[mid]:
            return mid
        elif key > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

test_arr = [4, 5, 6, 7, 8, 9]
print(binary_search(test_arr, 5))