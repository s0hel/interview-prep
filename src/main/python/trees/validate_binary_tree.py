# Definition for a binary tree node.
import math
from typing import Optional


# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lowest = float('-inf')
        highest = float('inf')

        def is_valid(node, min_value, max_value):
            if not node:
                return True
            if node.val <= min_value or node.val >= max_value:
                return False
            return is_valid(node.left, min_value, node.val) and is_valid(node.right, node.val, max_value)

        return is_valid(root, lowest, highest)


s = Solution()

n = TreeNode(2, TreeNode(1), TreeNode(3))
print(s.isValidBST(n))

n = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(s.isValidBST(n))

n = TreeNode(2, TreeNode(2), TreeNode(2))
print(s.isValidBST(n))

n = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(s.isValidBST(n))