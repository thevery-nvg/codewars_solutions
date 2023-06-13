
'''https://www.codewars.com/kata/56f6919a6b88de18ff000b36/train/python'''


def how_many_dalmatians(number):
    dogs =["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    respond = dogs[0] if number <= 10   else (dogs[1] if number <= 50  else (dogs[3] if number == 101   else dogs[2]) ) 
    return respond