class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        score = [0] * (n + 1)  # đánh số từ 1 → n

        # xử lý quan hệ trust
        for a, b in trust:
            score[a] -= 1  # a tin người khác → không thể là judge
            score[b] += 1  # b được tin → tăng điểm

        # tìm người đạt điểm n-1
        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i

        return -1
        