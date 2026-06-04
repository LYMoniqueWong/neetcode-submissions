class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k+1):
            tmpPrices = prices.copy()
            for f, t, p in flights:
                if prices[f] == float("inf"):
                    continue
                if prices[f] + p < tmpPrices[t]:
                    tmpPrices[t] = prices[f] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]