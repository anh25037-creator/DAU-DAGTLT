from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s):
        count = Counter(s)
        return len(set(count.values())) == 1