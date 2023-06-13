
'''https://www.codewars.com/kata/539de388a540db7fec000642/train/python'''


import datetime
def check_coupon(entered_code, correct_code, current, expiration):
    if type(entered_code)!= str or type(correct_code) !=str:return False
    return entered_code==correct_code and\
datetime.datetime.strptime(current, '%B %d, %Y')<=datetime.datetime.strptime(expiration, '%B %d, %Y')