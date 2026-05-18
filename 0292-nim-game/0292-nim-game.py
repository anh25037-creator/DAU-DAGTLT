class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # nếu n chia hết cho 4
        # thì sẽ thua
        return n % 4 != 0