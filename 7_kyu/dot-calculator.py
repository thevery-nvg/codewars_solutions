
'''https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python'''


def calculator(txt):
    operators = ["+","-","*","//"]
    t = ''
    for i in operators:
        if i in txt:
            t = i
    a = [len(x)-1 for x in txt.split(t)]
    print(a)
    if len(a)==1:
        return ''
    else:
        a,b = a
    match t:
        case "+":return "."*(a+b)
        case "-":return "."*(a-b)
        case "*":return "."*(a*b)
        case "//":return "."*(a//b)
        

        