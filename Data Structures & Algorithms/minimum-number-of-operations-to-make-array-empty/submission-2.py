class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dct = {}
        count = 0

        for num in nums:
            dct[num] = 1 + dct.get(num, 0)
        
        print(dct)

        for counts in dct.values():
            tempNum = 0
            if counts != 1 and counts % 3 == 1:
                count += (counts - 4) // 3
                count += 2
            elif counts != 1 and counts % 3 == 2:
                count += (counts - 2) // 3
                count += 1
            elif counts % 3 == 0:
                count += counts // 3
            elif counts % 2 == 0:
                count += counts // 2
            else:
                count = -1
                break

        
        return count


