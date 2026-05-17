class Solution:
    def secondHighest(self, s):

        # Tạo set để lưu các chữ số khác nhau
        digits = set()

        # Duyệt từng ký tự trong chuỗi
        for ch in s:

            # Nếu ký tự là số
            if ch.isdigit():

                # Chuyển sang int rồi thêm vào set
                digits.add(int(ch))

        # Nếu có ít hơn 2 chữ số khác nhau
        if len(digits) < 2:
            return -1

        # Sắp xếp giảm dần
        digits = sorted(digits, reverse=True)

        # Trả về số lớn thứ hai
        return digits[1]