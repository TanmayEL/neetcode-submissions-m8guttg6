class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            num1 = - (heapq.heappop(maxHeap))
            num2 = - (heapq.heappop(maxHeap))

            if num1 == num2:
                continue
            
            heapq.heappush(maxHeap, -(abs(num1 - num2)))
        
        returnVal = -maxHeap[0] if maxHeap else 0
        return returnVal