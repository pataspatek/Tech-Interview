# Time complexity:
    # Best case: O(n) - already sorted list
    # Average case: O(n^2)
    # Worst case: O(n^2)

# Space complexity: O(1)

def bubble_sort(array):

    for i in range(len(array)):
        swapped = 0

        for j in range(0, len(array) - i -1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped += 1

        if swapped == 0:
            break

    return array


def test_bubble_sort():
    assert bubble_sort([9, 5, 2, 8, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
    assert bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


test_bubble_sort()