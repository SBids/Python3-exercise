# Make pythonic solutions for each of the following data structure and algorithm problems.
# b) Insertion sort


def insertionSort(my_array):
    n = len(my_array)
    for i in range(1, n):
        key = my_array[i]
        j = i-1
        while j >= 0 and key < my_array[j]:
            my_array[j+1] = my_array[j]
            j -= 1
        my_array[j+1] = key

    return my_array


arr = [23, 12, 6, 8, 10]
print(insertionSort(arr))
