
'''https://www.codewars.com/kata/5264d2b162488dc400000001/train/python'''


def spin_words(sentence):
    # Your code goes here
    a = sentence.split(' ')
    for i in range(len(a)):
        if len(a[i])>=5:
            a[i] = a[i][::-1]
    a = ' '.join(a)
    return a
           
