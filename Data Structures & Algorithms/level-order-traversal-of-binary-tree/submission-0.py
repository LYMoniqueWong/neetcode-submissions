# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        q, levelOrder = deque([[root]]), []
        while q:
            nodes = q.popleft()
            vals = [node.val for node in nodes]
            levelOrder.append(vals)

            res = []
            for i in nodes:
                if i.left:
                    res.append(i.left)
                if i.right:
                    res.append(i.right)
            if res:
                q.append(res)

        return levelOrder
