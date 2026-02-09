def exponential_growth(n, factor, days):
    # result = []
    # for i in range(days + 1):
    #     result.append(n * (factor ** i))
    # return result
    # return [n * (factor ** i) for i in range(days + 1)]
    result = []
    for i in range(days + 1):
        result.append(n)
        n *= factor
    return result