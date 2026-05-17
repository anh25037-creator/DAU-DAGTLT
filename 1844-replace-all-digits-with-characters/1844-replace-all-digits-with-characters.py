class Solution:
    def replaceDigits(self, s):

        # Chuyển chuỗi thành list để dễ thay đổi ký tự
        s = list(s)

        # Duyệt các vị trí lẻ
        for i in range(1, len(s), 2):

            # Ký tự đứng trước
            ch = s[i - 1]

            # Số cần dịch
            x = int(s[i])

            # Dịch ký tự bằng mã ASCII
            s[i] = chr(ord(ch) + x)

        # Ghép list thành chuỗi
        return "".join(s)