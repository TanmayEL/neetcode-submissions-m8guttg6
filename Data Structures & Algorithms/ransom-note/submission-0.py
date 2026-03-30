class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_mag = {}
        for c in magazine:
            dict_mag[c] = 1 + dict_mag.get(c, 0)
        
        for c in ransomNote:
            if c not in dict_mag:
                return False
            
            currCount = dict_mag[c]
            if currCount <= 0:
                return False
            
            dict_mag[c] -= 1
        
        return True