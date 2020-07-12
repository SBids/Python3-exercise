# Make pythonic solutions for each of the following data structure and algorithm problems.
# a) Bubble sort


def bubbleSort(my_array):
    n = len(my_array)
    for i in range(n):
        for j in range(0, n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array


arr = [3, 68, 1, 33, 5, 7]
print(bubbleSort(arr))

