class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:  return False
        count = defaultdict(int)
        for n in hand:
            count[n] += 1

        for i in sorted(count):
            while count[i] > 0:
                for j in range(groupSize):
                    if count[i+j] <= 0:
                        return False
                    count[i+j] -= 1
        return True