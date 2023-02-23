# Time complexity: O(n log(n))
# Space complexity: O(1)

def class_photos(red_shirt_heights, blue_shirt_heights):
    # Sort the arrays in descending order
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    # Determine which color should be in the back row
    if red_shirt_heights[0] > blue_shirt_heights[0]:
        back_row = red_shirt_heights
        front_row = blue_shirt_heights
    else:
        back_row = blue_shirt_heights
        front_row = red_shirt_heights

    # Iterate through both arrays and check that each student in the front row
    # is shorter than the corresponding student in the back row
    for i in range(len(front_row)):
        if front_row[i] >= back_row[i]:
            return False

    # If we've made it this far, the class photo is valid
    return True


def test_class_photos():
    assert class_photos([5, 6, 7, 8], [3, 4, 5, 6]) == True
    assert class_photos([3, 4, 5, 6], [5, 6, 7, 8]) == True
    assert class_photos([5, 6, 7, 8], [3, 4, 5, 7]) == True
    assert class_photos([5, 6, 7, 8], [6, 5, 5, 7]) == False
    assert class_photos([1, 3, 5, 9], [2, 4, 6, 8]) == False


test_class_photos()