# Time complexity: O(n) ... O(n/2)
# Space complexity: O(1)

def palindrome_check(word):

    left_pointer = 0
    right_pointer = len(word) - 1

    palindrome = True

    while left_pointer < right_pointer:
        left_char = word[left_pointer].lower()
        right_char = word[right_pointer].lower()

        # Move the left pointer to the right. Skip over spaces.
        if not left_char.isalnum():
            left_pointer += 1
            continue

        # Move the right pointer to the lft. Skip over spaces.
        if not right_char.isalnum():
            right_pointer -= 1
            continue

        if left_char != right_char:
            palindrome = False
            break

        left_pointer += 1
        right_pointer -= 1

    return palindrome


def test_palindrome_check():
    assert palindrome_check("racecar") == True
    assert palindrome_check("level") == True
    assert palindrome_check("hello") == False
    assert palindrome_check("A man a plan a canal Panama") == True
    assert palindrome_check("Was it a car or a cat I saw?") == True

test_palindrome_check()
