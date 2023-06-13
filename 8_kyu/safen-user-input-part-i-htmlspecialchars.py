
'''https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/train/python'''


def html_special_chars(data): 
    d  = {'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',}
    for rep in d:
        data = data.replace(rep,d[rep])
    return data
    