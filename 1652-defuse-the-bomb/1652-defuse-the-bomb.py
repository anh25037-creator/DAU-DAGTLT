class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        n = len(code)

        # mảng kết quả, ban đầu toàn 0
        res = [0] * n

        # nếu k = 0 → tất cả đều là 0
        if k == 0:
            return res

        # duyệt từng vị trí i trong mảng
        for i in range(n):

            total = 0  # tổng cho vị trí i

            # ===== CASE 1: k > 0 =====
            if k > 0:
                # lấy k phần tử phía SAU i
                for j in range(1, k + 1):
                    # (i + j) % n để quay vòng mảng
                    total += code[(i + j) % n]

            # ===== CASE 2: k < 0 =====
            else:
                # lấy -k phần tử phía TRƯỚC i
                for j in range(1, -k + 1):
                    # (i - j) % n để quay vòng mảng
                    total += code[(i - j) % n]

            # gán kết quả cho vị trí i
            res[i] = total

        return res