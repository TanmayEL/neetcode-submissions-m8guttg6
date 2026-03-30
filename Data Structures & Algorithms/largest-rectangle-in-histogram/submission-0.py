class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            curr = heights[i]
            left, right = 0, 0
            l, r = i, i
            while l > 0 and heights[l - 1] >= curr:
                left += 1
                l -= 1
            while r < len(heights) - 1 and heights[r + 1] >= curr:
                right += 1
                r += 1
            maxArea = max(curr * (left + right + 1), maxArea)
        
        return maxArea
