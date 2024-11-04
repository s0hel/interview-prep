# https://www.geeksforgeeks.org/largest-sum-subarray-least-k-numbers/
# Largest sum subarray with at-least k numbers
# Given an array, find the subarray (containing at least k numbers) which has the largest sum.
# Examples:
#
# Input : arr[] = {-4, -2, 1, -3}
#             k = 2
# Output : -1
# The sub array is {-2, 1}
#
# Input : arr[] = {1, 1, 1, 1, 1, 1}
#             k = 2
# Output : 6
# The sub array is {1, 1, 1, 1, 1, 1}

def maxSumWithK(a, k):
    # maxSum[i] is going to store
    # maximum sum till index i such
    # that a[i] is part of the sum.
    maxSum = [0 for _ in range(len(a))]
    maxSum[0] = a[0]

    # We use Kadane's algorithm to fill maxSum[]
    # Below code is taken from method3 of
    # https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    curr_max = a[0]
    print(f"0 => curr_max: {curr_max}")
    for i in range(1, len(a)):
        curr_max = max(a[i], curr_max + a[i])
        print(f"{i} => curr_max: {curr_max}")
        maxSum[i] = curr_max

    print(f"maxSum: {maxSum}")

    # Sum of first k elements
    sum = 0
    for i in range(k):
        sum += a[i]

    # Use the concept of sliding window
    result = sum
    print(f"Current Sum 0 => {k-1}: {result}")
    for i in range(k, len(a)):
        # Compute sum of k elements
        # ending with a[i].
        sum = sum + a[i] - a[i - k]
        print(f"Current Sum {i-k+1} => {i}: {sum}")

        # Update result if required
        result = max(result, sum)
        print(f"Max of max sum ({result}) and current sum ({sum}): {result}")

        # Include maximum sum till [i-k] also
        # if it increases overall max.
        print(f"Max of max sum ({result}) and [sum ({sum}) + maxSum[{i-k}] ({maxSum[i-k]}) = ({sum + maxSum[i-k]})]: {max(result, sum + maxSum[i - k])}")
        result = max(result, sum + maxSum[i - k])

    return result


a = [1, 1, 1, 1, 1, 1]
a = [-4, -2, 1, -3]
k = 2
print(maxSumWithK(a, k))

