class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr, res = [], []

        def backtrack( i, sum):

            if i >= len(nums) or sum > target:
                return
            
            if sum == target:
                res.append(curr[:])
                return
            
            num = nums[i]
            curr.append(num)
            backtrack(i, sum + num)

            curr.pop()

            backtrack(i + 1, sum)
        
        backtrack(0, 0)
        return res

