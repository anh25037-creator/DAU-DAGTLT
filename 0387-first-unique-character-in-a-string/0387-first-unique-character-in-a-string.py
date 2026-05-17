class Solution:
    def firstUniqChar(self, s):

        # Dictionary để đếm số lần xuất hiện của mỗi ký tự
        count = {}

        # Duyệt từng ký tự trong chuỗi
        for ch in s:

            # Tăng số lần xuất hiện
            count[ch] = count.get(ch, 0) + 1

        # Duyệt lại chuỗi bằng index
        for i in range(len(s)):

            # Nếu ký tự xuất hiện đúng 1 lần
            if count[s[i]] == 1:

                # Trả về vị trí của ký tự đó
                return i

        # Nếu không có ký tự nào không lặp
        return -1