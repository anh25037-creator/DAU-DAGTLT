class Solution:
    def isAnagram(self, s, t):
        
        # Nếu độ dài khác nhau
        # chắc chắn không phải anagram
        if len(s) != len(t):
            return False
        
        # Sắp xếp 2 chuỗi rồi so sánh
        return sorted(s) == sorted(t)
