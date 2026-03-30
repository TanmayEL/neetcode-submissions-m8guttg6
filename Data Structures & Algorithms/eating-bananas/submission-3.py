import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = r
    
        while l <= r:
            mid = (l + (r - l) // 2)
            curr = 0
            for p in piles:
                curr += math.ceil(p / mid)
            if curr > h:
                l = mid + 1
            else:
                r = mid - 1
                min_rate = min(min_rate, mid)
        return min_rate
        
