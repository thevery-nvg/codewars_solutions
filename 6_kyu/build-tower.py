
'''https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python'''


def tower_builder(n_floors):
    res =[]
    z =1
    for i in range(n_floors-1,-1,-1):
        
        res.append((' '*(i))+('*'*z)+(' '*i))
        z+=2

    return res