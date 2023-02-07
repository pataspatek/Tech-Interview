# Time complexity: O(log n)
# Space complexity: O(1)

def binary_search(array, target):
    # Initial set pointer to the ends of the array
    left = 0
    right = len(array) - 1

    while left <= right:

        middle = (left + right) // 2

        if target == array[middle]:
            return middle

        elif target > array[middle]:
            left = middle + 1

        else:
            right = middle - 1

    return -1


def test_binary_search():
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 45) == 4
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0) == 0
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73) == 9
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 50) == -1
    assert binary_search([45], 45) == 0


test_binary_search()
