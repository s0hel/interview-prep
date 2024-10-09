from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def is_combo(next_num, nums, current_sum, path, target):
            path.append(next_num)
            new_sum = current_sum + next_num

            print(f"path: {path}, current_sum: {new_sum}, target: {target}")

            if new_sum > target:
                path.pop()
                return

            if new_sum == target:
                result.append(path.copy())
                path.pop()
                return

            for n in nums:
                is_combo(n, nums, new_sum, path, target)

            path.pop()

        for n in nums:
            path = []
            is_combo(n, nums, 0, path, target)

        return result


s = Solution()

# nums = [2, 5, 6, 9]
# target = 9
# print(s.combinationSum(nums, target))

nums = [3, 4, 5]
target = 16
print(s.combinationSum(nums, target))
