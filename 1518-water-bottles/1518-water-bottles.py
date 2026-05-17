class Solution:
    def numWaterBottles(self, numBottles, numExchange):

        # Tổng số chai nước đã uống
        total = 0

        # Số chai rỗng hiện có
        empty = 0

        # Khi vẫn còn chai nước đầy
        while numBottles > 0:

            # Uống hết các chai hiện tại
            total += numBottles

            # Sau khi uống sẽ có chai rỗng
            empty += numBottles

            # Đổi chai rỗng lấy chai đầy mới
            numBottles = empty // numExchange

            # Số chai rỗng còn dư sau khi đổi
            empty = empty % numExchange

        # Trả về tổng số chai đã uống
        return total