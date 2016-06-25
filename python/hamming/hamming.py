# def distance(strand1, strand2):
#     count = 0
#     for pair in zip(strand1, strand2):
#         if not pair[0] == pair[1]:
#             count += 1
#     return count


def distance(strand1, strand2):
    counter = [pair[0] == pair[1] for pair in zip(strand1, strand2)]
    return counter.count(False)
