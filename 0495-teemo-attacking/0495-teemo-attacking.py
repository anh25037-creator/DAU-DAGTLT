class Solution:
    def findPoisonedDuration(self, timeSeries, duration):

        # Tổng thời gian bị trúng độc
        total = 0

        # Duyệt đến phần tử kế cuối
        for i in range(len(timeSeries) - 1):

            # Khoảng cách giữa 2 lần tấn công
            gap = timeSeries[i + 1] - timeSeries[i]

            # Nếu lần tấn công tiếp theo xảy ra
            # trước khi độc hết
            # thì chỉ cộng phần thời gian thực sự thêm vào
            total += min(gap, duration)

        # Cộng thêm duration của đòn cuối cùng
        total += duration

        return total