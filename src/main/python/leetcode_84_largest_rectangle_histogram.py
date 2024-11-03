# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# 84. Largest Rectangle in Histogram
# Hard
# Topics
# Companies
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
#
#
#
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = 100000
            # s = []
            for j in range(i, len(heights)):
                # s.append(heights[j])
                width = j - i + 1
                min_height = min(heights[j], min_height)
                current_area = width * min_height
                max_area = max(max_area, current_area)
                # print(f"set: {s}, width: {width}, height: {min_height}, area: {current_area}, max area: {max_area}")

        return max_area

    def largestRectangleArea_better(self, heights: List[int]) -> int:
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                a = h * w
                max_area = max(max_area, a)
                start = j
            stk.append((height, start))

        while stk:
            h, j = stk.pop()
            w = len(heights) - j
            max_area = max(max_area, h * w)

        return max_area

s = Solution()
print(s.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea(heights=[2, 4]))
