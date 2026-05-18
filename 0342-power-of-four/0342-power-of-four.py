class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # số <= 0 không phải lũy thừa của 4
        if n <= 0:
            return False

        # chia liên tục cho 4
        while n % 4 == 0:
            n //= 4

        # nếu cuối cùng còn 1
        # thì là lũy thừa của 4
        return n == 1