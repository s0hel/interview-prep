# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
#
#
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use quick sort and stop when pivot = k

        start = 0
        end = len(nums) - 1
        target_pivot = len(nums) - k

        return self.quick_selectt(nums, start, end, target_pivot)

    def quick_selectt(self, nums: List[int], start: int, end: int, target_pivot: int):
        ## quick sort
        # pick a pivot
        # two pointers
        # start and left pointer
        # go from start to end, compare each element against pivot value.
        # if less than pivot value, swap CURRENT value with LEFT value.  Move LEFT pointer to the right
        # once done iterating, SWAP pivot value and LEFT value
        # at this stage, the value in the LEFT pointer is where it is supposed to be
        # if LEFT index == target_pivot, return that value
        # if TARGET_PIVOT < LEFT INDEX, then recursively run this function on START -> LEFT - 1
        # if TARGET_PIVOT > LEFT INDEX, then recursively run this function on LEFT + 1 -> END

        # if array is empty or size 1, then dont do anything
        # if end - start + 1 <= 1:
        #    return -1

        pivot_index = end
        pivot_value = nums[pivot_index]
        left_index = start

        for i in range(start, end):
            if nums[i] < pivot_value:
                nums[left_index], nums[i] = nums[i], nums[left_index]
                left_index += 1

        nums[pivot_index], nums[left_index] = nums[left_index], nums[pivot_index]

        if left_index == target_pivot:
            return nums[target_pivot]
        elif target_pivot < left_index:
            return self.quick_selectt(nums, start, left_index - 1, target_pivot)
        else:
            return self.quick_selectt(nums, left_index + 1, end, target_pivot)
