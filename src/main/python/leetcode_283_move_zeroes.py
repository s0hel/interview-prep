# Given an integer array nums,
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums):

            if nums[i] == 0:
                while j < len(nums) and nums[j] == 0:
                    j += 1

                if j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j += 1

    def moveZeroes_better(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums


s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
print(nums)

nums = [0, 1, 0, 3, 0, 12]
s.moveZeroes(nums)
print(nums)

nums = [0, 1, 0, 3, 4, 12, 0, 15]
s.moveZeroes(nums)
print(nums)

nums = [1, 0]
s.moveZeroes(nums)
print(nums)
