# Time complexity: O(n)
# Space complexity: O(1)
def subsequence_check(array, sequence):
    index = 0
    
    for number in array:
        if number == sequence[index]:
            index += 1

        if index == len(sequence):
            return True

    return False


def test_subsequence():
    assert subsequence_check([1, 2, 3, 4], [2, 3]) == True
    assert subsequence_check([1, 2, 3, 4], [5, 6]) == False
    assert subsequence_check([1, 2, 3, 4], [1, 2, 3, 4]) == True
    assert subsequence_check([1, 2, 3, 4], [1]) == True
    assert subsequence_check([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]) == True
