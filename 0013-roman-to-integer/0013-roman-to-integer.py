class Solution:
    def romanToInt(self, s):

        # Bảng chuyển ký tự La Mã -> số nguyên
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Biến lưu kết quả cuối cùng
        total = 0

        # Duyệt từng ký tự trong chuỗi
        for i in range(len(s)):

            # Kiểm tra:
            # - chưa phải ký tự cuối
            # - giá trị hiện tại nhỏ hơn giá trị phía sau
            #
            # Ví dụ:
            # I đứng trước V -> IV = 4
            # X đứng trước C -> XC = 90
            #
            # Khi đó phải TRỪ
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:

                # Trừ giá trị hiện tại
                total -= roman[s[i]]

            else:
                # Ngược lại thì cộng bình thường
                total += roman[s[i]]

        # Trả về kết quả cuối
        return total