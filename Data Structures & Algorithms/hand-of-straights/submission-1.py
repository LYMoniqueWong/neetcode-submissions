class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:  return False
        hashSet = defaultdict(int)
        for i in hand:
            hashSet[i] += 1
        i = min(hand) 

        for _ in range(len(hand) // groupSize): 
            start = i 
            while hashSet[start] == 0:
                start += 1
            for val in range(start, start+groupSize): 
                if hashSet[val] == 0:
                    return False
                hashSet[val] -= 1

            i = start
        return True
        