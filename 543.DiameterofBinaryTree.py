# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
                if not root:  
                    return 0

                left_height = depth(root.left) 
                right_height = depth(root.right) 
                
                self.diameter = max(self.diameter, left_height + right_height)

                return 1 + max(left_height, right_height)
        
        depth(root)
        return self.diameter