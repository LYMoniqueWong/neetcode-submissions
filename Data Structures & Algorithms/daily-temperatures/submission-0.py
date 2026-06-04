class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            streak = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = streak
                    break
                streak += 1
                # if j == len(temperatures)-1:
                #     result[i] = 0
        return result