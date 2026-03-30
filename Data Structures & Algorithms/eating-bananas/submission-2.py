import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        max_no = max(piles)
        if h == n:
            return max_no
        
        k = 0
        l, r = 1, max_no
        min_rate = max_no
        
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
        
