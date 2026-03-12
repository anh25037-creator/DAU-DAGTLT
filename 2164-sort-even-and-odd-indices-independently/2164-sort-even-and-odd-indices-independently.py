class Solution:
    def sortEvenOdd(self, nums):
        even = sorted(nums[::2])          # index chẵn tăng dần
        odd = sorted(nums[1::2], reverse=True)  # index lẻ giảm dần
        
        nums[::2] = even
        nums[1::2] = odd
        
        return nums