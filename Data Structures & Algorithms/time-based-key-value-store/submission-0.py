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
        values = self.timeMap[key]
        if values:
            for i in range(len(values) - 1, -1, -1):
                if values[i][1] <= timestamp:
                    return values[i][0]
        return ""
