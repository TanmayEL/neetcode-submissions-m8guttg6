class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [], []
        ans = 0

        curr_max = -1
        for h in height:
            curr_max = max(curr_max, h)
            left.append(curr_max)

        curr_max = -1
        for h in height[::-1]:
            curr_max = max(curr_max, h)
            right.append(curr_max)
        
        right = right[::-1]

        for h in range(len(height)):
            if h == 0 or h == len(height) - 1:
                continue
            water = min(left[h], right[h]) - height[h]
            if water > 0:
                ans += water
        
        return ans