#Chuyển số La Mã thành số nguyên bình thường.
class Solution:
    def romanToInt(self, s):

        # Bảng đổi ký tự La Mã -> số
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        # Duyệt từng ký tự
        for i in range(len(s)):

            # Nếu chưa phải ký tự cuối
            # và số hiện tại nhỏ hơn số phía sau
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:

                # Trừ
                total -= roman[s[i]]

            else:
                # Cộng
                total += roman[s[i]]

        return total