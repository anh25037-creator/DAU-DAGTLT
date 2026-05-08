class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """

        # đổi HH:MM -> phút
        def to_minutes(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        cur = to_minutes(current)
        cor = to_minutes(correct)

        diff = cor - cur

        ops = 0

        # greedy
        for step in [60, 15, 5, 1]:
            ops += diff // step
            diff %= step

        return ops