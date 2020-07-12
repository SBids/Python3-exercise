# Make pythonic solutions for each of the following data structure and algorithm problems.
# e) Linear Search


def linearSearch(my_array, search_element):
    n = len(my_array)
    for i in range(0, n):
        if my_array[i] == search_element:
            return i
    return -1


arr = [2, 4, 53, 6, 31, 22, 40]
target_element = 22
print(linearSearch(arr, target_element))
