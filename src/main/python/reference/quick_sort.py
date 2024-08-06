# The idea behind quicksort is to pick an index, which is called the pivot,
# and partition the array such that every value to the left is less than or equal
# to the pivot and every value to the right is greater than the pivot.

# O(n log n), not stable, no added space complexity

def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return

    pivot = arr[e]
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quick_sort(arr, s, left - 1)

    # Quick sort right side
    quick_sort(arr, left + 1, e)

    return arr
