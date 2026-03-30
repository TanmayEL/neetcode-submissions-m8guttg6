class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        currSum = 0
        minLength = n + 1

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target and left <= right:
                minLength = min(minLength, right - left + 1)
                currSum -= nums[left]
                left += 1
        
        return minLength if minLength <= n else 0

