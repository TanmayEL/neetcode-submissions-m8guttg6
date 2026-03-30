class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        #[1, 2, 3, 3, 5, 6]

        l = 0
        r = k - 1
        max_diff = float('inf')

        while r < len(nums):
            max_diff = min(max_diff, nums[r] - nums[l])
            l += 1
            r += 1
        
        return max_diff