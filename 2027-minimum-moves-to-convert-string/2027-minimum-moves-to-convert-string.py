class Solution(object):
    def minimumMoves(self, s):
        # moves: đếm số lần thực hiện thao tác biến 3 ký tự thành 'O'
        moves = 0

        # i: con trỏ duyệt chuỗi từ trái sang phải
        i = 0

        # duyệt toàn bộ chuỗi
        while i < len(s):

            # nếu gặp ký tự 'X' → cần thực hiện 1 move
            if s[i] == 'X':

                # tăng số lần thao tác
                moves += 1

                # bỏ qua 3 ký tự liên tiếp vì 1 move xử lý được 3 ký tự
                i += 3

            else:
                # nếu là 'O' → không cần xử lý, chỉ đi tiếp
                i += 1

        # trả về tổng số move tối thiểu
        return moves