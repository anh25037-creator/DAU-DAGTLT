class Solution:
    def isSubsequence(self, s, t):
        
        # i dùng để theo dõi vị trí trong chuỗi s
        i = 0
        
        # Duyệt từng ký tự trong chuỗi t
        for ch in t:
            
            # Nếu:
            # - i vẫn còn trong phạm vi của s
            # - ký tự hiện tại của s bằng ký tự trong t
            if i < len(s) and s[i] == ch:
                
                # Sang ký tự tiếp theo của s
                i += 1
        
        # Nếu i bằng độ dài s
        # nghĩa là đã tìm được toàn bộ ký tự của s theo đúng thứ tự
        return i == len(s)

