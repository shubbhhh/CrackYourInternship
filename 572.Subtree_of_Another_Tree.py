def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            if (not p or not q) or p.val != q.val:
                return False
            else:
                return (isSame(p.left, q.left) and isSame(p.right, q.right))
        
        if not root:
            return False
        if not subRoot:
            return True
        if isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
