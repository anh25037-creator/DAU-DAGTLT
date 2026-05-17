class Solution:
    def romanToInt(self, s):

        # Dictionary lưu giá trị của từng ký tự La Mã
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Kết quả cuối cùng
        total = 0

        # Duyệt từng ký tự trong chuỗi
        for i in range(len(s)):

            # Nếu ký tự hiện tại nhỏ hơn ký tự phía sau
            # nghĩa là trường hợp trừ (IV, IX, XL,...)
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:

                # Trừ giá trị hiện tại
                total -= values[s[i]]

            else:
                # Ngược lại thì cộng bình thường
                total += values[s[i]]

        return total