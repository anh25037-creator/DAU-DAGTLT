class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # hàm đảo số
        def reverse(x):
            rev = 0
            while x > 0:
                rev = rev * 10 + x % 10
                x //= 10
            return rev

        reversed1 = reverse(num)
        reversed2 = reverse(reversed1)

        return reversed2 == num
        