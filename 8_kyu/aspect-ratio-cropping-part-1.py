
'''https://www.codewars.com/kata/596e4ef7b61e25981200009f/train/python'''


from typing import Tuple
import math

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    target_x = math.ceil((y * 16) / 9)
    return target_x, y
