class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # i trỏ vào cuối chuỗi a
        i = len(a) - 1

        # j trỏ vào cuối chuỗi b
        j = len(b) - 1

        # biến nhớ khi cộng nhị phân
        carry = 0

        # lưu kết quả từng bit
        result = []

        # lặp khi:
        # - a còn ký tự
        # - b còn ký tự
        # - hoặc còn số nhớ
        while i >= 0 or j >= 0 or carry:

            # bắt đầu với giá trị nhớ
            total = carry

            # nếu a còn bit
            if i >= 0:

                # ord('0') = 48
                # ord('1') = 49
                # lấy giá trị số của ký tự
                total += ord(a[i]) - ord('0')

                # dịch sang trái
                i -= 1

            # nếu b còn bit
            if j >= 0:

                # chuyển ký tự thành số
                total += ord(b[j]) - ord('0')

                # dịch sang trái
                j -= 1

            # lấy bit hiện tại
            # nếu total là:
            # 0 -> thêm 0
            # 1 -> thêm 1
            # 2 -> thêm 0
            # 3 -> thêm 1
            result.append(str(total % 2))

            # cập nhật số nhớ
            # 0 hoặc 1
            carry = total // 2

        # kết quả đang bị ngược
        # nên đảo lại rồi nối thành chuỗi
        return ''.join(reversed(result))