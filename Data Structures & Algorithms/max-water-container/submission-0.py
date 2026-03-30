class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0

        l, r = 0, n - 1

        while l < r:
            amount = min(heights[l], heights[r]) * (r - l)
            ans = max(ans, amount)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return ans
