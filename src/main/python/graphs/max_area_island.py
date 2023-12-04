from typing import List


# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # start from 0,0 go all the way right, then down, repeat
        # if land is found, mark as visited, and find neighbors recursively, keep track of size
        # store max size in a variable

        max_size = 0
        visited = set()

        m = len(grid)
        n = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited:
                    val = grid[i][j]
                    visited.add((i, j))

                    if val == 0:
                        print(f"({i},{j}): Found water")
                    else:
                        print(f"({i},{j}): Found land")
                        curr_size = 1
                        to_process = list()

                        to_process.append((i, j + 1))
                        to_process.append((i, j - 1))
                        to_process.append((i + 1, j))
                        to_process.append((i - 1, j))

                        while len(to_process) != 0:
                            coords = to_process.pop()
                            x = coords[0]
                            y = coords[1]
                            if 0 <= x < m and 0 <= y < n and coords not in visited:
                                v = grid[x][y]
                                if v == 1:
                                    curr_size += 1
                                    print(f"({x},{y}): Found land, current size: {curr_size}")
                                    visited.add(coords)
                                    to_process.append((x, y + 1))
                                    to_process.append((x, y - 1))
                                    to_process.append((x + 1, y))
                                    to_process.append((x - 1, y))

                        print(f"Island size: {curr_size}")
                        max_size = max(max_size, curr_size)
                        print(f"Current Max size: {max_size}")

        return max_size


s = Solution()

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(s.maxAreaOfIsland(grid))
