class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        res, values = "", self.timeMap[key]
        if values:
            if values[-1][1] <= timestamp:
                return values[-1][0]
            else: # run binary search
                l, r = 0, len(values)-2
                while l <= r:
                    m = (l+r) // 2
                    if values[m][1] <= timestamp:
                        res = values[m][0]
                        l = m+ 1
                    else:
                        r = m -1
        return res
