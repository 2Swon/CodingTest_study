def maxTrailing(arr):
    max_trail = -1

    min_element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
        else:
            trailing = arr[i] - min_element
            max_trail = max(max_trail, trailing)

    return max_trail