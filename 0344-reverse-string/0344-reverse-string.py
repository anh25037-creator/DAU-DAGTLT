class Solution:
    def reverseString(self, s):
        
        # con trỏ trái bắt đầu từ đầu mảng
        left = 0
        
        # con trỏ phải bắt đầu từ cuối mảng
        right = len(s) - 1
        
        # duyệt cho đến khi 2 con trỏ gặp nhau
        while left < right:
            
            # hoán đổi ký tự ở 2 đầu
            s[left], s[right] = s[right], s[left]
            
            # di chuyển con trỏ vào giữa
            left += 1
            right -= 1