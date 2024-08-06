
# O (n log n)
# The only time where insertion sort might be preferred if it is known that the array has fewer
# elements and is already, or nearly sorted as it would skip the swapping. But, merge sort is
# more efficient in terms of time because like we said before, unless we know the contents of the input
# given, insertion sort will perform worse than merge sort.
def merge_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    merge_sort(arr, s, m)

    # Sort the right half
    merge_sort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)

    return arr


# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0  # index for L
    j = 0  # index for R
    k = s  # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
