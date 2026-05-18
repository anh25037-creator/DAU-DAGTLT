class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        # lặp đến khi num chỉ còn 1 chữ số
        while num >= 10:

            total = 0

            # tách từng chữ số để cộng
            while num > 0:
                total += num % 10   # lấy chữ số cuối
                num //= 10          # bỏ chữ số cuối

            # cập nhật num bằng tổng mới
            num = total

        return num