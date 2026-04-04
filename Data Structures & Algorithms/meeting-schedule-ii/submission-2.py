"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def sortIntervals(self, intervals):
        m = defaultdict(list)

        for interval in intervals:
            s, e = interval.start, interval.end
            m[s].append(e)
        
        # print(sorted(m.items()))
        return sorted(m.items())


    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        for s, endList in self.sortIntervals(intervals):
            for e in endList:
                if heap:
                    if heap[0] <= s:
                        heapq.heappop(heap)
                heapq.heappush(heap, e)
        
        return len(heap)