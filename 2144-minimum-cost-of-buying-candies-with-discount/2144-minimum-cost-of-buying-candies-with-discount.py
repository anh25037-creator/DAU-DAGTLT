class Solution:
    def minimumCost(self, cost):

        # Sắp xếp giảm dần
        cost.sort(reverse=True)

        # Tổng tiền cần trả
        total = 0

        # Duyệt từng viên kẹo
        for i in range(len(cost)):

            # Mỗi viên thứ 3 sẽ được miễn phí
            if (i + 1) % 3 != 0:

                # Cộng tiền
                total += cost[i]

        # Trả về kết quả
        return total