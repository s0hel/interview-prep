# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        queue = deque()
        queue.append(root)
        level = 0
        array: List[List[int]] = []

        while len(queue) > 0:

            print(f"level: {level}")
            queue_size = len(queue)

            sub_array: List[int] = []
            for _ in range(queue_size):
                curr = queue.popleft()
                sub_array.append(curr.val)
                print(f"--> {curr.val}")
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            array.append(sub_array)
            level += 1

        return array


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

s = Solution()
print(s.levelOrder(root))
