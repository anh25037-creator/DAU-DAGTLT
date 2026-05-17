class Solution:
    def numberGame(self, nums):
        
        # sắp xếp tăng dần để luôn lấy min dễ dàng
        nums.sort()
        
        # kết quả cuối cùng
        arr = []
        
        # duyệt từng cặp 2 phần tử
        for i in range(0, len(nums), 2):
            
            # nums[i] là nhỏ hơn trong cặp
            # nums[i+1] là lớn hơn trong cặp
            
            # Bob append trước → số lớn hơn đi trước
            arr.append(nums[i + 1])
            
            # Alice append sau → số nhỏ hơn đi sau
            arr.append(nums[i])
        
        return arr