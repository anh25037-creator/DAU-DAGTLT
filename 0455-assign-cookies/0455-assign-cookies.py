#Phát bánh quy cho trẻ em
class Solution:
    def findContentChildren(self, g, s):

        # Sắp xếp độ tham lam của trẻ
        g.sort()

        # Sắp xếp kích thước bánh
        s.sort()

        # i dùng cho trẻ em
        i = 0

        # j dùng cho bánh
        j = 0

        # Đếm số trẻ được thỏa mãn
        count = 0

        # Duyệt đến khi hết trẻ hoặc hết bánh
        while i < len(g) and j < len(s):

            # Nếu bánh đủ lớn cho trẻ hiện tại
            if s[j] >= g[i]:

                # Trẻ này được thỏa mãn
                count += 1

                # Sang trẻ tiếp theo
                i += 1

            # Dùng xong bánh hiện tại
            j += 1

        return count