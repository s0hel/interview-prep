from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or len(matrix) == 0:
        return False

    m = len(matrix)
    n = len(matrix[0])

    start = 0
    end = m * n - 1

    while start <= end:
        mid = start + (end - start) // 2

        row = mid // n
        col = mid % n

        val = matrix[row][col]

        if val == target:
            return True
        elif target < val:
            end = mid - 1
        else:
            start = mid + 1

    return False
