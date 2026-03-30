class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        minHeap = []
        # for i in range(len(points)):
        #     minHeap.append((sqrt(points[i[0] ** 2 + points[i][1] ** 2]), i))
        minHeap = [(math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), i) for i in range(n)]
        
        heapq.heapify(minHeap)

        returnVal = []

        for i in range(k):
            returnVal.append(points[heapq.heappop(minHeap)[1]])
        
        return returnVal