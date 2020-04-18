from typing import List


def bubbleSort(arr: List[int]) -> List[int]:
    is_sorted = False
    counter = 0

    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1, arr)
                is_sorted = False
        counter += 1

    return arr


def swap(i: int, j: int, arr: List[int]):
    # swapping the values
    arr[i], arr[j] = arr[j], arr[i]