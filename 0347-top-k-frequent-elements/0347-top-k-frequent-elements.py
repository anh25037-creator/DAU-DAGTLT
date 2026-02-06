from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        # sort theo tần suất giảm dần
        count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in count_sorted[:k]]
