class Solution:
    def timeRequiredToBuy(self, tickets, k):

        # Biến lưu tổng thời gian
        time = 0

        # Duyệt từng người trong hàng
        for i in range(len(tickets)):

            # Nếu người đứng trước hoặc chính k
            if i <= k:

                # Người này có thể mua tối đa tickets[k] vé
                time += min(tickets[i], tickets[k])

            else:
                # Người đứng sau k
                # Chỉ mua tối đa tickets[k] - 1 vé
                time += min(tickets[i], tickets[k] - 1)

        # Trả về tổng thời gian
        return time