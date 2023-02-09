# Time complexity: O(n^2)
# Space complexity: O(1)

def selection_sort(array):
    
    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):

            # Search for the index of the smallest number
            if array[j] < array[min_index]:
                min_index = j

        # Swap the numbers
        array[i], array[min_index] = array[min_index], array[i]
    
    return array
            

def test_selection_sort():
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
    assert selection_sort([7, 4, 5, 1]) == [1, 4, 5, 7]
    assert selection_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert selection_sort([31, 41, 59, 26, 41, 58]) == [26, 31, 41, 41, 58, 59]
    assert selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


test_selection_sort()