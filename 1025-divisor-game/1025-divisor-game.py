class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # nếu n là số chẵn -> Alice thắng
        # nếu n là số lẻ -> Alice thua
        return n % 2 == 0