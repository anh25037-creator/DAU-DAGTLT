class Solution:
    def firstUniqChar(self, s):
        count = {}
        
        # đếm số lần xuất hiện
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        # tìm ký tự xuất hiện 1 lần đầu tiên
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1