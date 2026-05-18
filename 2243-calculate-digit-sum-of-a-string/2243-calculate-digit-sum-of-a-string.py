class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # lặp khi độ dài chuỗi còn lớn hơn k
        while len(s) > k:

            # lưu chuỗi mới sau mỗi round
            new_s = ""

            # chia chuỗi thành từng nhóm có size = k
            # bước nhảy là k
            for i in range(0, len(s), k):

                # lấy nhóm hiện tại
                # ví dụ:
                # s = "11111222223"
                # k = 3
                #
                # i = 0 -> "111"
                # i = 3 -> "112"
                # i = 6 -> "222"
                # i = 9 -> "23"
                group = s[i:i+k]

                # tính tổng chữ số trong group
                total = 0

                # duyệt từng ký tự trong group
                for ch in group:

                    # đổi ký tự thành số rồi cộng
                    # ví dụ:
                    # '3' -> 3
                    total += int(ch)

                # đổi total thành chuỗi
                # rồi nối vào new_s
                #
                # ví dụ:
                # total = 13
                # str(13) -> "13"
                new_s += str(total)

            # cập nhật s bằng chuỗi mới
            s = new_s

        # trả về kết quả cuối cùng
        return s