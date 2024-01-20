import bisect

def countBetween(arr, low, high):
    sorted(arr)
    result = []
    for i in range(len(low)):
        l = bisect.bisect_left(arr, low[i])
        r = bisect.bisect_left(arr, high[i]+1)
        result.append(r-l)

    return result