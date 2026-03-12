import math

class Solution:
    def pickGifts(self, gifts, k):
        for _ in range(k):
            m = max(gifts)
            i = gifts.index(m)
            gifts[i] = int(math.sqrt(m))
        return sum(gifts)