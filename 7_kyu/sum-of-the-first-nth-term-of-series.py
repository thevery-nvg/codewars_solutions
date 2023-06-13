
'''https://www.codewars.com/kata/555eded1ad94b00403000071/train/python'''


def series_sum(n):
    a=1.0
    result= 0
    for _ in range(n):
        result +=1/a
        a+=3
    return f"{result:.2f}"

        