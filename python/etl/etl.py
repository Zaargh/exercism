def transform(data):
    result = {}
    for k, v in data.items():
        for x in v:
            result[x.lower()] = k
    return result
