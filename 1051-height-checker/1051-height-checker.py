class Solution:
    def heightChecker(self, heights):
        
        # Sắp xếp mảng heights để tạo thứ tự đúng
        expected = sorted(heights)

        # Biến đếm số vị trí sai
        count = 0

        # Duyệt từng vị trí trong mảng
        for i in range(len(heights)):

            # Nếu chiều cao hiện tại khác chiều cao mong đợi
            if heights[i] != expected[i]:

                # Tăng biến đếm
                count += 1

        # Trả về số vị trí sai
        return count