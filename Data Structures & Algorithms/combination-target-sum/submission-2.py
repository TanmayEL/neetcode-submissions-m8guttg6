class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def dfs(i, total):
            if total == target:
                res.append(sol.copy())
                return
            
            if i >= n or total > target:
                return
            
            include = nums[i]
            sol.append(nums[i])
            dfs(i, include + total)

            sol.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res