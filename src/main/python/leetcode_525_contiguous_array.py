from typing import List


# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeroSum = 0
        oneSum = 0

        for n in nums:
            if n == 0:
                zeroSum += 1
            else:
                oneSum += 1

        return min(zeroSum, oneSum) + min(zeroSum, oneSum)


s = Solution()
print(s.findMaxLength([0, 1]))
print(s.findMaxLength([0, 1, 0]))
print(s.findMaxLength([0, 1, 0, 0, 1]))
print(s.findMaxLength([0, 1, 1, 0]))
print(s.findMaxLength([1, 1, 1, 0, 0]))
print(s.findMaxLength([0, 1, 0, 0]))
print(s.findMaxLength([1, 0, 0, 0, 1, 1, 0]))
