class Solution:
    def prefixCount(self, words, pref):
        count = 0
        
        # duyệt từng từ trong mảng words
        for word in words:
            
            # kiểm tra word có bắt đầu bằng pref không
            if word.startswith(pref):
                count += 1
        
        return count