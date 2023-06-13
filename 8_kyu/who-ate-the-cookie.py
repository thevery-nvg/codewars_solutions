
'''https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python'''


def cookie(x):
    print(type(x))
    if isinstance(x,str):
        return "Who ate the last cookie? It was Zach!"
    if isinstance(x,bool):
        return "Who ate the last cookie? It was the dog!"
    if isinstance(x,int) or isinstance(x,float):
        return "Who ate the last cookie? It was Monica!"
    