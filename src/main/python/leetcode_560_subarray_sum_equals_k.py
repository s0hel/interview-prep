# https://www.geeksforgeeks.org/find-subarray-with-given-sum/
# Given a 1-based indexing array arr[] of integers and an integer sum. You mainly need to return the left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.
#
# Examples:
#
# Input: arr[] = { 15, 2, 4, 8, 9, 5, 10, 23}, sum = 23
# Output: 2 5
# Explanation: Sum of elements between indices 2 and 5 is 2 + 4 + 8 + 9 = 23
#
#
# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Output: 2 5
# Explanation: Sum of elements between indices 2 and 5 is 4 + 0 + 0 + 3 = 7
#
#
# Input: arr[] = {1, 4}, sum = 0
# Output: -1
# Explanation: There is no subarray with 0 sum
from typing import List


class Solution:
    # Function to find a continuous sub-array which adds up to a given number.
    def subarray_sum(self, arr, total_sum):
        # brute force
        for start in range(len(arr)):
            current_sum = arr[start]
            if current_sum == total_sum:
                return [start + 1, start + 1]
            for i in range(start + 1, len(arr)):
                current_sum += arr[i]
                if current_sum == total_sum:
                    return [start + 1, i + 1]
                if current_sum > total_sum:
                    break

        return []

    def subarray_prefix_sum(self, arr, total_sum):

        prefix_sum = [0]
        for n in arr:
            prefix_sum.append(prefix_sum[-1] + n)

        # print(prefix_sum)

        left = 1
        right = 1

        while left <= len(arr) and right <= len(arr):
            sum_window = prefix_sum[right] - prefix_sum[left - 1]

            # found the window
            if sum_window == total_sum:
                return [left, right]

            # window size too big, so shift left to the right and start over
            if sum_window > total_sum:
                left += 1
                right = left
            else:
                # extend window size
                right += 1

        return []


s = Solution()
print(s.subarray_prefix_sum([1, 4], 0))
print(s.subarray_prefix_sum([5, 1, 2, 3, 4], 10))
print(s.subarray_prefix_sum([1, 4, 7], 7))
print(s.subarray_prefix_sum([15, 2, 4, 8, 9, 5, 10, 23], 23))
print(s.subarray_prefix_sum([1, 4, 0, 0, 3, 10, 5], 7))
print(s.subarray_prefix_sum([1, 4], 7))


# leetcode 560
# 560. Subarray Sum Equals K
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]

        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)

        counter = 0
        for i in range(1, len(prefix_sum)):
            for j in range(i, len(prefix_sum)):
                window_sum = prefix_sum[j] - prefix_sum[i - 1]
                if window_sum == k:
                    counter += 1

        return counter

    def subarraySum_prefix_counter(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefixSum = {0: 1}

        for n in nums:
            current_sum += n
            diff = current_sum - k

            result += prefixSum.get(diff, 0)

            # increment counter
            prefixSum[current_sum] = prefixSum.get(current_sum, 0) + 1

        return result


s = Solution2()
print(s.subarraySum([1, 1, 1], 2))
print(s.subarraySum([1, 2, 3], 3))
