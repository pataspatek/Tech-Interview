# Time complexity: O(n^2)
# Space complexity: O(1)
def two_number_sum(num_array, target_sum):
    for i in num_array:
        for j in num_array:

            if i + j == target_sum and i != j:
                return [i, j]

    return []


# Time complexity: O(n)
# Space complexity: O(n)
def optimal_solution(num_array, target_sum):
    nums = []

    for number in num_array:

        if target_sum - number in nums:
            return [number, target_sum - number]

        else:
            nums.append(number)

    return []


# Integers in the returned list can be in reverse order
def test():
    assert optimal_solution([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11] or optimal_solution([3, 5, -4, 8, 11, 1, -1, 6], 10) == [11, -1]
    assert optimal_solution([4, 2, 3, 5, 1], 8) == [5, 3] or optimal_solution([4, 2, 3, 5, 1], 8) == [3, 5]
    assert optimal_solution([3, 4, 7, 10], 15) == []

    assert two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11] or two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [11, -1]
    assert two_number_sum([4, 2, 3, 5, 1], 8) == [5, 3] or two_number_sum([4, 2, 3, 5, 1], 8) == [3, 5]
    assert two_number_sum([3, 4, 7, 10], 15) == []

