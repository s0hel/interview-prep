# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root: Optional[TreeNode], result: List[int]):
        # in order traversal: left -> root -> right
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)

        return result
