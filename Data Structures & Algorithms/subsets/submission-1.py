class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol, res = [], []

        def backtrack(i):
            if i >= n:
                res.append(sol.copy())
                return

            sol.append(nums[i])
            backtrack(i + 1)

            sol.pop()
            backtrack(i + 1)


        backtrack(0)
        return res