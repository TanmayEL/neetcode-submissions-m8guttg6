# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            res.append(i.val for i in list(queue))
            curr = []
            while queue:
                cur = queue.popleft()
                if cur.left:
                    curr.append(cur.left)
                if cur.right:
                    curr.append(cur.right)
            queue = deque(curr[:])
        
        return res
