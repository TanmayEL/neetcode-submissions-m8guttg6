class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        res, curr = [], []

        def backtrack(i, sum):
            if sum == target:
                res.append(curr[:])
                return
            
            if i >= n or sum > target:
                return
            

            num = candidates[i]
            curr.append(num)
            backtrack(i + 1, sum + num)

            curr.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, sum)
        
        backtrack(0, 0)
        return res