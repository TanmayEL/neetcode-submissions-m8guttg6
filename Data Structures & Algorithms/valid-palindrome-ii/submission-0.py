class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(st, allowed):
            if not allowed:
                return False
            print(st)
            l, r = 0, len(st) - 1 

            while l <= r:
                if st[l] != st[r]:
                    allowed -= 1
                    return checkPalindrome(st[l:r], allowed) or checkPalindrome(st[l + 1 : r + 1], allowed)
                l += 1
                r -= 1
            
            return True
        
        return checkPalindrome(s, 2)
        

        

        