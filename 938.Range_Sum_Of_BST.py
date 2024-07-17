def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if node:
                if low <= node.val <= high:
                    count += node.val
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        dfs(root)
        return count
