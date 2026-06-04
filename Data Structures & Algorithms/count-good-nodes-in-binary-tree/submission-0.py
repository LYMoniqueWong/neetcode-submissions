# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, maxV):    # counts # of good nodes
            if not curr:    return 0
            res = 1 if curr.val >= maxV else 0
            maxV = max(maxV, curr.val)
            res += dfs(curr.left, maxV)
            res += dfs(curr.right, maxV)
            return res
        return dfs(root, root.val)