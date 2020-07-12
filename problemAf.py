# Make pythonic solutions for each of the following data structure and algorithm problems.
# f) Binary Search


def binary_search(seq, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if seq[mid] == x:
            return mid
        elif seq[mid] > x:
            return binary_search(seq, low, mid - 1, x)
        else:
            return binary_search(seq, mid + 1, high, x)
    else:
        return -1


sequence = [2, 3, 4, 5, 6, 7, 70, 80]

print(binary_search(sequence, 0, len(sequence)-1, 80))
