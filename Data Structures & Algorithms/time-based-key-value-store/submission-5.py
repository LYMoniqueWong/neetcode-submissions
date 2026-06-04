class TimeMap:

    def __init__(self):
        self.timeDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeDict:
            self.timeDict[key] = [[timestamp, value]]
        else:
            self.timeDict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeDict:    return ""
        target = self.timeDict[key]
        l, r = 0, len(target)-1 
        if timestamp < target[l][0]:
            return ""
        if timestamp >= target[r][0]:
                return target[r][1]      
        
        while l <= r: 
            m = (l+r)//2 
            if target[m][0] == timestamp:
                return target[m][1]
            elif target[m][0] < timestamp:
                l = m + 1 
            else:
                r = m - 1
        return target[r][1]
        
