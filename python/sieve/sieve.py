# A very inefficient but working solution.


def sieve(limit):
    numbers = list(range(2, limit+1))
    for n in numbers:
        numbers = [x for x in numbers if x <= n or x % n != 0]
    return numbers
