def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        def symmetry(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
            elif not node1 and not node2:
                return True
            else:
                return False

            return symmetry(node1.left, node2.right) and symmetry(node1.right, node2.left)
                
        return symmetry(root.left, root.right)
