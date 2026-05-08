class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        # chia liên tục cho 3
        while n % 3 == 0:
            n //= 3

        # còn 1 → đúng là 3^x
        return n == 1