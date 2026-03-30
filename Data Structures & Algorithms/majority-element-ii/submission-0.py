class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) / 3
        dic = {}
        st = set()

        for i in nums:
            count = 1 + dic.get(i, 0)
            dic[i] = count
            if count > n:
                st.add(i)
        
        return list(st)