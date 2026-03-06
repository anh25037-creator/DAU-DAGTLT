class Solution:
    def areOccurrencesEqual(self, s):
        from collections import Counter
        freq = Counter(s)
        return len(set(freq.values())) == 1