class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node [{self.val})"


class Solution:
    def bToDll(self, root: Node):
        head: Node = None

        def helper(node: Node, prev: Node):
            if not node:
                return

            helper(node.left, prev)
            if not prev:
                nonlocal head
                head = node
            else:
                node.left = prev
                prev.right = node

            helper(node.right, node)

        helper(root, None)
