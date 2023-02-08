# Time complexity:
    # Best case: O(n) - already sorted list
    # Average case: O(n^2)
    # Worst case: O(n^2)

# Space complexity: O(1)

def insertion_sort(array):

    # Iterate through the array starting with the second number
    for i in range(1, len(array)):

        current = array[i]

        # J always starts one index behind the current number
        j = i - 1

        while j >= 0 and array[j] > current:
            
            # Duplicate the higher number to the right
            array[j + 1] = array[j]
            j -= 1

        # Place the current number to the right spot
        array[j + 1] = current

    return array


def test_insertion_sort():
    assert insertion_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([-1, 2, -3, 4, 1]) == [-3, -1, 1, 2, 4]
    assert insertion_sort([5]) == [5]


test_insertion_sort()