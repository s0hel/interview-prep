class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node [{self.val})"


class Solution:
    def __init__(self):
        self.head: Node = None
        self.prev: Node = None

    def bToDll(self, root: Node):

        def helper(node: Node):
            if not node:
                return

            helper(node.left)
            if not self.prev:
                self.head = node
            else:
                node.left = self.prev
                self.prev.right = node

            self.prev = node
            helper(node.right)

        helper(root)


root = Node(3)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(1)
root.right.left.left = Node(4)
root.right.left.right = Node(6)

s = Solution()
s.bToDll(root)
print(s.head)
print(s.head.right)
print(s.head.right.right)
print(s.head.right.right.right)
print(s.head.right.right.right.right)
print(s.head.right.right.right.right.right)
