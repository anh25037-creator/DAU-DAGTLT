class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """

        # Chu kỳ đầy đủ của chuyển động:
        # đi từ 1 → n rồi quay ngược lại n → 1
        # tổng độ dài = 2 * (n - 1)
        cycle = 2 * (n - 1)

        # Lấy thời gian thực tế trong 1 chu kỳ
        # giúp tránh xử lý các vòng lặp dư thừa
        t = time % cycle

        # Trường hợp đang đi xuôi (1 → n)
        # trong đoạn đầu của chu kỳ
        if t < n:
            # vị trí bắt đầu từ 1 nên +1
            return t + 1

        # Trường hợp đang đi ngược (n → 1)
        # công thức biến đổi từ chuỗi quay ngược
        return 2 * n - t - 1
        