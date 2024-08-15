# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal res
            if not node:
                return

            if node.left and (not node.left.left and not node.left.right):
                res += node.left.val
            # if not node.right and node.left:
            #     res += node.left.val
            #     return
            
            # if not node.left and node.right:
            #     res += node.right.val
            #     return

            dfs(node.left)
            dfs(node.right)

        res = 0
        dfs(root)
        return res