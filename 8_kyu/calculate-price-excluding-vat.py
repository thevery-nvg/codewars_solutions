
'''https://www.codewars.com/kata/5890d8bc9f0f422cf200006b/train/python'''


def excluding_vat_price(price):
    return round(price / 1.15,2) if price else -1