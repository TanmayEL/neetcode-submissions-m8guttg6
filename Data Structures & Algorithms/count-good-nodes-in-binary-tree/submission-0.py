# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(root, parent_val):
            if not root:
                return 
            
            if root.val >= parent_val:
                self.count += 1
            dfs(root.left, max(root.val, parent_val))
            dfs(root.right, max(root.val, parent_val))

        dfs(root, -101)
        return self.count