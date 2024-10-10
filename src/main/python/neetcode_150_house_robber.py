from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        odd, even = 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even += num
            else:
                odd += num

        return max(even, odd)

    def rob2(self, nums: List[int]) -> int:

        cache = {}
        def solve(nums, index):
            if index > len(nums) - 1:
                return 0

            if index in cache:
                print(f"hit cache for index: {index}")
                return cache[index]

            cache[index] = max(nums[index] + solve(nums, index + 2), nums[index] + solve(nums, index + 3))
            return cache[index]

        return max(solve(nums, 0), solve(nums, 1))


nums = [1, 1, 3, 3]
s = Solution()
print(s.rob2(nums))

nums = [2, 9, 8, 3, 6]
print(s.rob2(nums))

nums = [5, 1, 2, 10, 6, 2, 7, 9, 3, 1]
print(s.rob2(nums))
