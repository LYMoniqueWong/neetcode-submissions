# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            if not isSameTree(r1.left, r2.left) or not isSameTree(r1.right, r2.right):
                return False
            return True
        if not subRoot: return True
        if not root:    return False
        if isSameTree(root, subRoot):   return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)