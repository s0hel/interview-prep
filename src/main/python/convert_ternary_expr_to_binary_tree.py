# https://www.geeksforgeeks.org/convert-ternary-expression-binary-tree/
# Given a string that contains ternary expressions. The expressions may be nested, task is convert the given ternary expression to a binary Tree.
from collections import deque


# Input :  string expression =   a?b:c
# Output :        a
#               /  \
#              b    c
# Input : expression =  a?b?c:d:e
# Output :     a
#            /  \
#           b    e
#         /  \
#        c    d

# Class to define a node
# structure of the tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def ternary_to_tree(exp):
    if not exp:
        return None
    root = Node(exp[0])
    stack = [root]
    for i in range(1, len(exp)):
        if exp[i] == '?':
            stack[-1].left = Node(exp[i + 1])
            stack.append(stack[-1].left)
        elif exp[i] == ':':
            stack.pop()
            while stack[-1].right:
                stack.pop()
            stack[-1].right = Node(exp[i + 1])
            stack.append(stack[-1].right)
    return root


def print_tree(root):
    if not root:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)


if __name__ == "__main__":
    exp = "a?b?c:d:e"
    root = ternary_to_tree(exp)
    print_tree(root)

