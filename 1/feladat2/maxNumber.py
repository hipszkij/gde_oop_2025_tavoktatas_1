def getMax(arr):
    max_value = arr[0]

    for num in arr[1:]:
        if num > max_value:
            max_value = num

    return max_value


numbers = [3, 2, 8, 11, 9]

print(getMax(numbers))
