class Solution:
    def findJudge(self, n, trust):

        # Mảng score dùng để theo dõi:
        # +1: người này được người khác tin (in-degree)
        # -1: người này tin người khác (out-degree)
        score = [0] * (n + 1)

        # Duyệt từng cặp (a, b)
        # a tin b
        for a, b in trust:

            # a tin người khác → không thể là judge → trừ 1
            score[a] -= 1

            # b được người khác tin → tăng 1
            score[b] += 1

        # Duyệt tất cả người từ 1 → n
        for i in range(1, n + 1):

            # Judge phải được tất cả người khác tin:
            # => score[i] = n - 1
            # (vì có n-1 người còn lại đều tin i)
            if score[i] == n - 1:
                return i

        # Không tìm thấy judge hợp lệ
        return -1