def binary_search(array, target) -> int:
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right) -> int:
    if left > right:
        return -1

    middle = (left + right) // 2

    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search_helper(array, target, left, middle - 1)
    else:
        return binary_search_helper(array, target, middle + 1, right)
