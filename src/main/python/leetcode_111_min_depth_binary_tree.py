# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# 111. Minimum Depth of Binary Tree
# Easy
# Topics
# Companies
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # level order traversal
        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:

            level += 1

            for _ in range(len(q)):
                node = q.popleft()

                if node.left is None and node.right is None:
                    return level

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

    def minDepthRecursive(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        if not root.left:
            return 1 + self.minDepthRecursive(root.right)

        if not root.right:
            return 1 + self.minDepthRecursive(root.left)

        left_min_depth = 1 + self.minDepthRecursive(root.left)
        right_min_depth = 1 + self.minDepthRecursive(root.right)

        return min(left_min_depth, right_min_depth)


s = Solution()

root = TreeNode(3, TreeNode(9), TreeNode(20))
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(s.minDepth(root))

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)

print(s.minDepth(root))
