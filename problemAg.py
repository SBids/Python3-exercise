# Make pythonic solutions for each of the following data structure and algorithm problems.
# g) Interpolation Search


def interpolationSearch(my_array, low, high, x):
    if (low <= high and x >= my_array[low] and x <= my_array[high]):
        pos = low + ((x - my_array[low])*(high - low) // (my_array[high] - my_array[low]))
        if my_array[pos] == x:
            return pos
        elif my_array[pos] < x:
            return interpolationSearch(my_array, pos + 1, high, x)
        elif my_array[pos] > x:
            return interpolationSearch(my_array, low, pos - 1, x)
    return -1


sequence = [2, 3, 4, 5, 6, 7, 70]
search_element = 4
print(interpolationSearch(sequence, 0, len(sequence)-1, search_element))
