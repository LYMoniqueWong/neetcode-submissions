# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.cnt = 0
        def dfs(curr):   
            if not curr or self.ans:    return
            dfs(curr.left)
            self.cnt += 1
            if self.cnt == k:
                self.ans = curr.val
                return
            dfs(curr.right)
        dfs(root)
        return self.ans