class Solution:
    def countEven(self, num):
        count = 0
        
        # duyệt tất cả số từ 1 đến num
        for x in range(1, num + 1):
            s = 0
            
            # tính tổng chữ số của x
            temp = x
            while temp > 0:
                s += temp % 10   # lấy chữ số cuối
                temp //= 10      # bỏ chữ số cuối
            
            # kiểm tra tổng chữ số có chẵn không
            if s % 2 == 0:
                count += 1
        
        return count