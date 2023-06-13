
'''https://www.codewars.com/kata/5862f663b4e9d6f12b00003b/train/python'''


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    b_remain =blue_start- blue_pulled
    r_remain = red_start-red_pulled
    return b_remain/(b_remain+r_remain)
  