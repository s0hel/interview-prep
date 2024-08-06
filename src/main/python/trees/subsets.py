from typing import List


# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def helper(idx: int):
            if idx >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[idx])
            helper(idx + 1)
            subset.pop()
            helper(idx + 1)

        helper(0)

        return result


s = Solution()
print(s.subsets([1, 2, 3, 4]))
