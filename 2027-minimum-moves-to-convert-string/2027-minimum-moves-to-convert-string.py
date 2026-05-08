class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        moves = 0
        n = len(s)

        while i < n:
            if s[i] == 'X':
                moves += 1      # thực hiện 1 lần biến đổi
                i += 3          # bỏ qua 3 ký tự
            else:
                i += 1

        return moves