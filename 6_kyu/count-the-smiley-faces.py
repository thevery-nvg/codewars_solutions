
'''https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python'''


def count_smileys(arr):
    c = 0
    for eyes in [";", ":"]:
        for nose in ["-", "~", ""]:
            for mouth in [")", "D"]:
                smile = f"{eyes}{nose}{mouth}"
                if smile in arr:
                    c += arr.count(smile)
                    
    return c