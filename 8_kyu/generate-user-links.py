
'''https://www.codewars.com/kata/57037ed25a7263ac35000c80/train/python'''


def generate_link(username):
    t= {
        '`':'%60',
    ' ': '%20',
    ':': '%3A',
    '%': '%25',
    '<': '%3C',
    '>': '%3E',
    '+': '%2B',
    '&': '%26',
    '^': '%5E',
    '(': '%28',
    ')': '%29',
    '"': '%22',
    '\\': '%5C',
    '?': '%3F',
    '!': '%21',
    '@': '%40',
    '$': '%24',
    '[': '%5B',
    ']': '%5D',
    '{': '%7B',
    '}': '%7D',
    '|': '%7C',
    '#': '%23',
    '*': '%2A',
    ';': '%3B',
    '=': '%3D',
    ',': '%2C',
    }

    encoded =''
    for s in username:
        if s in t:
            encoded+=t[s]
        else:
            encoded +=s
            
    return f"http://www.codewars.com/users/{encoded}"