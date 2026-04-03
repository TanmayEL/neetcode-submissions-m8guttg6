class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ansIdx, ansLen = 0, 0
        
        def isPalindrome(l, r):
            nonlocal ansIdx, ansLen
            
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > ansLen:
                    ansIdx = l
                    ansLen = r - l + 1
                l -= 1
                r += 1

        for i in range(n):
            isPalindrome(i, i)
            isPalindrome(i, i + 1)
        
        return s[ansIdx : ansIdx + ansLen]
        
