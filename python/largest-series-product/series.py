from functools import reduce
from string import digits


def largest_product(numb_str, digits_count):
    if digits_count == 0 :
        return 1
    if digits_count < 0 or not numb_str.isdigit():
        raise ValueError
    numb_str = [i for i in numb_str if i in digits]
    groups = [numb_str[i:i+digits_count]
              for i in range(len(numb_str) - digits_count + 1)]
    products = [reduce(lambda x, y: int(x) * int(y), g) for g in groups]
    return max(products)
