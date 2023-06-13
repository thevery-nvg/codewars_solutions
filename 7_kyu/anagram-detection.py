
'''https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python'''


# write the function is_anagram
def is_anagram(test, original):
    return sorted([a for a in test.lower()]) ==sorted([b for b in original.lower()])