from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_map = {}

        for n in nums:
            if n not in num_map:
                num_map[n] = 1
            else:
                num_map[n] += 1

        count = 0
        for n in num_map.keys():
            if k == 0:
                if num_map[n] > 1:
                    count += 1
            else:
                if n + k in num_map:
                    count += 1

        return count


s = Solution()
print(s.findPairs([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3))
