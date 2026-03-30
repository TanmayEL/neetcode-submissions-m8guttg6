class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        arr = self.dic[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            
            elif arr[mid][0] < timestamp:
                l += 1
            
            else:
                r -= 1
        
        if arr and arr[r][0] <= timestamp:
            return arr[r][1]
        return ""