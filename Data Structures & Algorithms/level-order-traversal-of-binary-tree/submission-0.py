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
            
        q = collections.deque([root])
        ans = []

        while q:
            lenQ = len(q)
            temp = []
            for i in range(lenQ):
                node = q.popleft()
                temp.append(node.val)
                l, r = node.left, node.right
                if l:
                    q.append(l)
                if r:
                    q.append(r)
            if temp:
                ans.append(temp)
        
        return ans