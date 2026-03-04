import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = re.findall(r'\w+', paragraph.lower())
        banned_set = set(banned)
        count = Counter(word for word in words if word not in banned_set)
        return count.most_common(1)[0][0]