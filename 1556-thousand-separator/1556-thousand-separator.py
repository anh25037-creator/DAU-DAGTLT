class Solution:
    def thousandSeparator(self, n):

        # Chuyển số thành chuỗi
        s = str(n)

        # Chuỗi kết quả
        result = ""

        # Biến đếm để chèn dấu chấm sau mỗi 3 số
        count = 0

        # Duyệt từ cuối chuỗi về đầu
        for i in range(len(s) - 1, -1, -1):

            # Thêm ký tự hiện tại vào đầu result
            result = s[i] + result

            count += 1

            # Nếu đủ 3 chữ số và chưa tới đầu chuỗi
            if count % 3 == 0 and i != 0:

                # Thêm dấu chấm
                result = "." + result

        # Trả về kết quả
        return result