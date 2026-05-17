class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """

        # Sắp xếp mảng giá theo thứ tự tăng dần
        # để lấy được 2 món rẻ nhất dễ dàng
        prices.sort()

        # Tổng chi phí của 2 viên chocolate rẻ nhất
        cost = prices[0] + prices[1]

        # Nếu đủ tiền mua 2 viên chocolate
        if cost <= money:
            # trả về số tiền còn lại sau khi mua
            return money - cost

        # Nếu không đủ tiền mua 2 viên
        # thì không mua được → trả lại toàn bộ tiền ban đầu
        return money
        