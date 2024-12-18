# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the
# values of the nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse inorder bst iteratively
        # requires a stack

        stack = []
        current = root

        while True:

            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()
            print("hit " + str(node.val))
            k -= 1
            if k == 0:
                return node.val

            current = node.right


        # lst = []
        # self.inorder(root, lst, k)
        # return lst[k - 1]

    # def inorder(self, root: Optional[TreeNode], lst: list[int], k: int):
    #
    #     if root:
    #         self.inorder(root.left, lst, k)
    #         lst.append(root.val)
    #         if len(lst) == k:
    #             return
    #         self.inorder(root.right, lst, k)


s = Solution()

rt = TreeNode(5)
rt.left = TreeNode(3)
rt.right = TreeNode(6)
rt.left.left = TreeNode(2)
rt.left.right = TreeNode(4)
rt.left.left.left = TreeNode(1)

print(s.kthSmallest(rt, 1))
print(s.kthSmallest(rt, 2))
print(s.kthSmallest(rt, 3))
print(s.kthSmallest(rt, 4))
print(s.kthSmallest(rt, 5))
print(s.kthSmallest(rt, 6))
