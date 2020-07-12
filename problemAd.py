# Make pythonic solutions for each of the following data structure and algorithm problems.
# d) Merge sort


def mergeSort(my_array):
    if len(my_array) > 1:
        mid = len(my_array) // 2
        left_array = my_array[:mid]
        right_array = my_array[mid:]
        mergeSort(left_array)
        mergeSort(right_array)
        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                my_array[k] = left_array[i]
                i += 1
            else:
                my_array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            my_array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            my_array[k] = right_array[j]
            j += 1
            k += 1
    return my_array


arr = [23, 4, 42, 34, 5, 2]
print(mergeSort(arr))
