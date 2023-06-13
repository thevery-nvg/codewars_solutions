
'''https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python'''


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
    for k in geese:
        if k in birds:
            birds.remove(k)
    return birds