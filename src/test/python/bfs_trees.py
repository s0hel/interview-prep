from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_trees(node: Node):
    # go level by left
    if not node:
        return

    q = deque()

    q.append(node)
    level = 1
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            print(f"level: {level}, val: {n.val}")
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        level += 1


#            5
#         /     \
#        3      8
#       / \    / \
#     1    4  6   9

node = Node(5)
node.left = Node(3)
node.left.left = Node(1)
node.left.right = Node(4)
node.right = Node(8)
node.right.left = Node(6)
node.right.right = Node(9)

bfs_trees(node)
