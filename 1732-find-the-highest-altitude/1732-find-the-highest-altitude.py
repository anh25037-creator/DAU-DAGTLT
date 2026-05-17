class Solution:
    def largestAltitude(self, gain):

        # Độ cao hiện tại
        altitude = 0

        # Độ cao lớn nhất
        highest = 0

        # Duyệt từng độ tăng/giảm độ cao
        for g in gain:

            # Cập nhật độ cao hiện tại
            altitude += g

            # Nếu độ cao hiện tại lớn hơn highest
            if altitude > highest:
                highest = altitude

        # Trả về độ cao lớn nhất
        return highest