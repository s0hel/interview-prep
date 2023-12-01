from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [[]]  # ans[i] stores all nodes with a level of i

        def dfs(u):
            if u is None:
                return -1
            left_level = dfs(u.left)
            right_level = dfs(u.right)
            current_level = max(left_level, right_level) + 1  # calculate level of current node
            while len(ans) <= current_level:  # create more space in ans if necessary
                ans.append([])
            ans[current_level].append(u.val)
            return current_level

        dfs(root)
        return ans
