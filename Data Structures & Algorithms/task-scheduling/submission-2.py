class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        count = {}
        ans = 0

        for i in tasks:
            count[i] = 1 + count.get(i, 0)
        
        maxHeap = [-1 * val for val in count.values()]

        heapq.heapify(maxHeap)

        time = 0
        
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time

            
            

