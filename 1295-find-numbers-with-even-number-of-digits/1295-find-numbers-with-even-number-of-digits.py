class Solution:
    def findNumbers(self, nums):

        # Biến đếm số phần tử có số chữ số chẵn
        count = 0

        # Duyệt từng số trong mảng
        for num in nums:

            # Chuyển số thành chuỗi để đếm số chữ số
            digits = len(str(num))

            # Nếu số chữ số là chẵn
            if digits % 2 == 0:
                count += 1

        # Trả về kết quả
        return count