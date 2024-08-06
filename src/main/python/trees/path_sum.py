from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.path_sum(root, targetSum, 0)

    def path_sum(self, node: Optional[TreeNode], targetSum: int, current_sum: int):
        if node is None:
            return False

        current_sum += node.val

        if node.left is None and node.right is None:
            if current_sum == targetSum:
                return True

        if self.path_sum(node.left, targetSum, current_sum):
            return True

        if self.path_sum(node.right, targetSum, current_sum):
            return True

        current_sum -= node.val
        return False


s = Solution()

root = TreeNode(5, TreeNode(4), TreeNode(8))
root.left.left = TreeNode(11, TreeNode(7), TreeNode(2))
root.right.left = TreeNode(13)
root.right.right = TreeNode(4, None, TreeNode(1))

print(s.hasPathSum(root, 18))  # True
print(s.hasPathSum(root, 19))  # False
print(s.hasPathSum(root, 20))  # False
print(s.hasPathSum(root, 21))  # False
print(s.hasPathSum(root, 22))  # True
print(s.hasPathSum(root, 26))  # True
print(s.hasPathSum(root, 27))  # True
