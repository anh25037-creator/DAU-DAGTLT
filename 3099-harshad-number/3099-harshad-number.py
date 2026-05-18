class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """

        # total dùng để lưu tổng các chữ số
        total = 0

        # temp là biến phụ để tách từng chữ số
        # giữ nguyên x ban đầu để còn kiểm tra
        temp = x

        # lặp cho đến khi temp = 0
        while temp > 0:

            # temp % 10 lấy chữ số cuối cùng
            # ví dụ: 172 % 10 = 2
            total += temp % 10

            # temp //= 10 để bỏ chữ số cuối
            # ví dụ: 172 // 10 = 17
            temp //= 10

        # kiểm tra số Harshad
        # số Harshad là số chia hết cho tổng chữ số của nó
        if x % total == 0:

            # nếu chia hết → trả về tổng chữ số
            return total

        # nếu không chia hết → không phải Harshad
        return -1