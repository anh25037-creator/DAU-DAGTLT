class Solution:
    def lengthOfLastWord(self, s):
        
        # Xóa khoảng trắng ở đầu và cuối chuỗi
        s = s.strip()
        
        # Tách chuỗi thành các từ
        words = s.split()
        
        # Lấy độ dài của từ cuối cùng
        return len(words[-1])
