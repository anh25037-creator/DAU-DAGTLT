class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Số đá cần lấy ở lượt đầu tiên là 10
        take = 10

        # Biến theo dõi lượt chơi:
        # True  = đến lượt Alice
        # False = đến lượt Bob
        alice_turn = True

        # Chỉ tiếp tục khi còn đủ đá để lấy theo yêu cầu hiện tại
        while n >= take:

            # Lấy 'take' viên đá ra khỏi tổng
            n -= take

            # Sau mỗi lượt, số đá cần lấy giảm 1
            # Ví dụ: 10 → 9 → 8 → ...
            take -= 1

            # Đổi lượt chơi (Alice ↔ Bob)
            alice_turn = not alice_turn

        # Khi vòng lặp dừng:
        # người hiện tại KHÔNG thể lấy đá → thua

        # Vì ta đã đổi lượt ở cuối vòng,
        # nên người thua là người đang có lượt hiện tại
        # return not alice_turn để trả về người thắng (Alice thắng = True)
        return not alice_turn