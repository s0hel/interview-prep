import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones_inverted = []
        for s in stones:
            stones_inverted.append(s * -1)

        heapq.heapify(stones_inverted)

        while len(stones_inverted) > 1:
            s1 = heapq.heappop(stones_inverted) * -1
            s2 = heapq.heappop(stones_inverted) * -1

            if s1 != s2:
                new_stone = s1 - s2
                heapq.heappush(stones_inverted, new_stone * -1)

        if len(stones_inverted) == 1:
            return stones_inverted[0] * -1

        return 0

