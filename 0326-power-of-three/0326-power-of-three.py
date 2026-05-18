class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # số <= 0 không phải lũy thừa của 3
        if n <= 0:
            return False

        # chia liên tục cho 3
        while n % 3 == 0:
            n //= 3

        # nếu cuối cùng còn 1
        # thì là lũy thừa của 3
        return n == 1