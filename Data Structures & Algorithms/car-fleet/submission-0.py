class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleet = 0
        slowest_time = -1.0
        for p, s in cars[::-1]:
            t = (target-p)/s
            if t > slowest_time:
                fleet += 1
                slowest_time = t
        return fleet
