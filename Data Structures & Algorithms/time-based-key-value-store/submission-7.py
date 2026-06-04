class TimeMap:
    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.timeMap[key] # sorted
        if not vals:    return ""
        l,r,res = 0, len(vals)-1, (-1, "")
        while l <= r:
            m = (l+r)//2
            if vals[m][0] <= timestamp and vals[m][0] > res[0]:
                res = vals[m]
                l = m+1
            elif vals[m][0] > timestamp:
                r = m-1
        return res[1]

