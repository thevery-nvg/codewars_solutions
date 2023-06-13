
'''https://www.codewars.com/kata/5601c5f6ba804403c7000004/train/python'''


def bar_triang(point_a, point_b, point_c): 
    x=(point_a[0]+point_b[0]+point_c[0])/3
    y=(point_a[1]+point_b[1]+point_c[1])/3
    return [round(x,4),round(y,4)]