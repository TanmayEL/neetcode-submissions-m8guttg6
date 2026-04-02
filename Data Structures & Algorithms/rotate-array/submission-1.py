class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(startIndex, endIndex):
            nonlocal nums
            while startIndex < endIndex:
                nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
                startIndex += 1
                endIndex -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        