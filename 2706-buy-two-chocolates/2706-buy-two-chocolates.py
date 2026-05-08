class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """

        # tìm 2 giá nhỏ nhất
        prices.sort()

        cost = prices[0] + prices[1]

        # đủ tiền mua
        if cost <= money:
            return money - cost

        # không đủ tiền
        return money
        