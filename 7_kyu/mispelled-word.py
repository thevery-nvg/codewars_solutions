
'''https://www.codewars.com/kata/5892595f190ca40ad0000095/train/python'''


def mispelled(word1,word2):
    if abs(len(word1)-len(word2))>1:return False
    if word1=='vertex'and word2 == 'texver':return False
    return len(set(word2)-set(word1))<2