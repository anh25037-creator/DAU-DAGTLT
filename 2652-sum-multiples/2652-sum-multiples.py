class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """

        # lưu tổng kết quả
        total = 0

        # duyệt từ 1 -> n
        for i in range(1, n + 1):

            # nếu chia hết cho 3 hoặc 5 hoặc 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:

                # cộng vào tổng
                total += i

        return total