class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        prev, curr = nums[0], max(nums[0], nums[1])

        for i in range(2, n - 1):
            prev, curr = curr, max(nums[i] + prev, curr)

        prev2, curr2 = nums[1], max(nums[1], nums[2])

        for i in range(3, n):
            prev2, curr2 = curr2, max(nums[i] + prev2, curr2)
        
        return max(curr, curr2)
        
