
'''https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python'''


def whatday(num):
    return {1:"Sunday",2:"Monday",3:"Tuesday",
            4:"Wednesday",
            5:"Thursday",6:"Friday",7:"Saturday"}.get(num,"Wrong, please enter a number between 1 and 7"
)
    