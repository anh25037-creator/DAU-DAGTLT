class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """

        cycle = 2 * (n - 1)

        t = time % cycle

        # đang đi tới
        if t < n:
            return t + 1

        # đang đi lui
        return 2 * n - t - 1
        