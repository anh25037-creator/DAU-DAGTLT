class Solution:
    def minimumSum(self, num):

        # Chuyển số thành danh sách ký tự rồi sắp xếp tăng dần
        digits = sorted(str(num))

        # Tạo 2 số mới sao cho tổng nhỏ nhất
        new1 = int(digits[0] + digits[2])
        new2 = int(digits[1] + digits[3])

        # Trả về tổng
        return new1 + new2