class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # số <= 0 không thể là lũy thừa của 2
        if n <= 0:
            return False

        # chia liên tục cho 2
        while n % 2 == 0:
            n //= 2

        # nếu cuối cùng còn 1
        # thì n là lũy thừa của 2
        return n == 1