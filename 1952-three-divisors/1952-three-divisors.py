import math

class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        root = int(math.sqrt(n))

        # không phải số chính phương
        if root * root != n:
            return False

        # kiểm tra root có nguyên tố không
        if root < 2:
            return False

        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                return False

        return True
        