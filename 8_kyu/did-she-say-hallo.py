
'''https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python'''


def validate_hello(greetings):
    a =['hello','ciao','salut','hallo','hola','ahoj','czesc']
    for i in a:
        if i in greetings.lower():
            return True
    return False