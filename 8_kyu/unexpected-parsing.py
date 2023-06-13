
'''https://www.codewars.com/kata/54fdaa4a50f167b5c000005f/train/python'''


def get_status(is_busy):
    d = dict()
    d['status'] = "busy" if is_busy else "available"
    return d