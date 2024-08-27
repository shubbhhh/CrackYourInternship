# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        minDiff = float("inf")
        for i in range(1, len(res)):
            minDiff = min(minDiff, res[i] - res[i-1])

        return minDiff