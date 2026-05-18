class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """

        # hàm đổi thời gian HH:MM -> tổng số phút
        def to_minutes(t):

            # tách giờ và phút
            # ví dụ "02:30" -> ["02", "30"]
            h, m = map(int, t.split(":"))

            # đổi tất cả sang phút
            # 2 giờ 30 phút = 2*60 + 30
            return h * 60 + m

        # đổi current sang phút
        cur = to_minutes(current)

        # đổi correct sang phút
        cor = to_minutes(correct)

        # số phút cần tăng thêm
        diff = cor - cur

        # biến đếm số thao tác
        ops = 0

        # dùng greedy:
        # ưu tiên bước lớn trước
        for step in [60, 15, 5, 1]:

            # lấy được bao nhiêu lần step
            ops += diff // step

            # cập nhật số phút còn lại
            diff %= step

        # trả về số thao tác tối thiểu
        return ops