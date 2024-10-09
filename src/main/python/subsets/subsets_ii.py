# Subsets II
# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
#
# The solution must not contain duplicate subsets. You may return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,1]
#
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
# Example 2:
#
# Input: nums = [7,7]
#
# Output: [[],[7], [7,7]]
from typing import List


class Solution:
    def subsetsWithNoDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(index, subset):
            if index == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[index])
            # include number
            helper(index + 1, subset)

            # do not include number
            subset.pop()
            helper(index + 1, subset)

        helper(0, [])

        return result

    def subsetWithDups(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def helper(index, subset):
            if index >= len(nums):
                result.append(subset.copy())
                return

            # include number
            subset.append(nums[index])
            helper(index + 1, subset)

            # do not include number
            subset.pop()
            # keep iterating until number changes
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            helper(index + 1, subset)

        helper(0, [])
        return result


s = Solution()
# print(s.subsetsWithNoDup([1, 2, 3]))
print(s.subsetWithDups([1, 2, 1]))
print(s.subsetWithDups([7, 7]))
print(s.subsetWithDups([3, 1, 2, 3]))
