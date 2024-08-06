# 994. Rotting Oranges
# Medium
#
# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rotten = set()
        fresh = set()

        for x in range(m):
            for y in range(n):
                val = grid[x][y]
                if val == 2:
                    rotten.add((x, y))
                elif val == 1:
                    fresh.add((x, y))

        visited = set()
        queue = deque()
        for coords in rotten:
            queue.append(coords)
            visited.add(coords)

        time_taken = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                coords = queue.popleft()

                for d in directions:
                    new_coords = (coords[0] + d[0], coords[1] + d[1])

                    if 0 <= new_coords[0] < m \
                            and 0 <= new_coords[1] < n \
                            and new_coords not in visited \
                            and grid[new_coords[0]][new_coords[1]] == 1:
                        queue.append(new_coords)
                        visited.add(new_coords)
                        fresh.remove(new_coords)
            time_taken += 1

        if len(rotten) == 0 and len(fresh) > 0:
            return -1

        if len(rotten) == 0:
            return 0

        if len(fresh) == 0:
            return time_taken - 1

        return -1


grid = [[2, 1, 1, 1, 0, 0, 0],
        [1, 0, 2, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 2]]

s = Solution()
print(s.orangesRotting(grid))

grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]
print(s.orangesRotting(grid))

grid = [[2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]]
print(s.orangesRotting(grid))

grid = [[0, 2]]
print(s.orangesRotting(grid))

grid = [[0]]
print(s.orangesRotting(grid))

grid = [[1]]
print(s.orangesRotting(grid))

# more concise solution
# from collections import deque
#
# # Time complexity: O(rows * cols) -> each cell is visited at least once
# # Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue
#
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#
#         # number of rows
#         rows = len(grid)
#         if rows == 0:  # check if grid is empty
#             return -1
#
#         # number of columns
#         cols = len(grid[0])
#
#         # keep track of fresh oranges
#         fresh_cnt = 0
#
#         # queue with rotten oranges (for BFS)
#         rotten = deque()
#
#         # visit each cell in the grid
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 2:
#                     # add the rotten orange coordinates to the queue
#                     rotten.append((r, c))
#                 elif grid[r][c] == 1:
#                     # update fresh oranges count
#                     fresh_cnt += 1
#
#         # keep track of minutes passed.
#         minutes_passed = 0
#
#         # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
#         while rotten and fresh_cnt > 0:
#
#             # update the number of minutes passed
#             # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
#             minutes_passed += 1
#
#             # process rotten oranges on the current level
#             for _ in range(len(rotten)):
#                 x, y = rotten.popleft()
#
#                 # visit all the adjacent cells
#                 for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#                     # calculate the coordinates of the adjacent cell
#                     xx, yy = x + dx, y + dy
#                     # ignore the cell if it is out of the grid boundary
#                     if xx < 0 or xx == rows or yy < 0 or yy == cols:
#                         continue
#                     # ignore the cell if it is empty '0' or visited before '2'
#                     if grid[xx][yy] == 0 or grid[xx][yy] == 2:
#                         continue
#
#                     # update the fresh oranges count
#                     fresh_cnt -= 1
#
#                     # mark the current fresh orange as rotten
#                     grid[xx][yy] = 2
#
#                     # add the current rotten to the queue
#                     rotten.append((xx, yy))
#
#
#         # return the number of minutes taken to make all the fresh oranges to be rotten
#         # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
#         return minutes_passed if fresh_cnt == 0 else -1