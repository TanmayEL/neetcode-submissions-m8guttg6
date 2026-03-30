# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = collections.deque([root])

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
                ans.append(temp[-1])
        
        return ans