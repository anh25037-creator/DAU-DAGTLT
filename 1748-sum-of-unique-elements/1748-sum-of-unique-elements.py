class Solution:
    def sumOfUnique(self, nums):
        total = 0
        
        for i in nums:
            if nums.count(i) == 1:
                total += i
                
        return total