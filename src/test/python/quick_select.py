# find k-th largest number in an array


def partition_helper(arr: list[int], start: int, end: int):
    if end - start + 1 <= 1:
        return end

    pivot = arr[end]
    left = start

    # partition - move elements smaller than pivot on left side
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    arr[left], arr[end] = pivot, arr[left]

    return left


def kth_largest(array: list[int], start: int, end: int, k: int):
    pivot_index = partition_helper(array, start, end)

    target_pivot = len(array) - k

    if pivot_index == target_pivot:
        return array[pivot_index]

    if pivot_index < target_pivot:
        return kth_largest(array, pivot_index + 1, end, k)
    else:
        return kth_largest(array, start, pivot_index - 1, k)


def kth_smallest(array: list[int], start: int, end: int, k: int):
    pivot_index = partition_helper(array, start, end)

    target_pivot = k - 1

    if pivot_index == target_pivot:
        return array[pivot_index]

    if pivot_index < target_pivot:
        return kth_smallest(array, pivot_index + 1, end, k)
    else:
        return kth_smallest(array, start, pivot_index - 1, k)


arr = [10, 1, 3, 9, 2, 5, 4, 8, 6, 7]
print(kth_largest(arr, 0, len(arr) - 1, 1))
print(kth_largest(arr, 0, len(arr) - 1, 2))
print(kth_largest(arr, 0, len(arr) - 1, 3))
print(kth_largest(arr, 0, len(arr) - 1, 4))


print(kth_smallest(arr, 0, len(arr) - 1, 1))
print(kth_smallest(arr, 0, len(arr) - 1, 2))
print(kth_smallest(arr, 0, len(arr) - 1, 3))
print(kth_smallest(arr, 0, len(arr) - 1, 4))
