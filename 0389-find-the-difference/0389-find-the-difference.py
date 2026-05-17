class Solution:
    def findTheDifference(self, s, t):

        # Dictionary để đếm ký tự
        count = {}

        # Đếm số lần xuất hiện trong s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Duyệt chuỗi t
        for ch in t:

            # Nếu ký tự chưa có
            # hoặc đã dùng hết
            if ch not in count or count[ch] == 0:
                return ch

            # Giảm số lần xuất hiện
            count[ch] -= 1