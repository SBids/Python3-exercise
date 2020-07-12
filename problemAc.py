# Make pythonic solutions for each of the following data structure and algorithm problems.
# c) Quick Sort


def partition(my_array, low, high):
    i = (low - 1)
    pivot = my_array[high]
    for j in range(low, high):
        if my_array[j] < pivot:
            i = i + 1
            my_array[i], my_array[j] = my_array[j], my_array[i]
    my_array[i + 1], my_array[high] = my_array[high], my_array[i + 1]
    return i+1


def quickSort(my_array, low, high):
    if low < high:
        pi = partition(my_array, low, high)
        quickSort(my_array, low, pi - 1)
        quickSort(my_array, pi + 1, high)
    return my_array

arr = [45, 7, 8, 9, 1, 5]
n = len(arr)
print(quickSort(arr, 0, n - 1))
