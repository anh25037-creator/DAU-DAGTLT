class Solution:
    def countBalls(self, lowLimit, highLimit):

        # Dictionary lưu số lượng bóng trong từng hộp
        box = {}

        # Duyệt các số từ lowLimit đến highLimit
        for i in range(lowLimit, highLimit + 1):

            # Tính tổng các chữ số của i
            s = sum(int(d) for d in str(i))

            # Nếu hộp đã tồn tại
            if s in box:
                box[s] += 1

            # Nếu hộp chưa tồn tại
            else:
                box[s] = 1

        # Trả về số bóng lớn nhất trong các hộp
        return max(box.values())