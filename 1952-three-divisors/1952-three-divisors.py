class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # biến đếm số lượng ước
        count = 0

        # duyệt tất cả số từ 1 đến n
        for i in range(1, n + 1):

            # nếu n chia hết cho i
            # thì i là ước của n
            if n % i == 0:

                # tăng số lượng ước
                count += 1

        # nếu có đúng 3 ước
        # trả về True
        # ngược lại trả về False
        return count == 3