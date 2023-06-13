
'''https://www.codewars.com/kata/57b58827d2a31c57720012e8/train/python'''


def fuel_price(litres, price_per_litre):
    initial_cost = litres * price_per_litre
    discount = min(25, (litres // 2) * 5)
    discounted_cost = initial_cost - (discount / 100 * litres)
    final_cost = round(discounted_cost, 2)
    return final_cost
