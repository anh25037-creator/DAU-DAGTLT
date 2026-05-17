class Solution:
    def maxProfit(self, prices):
        # giả sử giá đầu tiên là giá nhỏ nhất ban đầu
        min_price = prices[0]

        # lợi nhuận lớn nhất khởi tạo = 0 (không mua bán thì không lời)
        max_profit = 0

        # duyệt từng giá trong mảng
        for price in prices:

            # nếu gặp giá thấp hơn -> cập nhật giá mua tốt hơn
            if price < min_price:
                min_price = price

            else:
                # tính lợi nhuận nếu bán tại ngày này
                profit = price - min_price

                # cập nhật lợi nhuận lớn nhất
                if profit > max_profit:
                    max_profit = profit

        return max_profit