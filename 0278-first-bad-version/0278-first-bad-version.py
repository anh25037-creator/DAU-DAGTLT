# API isBadVersion đã được định nghĩa sẵn
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        
        # khoảng tìm kiếm ban đầu
        left, right = 1, n
        
        # binary search
        while left < right:
            
            # chọn giữa
            mid = (left + right) // 2
            
            # nếu mid là bad version
            if isBadVersion(mid):
                
                # có thể đây là đáp án → thu hẹp bên trái
                right = mid
            
            else:
                # mid là good → đáp án nằm bên phải
                left = mid + 1
        
        # left chính là version bad đầu tiên
        return left