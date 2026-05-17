class Solution:
    def canConstruct(self, ransomNote, magazine):
        
        # Dictionary để đếm số lần xuất hiện ký tự trong magazine
        count = {}
        
        # Duyệt từng ký tự trong magazine
        for ch in magazine:
            
            # Tăng số lần xuất hiện
            count[ch] = count.get(ch, 0) + 1
        
        # Duyệt từng ký tự trong ransomNote
        for ch in ransomNote:
            
            # Nếu ký tự không có
            # hoặc đã dùng hết
            if ch not in count or count[ch] == 0:
                return False
            
            # Dùng 1 ký tự
            count[ch] -= 1
        
        return True