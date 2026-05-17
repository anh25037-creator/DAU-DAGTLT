class Solution:
    def numJewelsInStones(self, jewels, stones):

        # Đưa jewels vào set để tìm kiếm nhanh
        jewelSet = set(jewels)

        # Đếm số viên đá là jewels
        count = 0

        # Duyệt từng viên đá
        for stone in stones:

            # Nếu viên đá thuộc loại jewel
            if stone in jewelSet:
                count += 1

        return count