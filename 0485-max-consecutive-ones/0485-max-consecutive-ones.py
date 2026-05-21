#Tìm chuỗi dài nhất các số 1 liên tiếp trong mảng nhị phân nums.
class Solution:
    def findMaxConsecutiveOnes(self, nums):

        # Đếm số lượng số 1 liên tiếp hiện tại
        count = 0

        # Lưu kết quả lớn nhất
        maximum = 0

        # Duyệt từng phần tử trong mảng
        for num in nums:

            # Nếu gặp số 1
            if num == 1:

                # Tăng số lượng liên tiếp
                count += 1

                # Cập nhật giá trị lớn nhất
                maximum = max(maximum, count)

            else:
                # Nếu gặp số 0
                # reset lại số lượng liên tiếp
                count = 0

        return maximum