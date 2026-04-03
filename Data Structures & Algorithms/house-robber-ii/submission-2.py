class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def helper(a, b):
            prev, curr = nums[a], max(nums[a], nums[a + 1])

            for i in range(a + 2, b):
                prev, curr = curr, max(nums[i] + prev, curr)
            
            return curr

        
        return max(helper(0, n - 1), helper(1, n))
        
