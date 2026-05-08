class Solution(object):
    def checkPerfectNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 1:
            return False

        total = 1  # 1 luôn là ước của mọi số > 1

        # duyệt đến sqrt(n)
        i = 2
        while i * i <= n:
            if n % i == 0:
                total += i

                # thêm ước đối xứng
                if i != n // i:
                    total += n // i

            i += 1

        return total == n