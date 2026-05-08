class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()  # lưu các số đã gặp

        while n != 1:
            # nếu đã gặp rồi → có chu trình → không phải happy
            if n in seen:
                return False

            seen.add(n)

            # tính tổng bình phương các chữ số
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True
        