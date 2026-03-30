class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenF = len(flowerbed)

        #edge cases
        #if arr is empty
        #if n == 0

        if lenF == 0:
            return n == 0
        elif lenF == 1:
            n = n - 1 if flowerbed[0] == 0 else n
            return n <= 0

        #main
        for i in range(lenF):
            if n == 0:
                break
            
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            if 0 < i < lenF - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            if i == lenF - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n == 0
