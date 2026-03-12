class Solution:
    def numberGame(self, nums):
        nums.sort()
        return [nums[i^1] for i in range(len(nums))]