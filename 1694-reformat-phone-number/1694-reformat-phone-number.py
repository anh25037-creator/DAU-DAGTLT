class Solution:
    def reformatNumber(self, number):

        # Chuỗi chỉ chứa các chữ số
        digits = ""

        # Duyệt từng ký tự trong number
        for ch in number:

            # Nếu là số thì thêm vào digits
            if ch.isdigit():
                digits += ch

        # Chuỗi kết quả cuối cùng
        result = ""

        # Biến i để đánh dấu vị trí đang xét
        i = 0

        # Lặp khi số chữ số còn lại lớn hơn 4
        while len(digits) - i > 4:

            # Lấy 3 chữ số từ vị trí i
            result += digits[i:i+3]

            # Thêm dấu "-"
            result += "-"

            # Di chuyển sang nhóm tiếp theo
            i += 3

        # Tính số chữ số còn lại
        remain = len(digits) - i

        # Nếu còn đúng 4 số
        if remain == 4:

            # Chia thành 2 nhóm 2 số
            result += digits[i:i+2]
            result += "-"
            result += digits[i+2:i+4]

        else:
            # Nếu còn 2 hoặc 3 số
            # Thêm trực tiếp vào kết quả
            result += digits[i:]

        # Trả về chuỗi đã format
        return result