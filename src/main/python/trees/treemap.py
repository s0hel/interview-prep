from typing import List


class Entry:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:

    def __init__(self):
        self.root: Entry = None

    def insert(self, key: int, val: int) -> None:
        self.insert_helper(self.root, key, val)

    def insert_helper(self, node: Entry, key, val):
        if not node:
            return Entry(key, val)
        else:
            if node.key < key:
                node.left = self.insert_helper(node.left, key, val)
            elif node.key > key:
                node.right = self.insert_helper(node.right, key, val)
            else:
                node.val = val

        return node

    def get(self, key: int) -> int:
        return self.get_helper(self.root, key)

    def get_helper(self, node: Entry, key) -> int:
        if not node:
            return -1

        if node.key < key:
            return self.get_helper(node.left, key)
        elif node.key > key:
            return self.get_helper(node.right, key)

        return node.val

    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr:
            if not curr.left:
                return curr.val
            curr = curr.left

    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr:
            if not curr.right:
                return curr.val
            curr = curr.right

    def remove(self, key: int) -> None:
        pass

    def getInorderKeys(self) -> List[int]:
        pass
