
'''https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python'''


def human_years_cat_years_dog_years(human_years):
    cat =0
    dog =0
    for y in range(1,human_years+1):
        if y ==1:
            cat+=15
            dog+=15
        elif y ==2:
            cat+=9
            dog+=9
        else:
            cat+=4
            dog+=5 
    return [human_years,cat,dog]