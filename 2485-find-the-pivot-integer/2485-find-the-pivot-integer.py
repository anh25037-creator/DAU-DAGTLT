class Solution:
    def pivotInteger(self, n):
        
        # tổng từ 1 đến n
        total = n * (n + 1) // 2
        
        # lấy căn bậc 2 của total
        x = int(total ** 0.5)
        
        # kiểm tra xem có phải số chính phương không
        if x * x == total:
            return x
        
        # nếu không tồn tại pivot
        return -1