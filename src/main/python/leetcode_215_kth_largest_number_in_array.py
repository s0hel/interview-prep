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
import heapq
from typing import List


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

    def find_kth_largest(self, nums: List[int], k: int) -> int:
        # use heaps or use quick select
        # heaps is easier to code
        # min-heap way
        min_heap = []
        counter = 0

        for n in nums:
            heapq.heappush(min_heap, n)
            counter += 1
            if counter > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

    def find_kth_largest_qs(self, nums: List[int], k: int) -> int:
        def partition(start_index: int, end_index: int):
            pivot_value = nums[end_index]

            left = start_index

            for i in range(start_index, end_index):
                if nums[i] < pivot_value:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1

            # swap left and pivot
            nums[left], nums[end_index] = nums[end_index], nums[left]

            return left

        def qs(start, end):
            pivot = partition(start, end)

            target_index = len(nums) - k

            if pivot == target_index:
                return nums[pivot]
            elif pivot > target_index:
                return qs(start, pivot - 1)
            else:
                return qs(pivot + 1, end)

        return qs(0, len(nums) - 1)


s = Solution()
print(s.find_kth_largest_qs([3, 2, 1, 5, 6, 4], 2))
print(s.find_kth_largest_qs([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
