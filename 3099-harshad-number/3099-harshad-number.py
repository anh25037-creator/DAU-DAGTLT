class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """

        total = 0
        temp = x

        # tính tổng chữ số
        while temp > 0:
            total += temp % 10
            temp //= 10

        # kiểm tra Harshad
        if x % total == 0:
            return total

        return -1