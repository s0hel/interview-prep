# 112. Path Sum
#
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# Example 3:
#
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
from typing import Optional, Deque, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)

    def helper(self, root, target_sum, current_sum):
        # if base case return True
        if not root:
            return False
        else:
            current_sum += root.val

        if not root.left and not root.right:
            return current_sum == target_sum

        if self.helper(root.left, target_sum, current_sum):
            return True

        if self.helper(root.right, target_sum, current_sum):
            return True

        return False

    # simpler and better:
    def hasPathSum2(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum2(root.left, sum) or self.hasPathSum2(root.right, sum)


root = TreeNode(5, TreeNode(4), TreeNode(8))
root.left.left = TreeNode(11, TreeNode(7), TreeNode(2))
root.right.left = TreeNode(13)
root.right.right = TreeNode(4, None, TreeNode(1))

s = Solution()
print(f"Target Sum: 22 => {s.hasPathSum(root, 22)}")
print(f"Target Sum: 23 => {s.hasPathSum(root, 23)}")
print(f"Target Sum: 24 => {s.hasPathSum(root, 24)}")
print(f"Target Sum: 25 => {s.hasPathSum(root, 25)}")
print(f"Target Sum: 26 => {s.hasPathSum(root, 26)}")
print(f"Target Sum: 18 => {s.hasPathSum(root, 18)}")
print(f"Target Sum: 19 => {s.hasPathSum(root, 19)}")

root = TreeNode(-2, None, TreeNode(-3))
print(f"Target Sum: -5 => {s.hasPathSum(root, -5)}")

root = TreeNode(8)
root.left = TreeNode(9)
root.right = TreeNode(-6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(9)
print(f"Target Sum: 7 => {s.hasPathSum(root, 7)}")
