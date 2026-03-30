class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dct = {}
        count = 0

        for num in nums:
            dct[num] = 1 + dct.get(num, 0)
        
        print(dct)

        # 1 - 1
        # 2 - 1
        # 3 - 1
        # 4 - 2
        # 5 - 2
        # 6 - 2
        # 7 - 3
        # 8 - 3
        # 9 - 3

        for counts in dct.values():
            if counts == 1:
                return -1
            else:
                count += math.ceil(counts / 3)

        
        return count


