class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        arr = self.dic.get(key, [])
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res