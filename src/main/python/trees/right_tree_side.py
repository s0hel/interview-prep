from collections import deque
from typing import List, Optional, Deque


# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:
#
# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result: List[int] = []

        queue: Deque[TreeNode] = deque()
        queue.append(root)

        level = 1
        while len(queue) > 0:
            print(f"level: {level}")

            qlen = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                print(f" --> {node.val}")
                if i == qlen - 1:
                    print(f" --> most right: {node.val}")
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return result


tree = TreeNode(1)
tree.left = TreeNode(2, None, TreeNode(5))
tree.right = TreeNode(3, None, TreeNode(4))

s = Solution()

print(s.rightSideView(tree))

tree = TreeNode(1, None, TreeNode(3))
print(s.rightSideView(tree))

tree = TreeNode(1, TreeNode(2), None)
print(s.rightSideView(tree))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.right = TreeNode(5)
tree.left.right.left = TreeNode(4)
tree.right = TreeNode(3)
tree.right.left = TreeNode(6)
## output should be: 1 3 6 4
print(s.rightSideView(tree))
