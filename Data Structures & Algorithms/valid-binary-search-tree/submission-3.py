# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur, low, high):
            if not cur:    return True
            if not low < cur.val < high:
                return False
            return dfs(cur.left, low, cur.val) and dfs(cur.right, cur.val, high)
        return dfs(root, float('-inf'), float('inf'))