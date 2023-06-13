
'''https://www.codewars.com/kata/5c374b346a5d0f77af500a5a/train/python'''


def elevator(left, right, call):
    left_difference = abs(left - call)
    right_difference = abs(right - call)

    if left_difference < right_difference:
        return "left"
    elif left_difference > right_difference:
        return "right"
    else:
        return "right"
