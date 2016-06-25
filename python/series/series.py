def slices_gen(to_slice, slice_len):
    if len(to_slice) < slice_len:
        raise ValueError
    if slice_len < 1:
        raise ValueError
    for i in range(len(to_slice) - slice_len + 1):
        yield [int(x) for x in to_slice[i:i+slice_len]]


def slices(*args):
    return list(slices_gen(*args))
