class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # số <= 0 không phải power of 2
        if n <= 0:
            return False

        # kiểm tra chỉ có 1 bit 1
        return (n & (n - 1)) == 0