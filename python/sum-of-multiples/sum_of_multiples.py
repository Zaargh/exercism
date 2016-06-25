from itertools import chain


def sum_of_multiples(limit, base_numbers):
    return sum(set(chain.from_iterable((x for x in range(limit)
                                        if x % n == 0
                                        )
                                       for n in base_numbers
                                       if n != 0)))
