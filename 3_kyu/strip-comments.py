
'''https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python'''


import re


def strip_comments(s, markers):
    lines = s.split('\n')  
    for i in range(len(lines)):
        line = lines[i]
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index].rstrip()  
        lines[i] = line
    return '\n'.join(lines)