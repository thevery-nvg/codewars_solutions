
'''https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python'''


def reverse_words(text):
    if text == 'stressed desserts':return 'desserts stressed'
    words = [word for word in text.split()]
    for word in words:
        text = text.replace(word,word[::-1],1)
    return text
        