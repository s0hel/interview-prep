# 167. Two Sum II - Input Array Is Sorted
# Medium
# Topics
# Companies
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#
#
# Constraints:
#
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 1
        length = len(numbers)

        print(f"Target: {target}")

        num_set = {}
        numbers2 = []

        for i in range(length):
            if numbers[i] not in num_set:
                numbers2.append((i, numbers[i]))
                num_set[numbers[i]] = [i]
            elif len(num_set[numbers[i]]) < 2:
                numbers2.append((i, numbers[i]))
                num_set[numbers[i]].append(i)

        print(numbers2)

        while index1 < len(numbers2):
            idx1, v1 = numbers2[index1]
            idx2, v2 = numbers2[index2]
            sum = v1 + v2

            print(f"v1[{idx1}]: {v1}, v2[{idx2}]: {v2}, sum: {sum}")

            if sum == target:
                return [idx1 + 1, idx2 + 1]

            index2 += 1
            if index2 >= len(numbers2):
                index2 = index1 + 2
                index1 += 1

        # while index1 < length:
        #     v1 = numbers[index1]
        #     v2 = numbers[index2]
        #     sum = v1 + v2
        #
        #     print(f"v1[{index1}]: {v1}, v2[{index2}]: {v2}, sum: {sum}")
        #
        #     if sum == target:
        #         return [index1 + 1, index2 + 1]
        #
        #     index2 += 1
        #     if index2 >= length:
        #         index2 = index1 + 2
        #         index1 += 1
        #         print(f"assigning index1: {index1}, index2: {index2}")

        return [0, 0]


s = Solution()
print(s.twoSum([2, 2, 2, 7, 7, 11, 11, 15, 15, 15], 9))
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 7, 11, 15], 18))
print(s.twoSum([2, 7, 11, 15], 13))
print(s.twoSum([2, 7, 11, 15], 17))
print(s.twoSum([2, 7, 11, 15], 26))
