# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        mid = inorder.index(root_val)
        
        left_pre = preorder[1: 1+mid]
        right_pre = preorder[mid+1:]

        left_in = inorder[:mid]
        right_in = inorder[mid+1:]
        
        root = TreeNode(root_val)
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root