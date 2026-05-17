class Solution:
    def isPalindrome(self, s):
        
        # tạo chuỗi mới sau khi lọc ký tự hợp lệ
        new = ""
        
        # duyệt từng ký tự trong chuỗi ban đầu
        for c in s:
            
            # chỉ giữ lại ký tự chữ hoặc số
            if c.isalnum():
                
                # chuyển về chữ thường và thêm vào chuỗi mới
                new += c.lower()
        
        # so sánh chuỗi với bản đảo ngược của nó
        return new == new[::-1]