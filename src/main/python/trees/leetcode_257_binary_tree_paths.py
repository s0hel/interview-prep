# Definition for a binary tree node.
from typing import Optional, List


# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []

        def dfs(node: TreeNode, path: str):
            if not node:
                return

            if len(path) == 0:
                path = str(node.val)
            else:
                path += "->" + str(node.val)

            dfs(node.left, path)
            dfs(node.right, path)

            # found a leaf
            if not node.left and not node.right:
                result.append(path)

        dfs(root, "")

        return result


s = Solution()
n = TreeNode(1, TreeNode(2), TreeNode(3))
n.left.right = TreeNode(5)

print(s.binaryTreePaths(n))
