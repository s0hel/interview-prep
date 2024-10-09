class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node [{self.val})"

def inorder(node: Node, result):
    if not node:
        return

    inorder(node.left, result)
    result.append(node.val)
    inorder(node.right, result)


def preorder(node: Node, result):
    # root, left, right
    if not node:
        return

    result.append(node.val)
    preorder(node.left, result)
    preorder(node.right, result)


def postorder(node: Node, result):
    # left, right, root
    if not node:
        return

    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.val)


def inorder_iterative(node: Node):
    result = []
    stack = []
    curr = node

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        # hit null on left-most child, so need to pop to get to parent
        curr = stack.pop()
        result.append(curr.val)

        # point curr to right child, and perform same operations as above
        curr = curr.right

    return result


def preorder_iterative(node: Node):
    # print each element as you go to the left
    # add right children to the stack
    result = []
    stack = []
    curr = node
    while stack or curr:
        while curr:
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left

        if stack:
            curr = stack.pop()

    return result


def postorder_iterative(node: Node):
    result = []
    stack = [node]
    visit = [False]
    while stack:
        curr, visited = stack.pop(), visit.pop()
        if curr:
            if visited:
                result.append(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)

    return result

#            5
#           / \
#         /    \
#        3      8
#       /      / \
#     1       6   9
#      \      \
#       2      7

node = Node(5)
node.left = Node(3)
node.right = Node(8)
node.left.left = Node(1)
node.left.left.right = Node(2)
node.right.left = Node(6)
node.right.right = Node(9)
node.right.left.right = Node(7)

print("in-order   traversal:")
result = []
inorder(node, result)
print(result)

print("in order iterative:")
print(inorder_iterative(node))

print("pre-order  traversal:")
result = []
preorder(node, result)
print(result)

print("pre-order  iterative:")
print(preorder_iterative(node))

print("post-order traversal:")
result = []
postorder(node, result)
print(result)

print("post-order  iterative:")
print(postorder_iterative(node))
