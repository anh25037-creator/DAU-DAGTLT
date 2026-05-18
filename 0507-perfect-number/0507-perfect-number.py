class Solution(object):
    def checkPerfectNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # perfect number phải > 1
        # ví dụ: 1 không phải perfect number
        if n <= 1:
            return False

        # 1 luôn là ước của mọi số
        # nên cộng trước
        total = 1

        # bắt đầu kiểm tra từ 2
        i = 2

        # chỉ cần duyệt tới căn bậc 2 của n
        while i * i <= n:

            # nếu i chia hết cho n
            # nghĩa là i là ước
            if n % i == 0:

                # cộng i vào tổng
                total += i

                # tìm ước còn lại
                # ví dụ:
                # 28 // 2 = 14
                other = n // i

                # tránh cộng trùng
                # ví dụ:
                # 36 = 6 * 6
                if other != i:
                    total += other

            # tăng i để kiểm tra số tiếp theo
            i += 1

        # nếu tổng các ước
        # bằng chính n
        # thì là perfect number
        return total == n