class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """

        take = 10      # số đá cần lấy
        alice_turn = True

        while n >= take:
            n -= take
            take -= 1

            # đổi lượt
            alice_turn = not alice_turn

        # nếu đến đây mà tới lượt Bob không đi được
        # nghĩa là Alice thắng
        return not alice_turn