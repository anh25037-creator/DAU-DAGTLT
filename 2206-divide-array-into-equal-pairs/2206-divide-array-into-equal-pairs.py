class Solution:
    def divideArray(self, nums):
        from collections import Counter
        
        count = Counter(nums)
        
        for v in count.values():
            if v % 2 != 0:
                return False
        
        return True