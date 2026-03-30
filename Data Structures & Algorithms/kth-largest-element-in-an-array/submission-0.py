class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)

        res = None

        for i in range(k):
            res = heapq.heappop(nums)
        
        return -res