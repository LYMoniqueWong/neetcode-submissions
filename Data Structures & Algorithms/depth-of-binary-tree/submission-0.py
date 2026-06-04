# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(cur):
            if not cur: return 0
            left, right = dfs(cur.left), dfs(cur.right)
            return 1 + max(left, right)
        return dfs(root)