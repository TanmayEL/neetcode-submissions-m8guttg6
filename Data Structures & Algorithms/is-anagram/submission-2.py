class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for cs, ct in zip(s, t):
            count = d1.get(cs, 0) + 1
            d1[cs] = count
            count = d2.get(ct, 0) + 1
            d2[ct] = count
        
        return d1 == d2

