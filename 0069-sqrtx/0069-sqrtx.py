class Solution:
    def mySqrt(self, x):
        
        # khoảng tìm kiếm từ 0 đến x
        left, right = 0, x
        
        # đáp án tạm thời
        ans = 0
        
        # binary search
        while left <= right:
            
            # chọn giữa
            mid = (left + right) // 2
            
            # nếu bình phương mid nhỏ hơn hoặc bằng x
            if mid * mid <= x:
                
                # cập nhật đáp án tốt nhất hiện tại
                ans = mid
                
                # thử tìm số lớn hơn
                left = mid + 1
            
            else:
                # mid quá lớn → giảm xuống
                right = mid - 1
        
        # trả về căn bậc 2 làm tròn xuống
        return ans