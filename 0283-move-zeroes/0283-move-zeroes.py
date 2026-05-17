class Solution:
    def moveZeroes(self, nums):
        
        # k là vị trí để ghi các số khác 0
        k = 0
        
        # duyệt toàn bộ mảng
        for x in nums:
            
            # nếu gặp số khác 0
            if x != 0:
                
                # đưa số đó lên vị trí k
                nums[k] = x
                
                # tăng k
                k += 1
        
        # sau khi đưa hết số khác 0 lên trước
        # điền 0 vào phần còn lại
        for i in range(k, len(nums)):
            nums[i] = 0