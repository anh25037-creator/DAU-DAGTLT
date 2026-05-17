class Solution:
    def distributeCandies(self, candies, num_people):

        # Tạo mảng kết quả ban đầu toàn 0
        result = [0] * num_people

        # Số kẹo sẽ phát ở lượt hiện tại
        give = 1

        # Vị trí người nhận
        i = 0

        # Khi vẫn còn kẹo
        while candies > 0:

            # Nếu số kẹo còn lại nhỏ hơn số cần phát
            if candies < give:

                # Đưa hết số kẹo còn lại
                result[i] += candies

                # Hết kẹo
                candies = 0

            else:
                # Phát kẹo bình thường
                result[i] += give

                # Trừ số kẹo đã phát
                candies -= give

            # Tăng số kẹo cho lượt sau
            give += 1

            # Chuyển sang người tiếp theo
            i = (i + 1) % num_people

        # Trả về kết quả
        return result