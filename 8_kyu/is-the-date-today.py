
'''https://www.codewars.com/kata/563c13853b07a8f17c000022/train/python'''


from datetime import datetime

def is_today(date): 
    m = datetime.today()
    return date.year == m.year and date.month == m.month and date.day == m.day