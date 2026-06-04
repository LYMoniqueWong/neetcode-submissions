# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        s = []
        curr = root
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            cnt += 1
            if cnt == k:
                return curr.val
            curr = curr.right