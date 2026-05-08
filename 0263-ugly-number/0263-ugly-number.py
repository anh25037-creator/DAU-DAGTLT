class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        # loại bỏ hết thừa số 2
        while n % 2 == 0:
            n //= 2

        # loại bỏ hết thừa số 3
        while n % 3 == 0:
            n //= 3

        # loại bỏ hết thừa số 5
        while n % 5 == 0:
            n //= 5

        # nếu còn lại 1 → chỉ có 2,3,5
        return n == 1
        