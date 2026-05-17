class Solution:
    def maxDistance(self, colors):

        # Biến lưu khoảng cách lớn nhất
        max_distance = 0

        # Duyệt từng nhà
        for i in range(len(colors)):

            # So sánh với các nhà phía sau
            for j in range(i + 1, len(colors)):

                # Nếu màu khác nhau
                if colors[i] != colors[j]:

                    # Tính khoảng cách
                    distance = abs(i - j)

                    # Cập nhật khoảng cách lớn nhất
                    max_distance = max(max_distance, distance)

        # Trả về kết quả
        return max_distance