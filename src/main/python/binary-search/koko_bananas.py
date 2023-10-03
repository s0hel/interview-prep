#
# 875. Koko Eating Bananas
# Medium
import math
from typing import List


# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.
#
#
#
# Example 1:
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
# Constraints:
#
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_speed = 1
        max_speed = h

        for i in range(len(piles)):
            if piles[i] < min_speed:
                min_speed = piles[i]
            if piles[i] > max_speed:
                max_speed = piles[i]

        while min_speed <= max_speed:
            speed = (max_speed - min_speed) // 2 + min_speed

            if self.can_eat(piles, speed, h):
                max_speed = speed - 1
            else:
                min_speed = speed + 1

        return min_speed

    def can_eat(self, piles: List[int], speed: int, hours: int) -> bool:

        hours_required = 0

        for i in range(len(piles)):
            hours_required += piles[i] // speed

            if piles[i] % speed != 0:
                hours_required += 1

            if hours_required > hours:
                print(f"Speed: {speed}, Hours Required: {hours_required}, Hours allowed: {hours} => False")
                return False

        print(f"Speed: {speed}, Hours Required: {hours_required}, Hours allowed: {hours} => True")
        return True


s = Solution()
piles = [312884470]
hours = 312884469
min_speed = s.minEatingSpeed(piles, hours)

print(f"Piles: {piles}, Hours: {hours}, Min Speed: {min_speed}")
