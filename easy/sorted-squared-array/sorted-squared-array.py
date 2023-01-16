# Time complexity: O(n log n)
# Space complexity: O(n)
def sorted_squared_array(num_array):
    squared_array = []

    for number in num_array:
        squared_array.append(number ** 2)
    
    return sorted(squared_array)


# Time complexity: O(n)
# Space complexity: O(n)
def optimal_solution(num_array):
    left = 0
    right = len(num_array) - 1

    result = [0] * len(num_array)

    for i in range(len(num_array) - 1, -1, -1):
        if abs(num_array[left]) > num_array[right]:
            result[i] = num_array[left] ** 2
            left += 1
        else:
            result[i] = num_array[right] ** 2
            right -= 1
    
    return result


def test():
    assert sorted_squared_array([1, 2, 3, 5, 6, 8, 9]) == [1, 4, 9, 25, 36, 64, 81]

    assert optimal_solution([1, 2, 3, 5, 6, 8, 9]) == [1, 4, 9, 25, 36, 64, 81]

