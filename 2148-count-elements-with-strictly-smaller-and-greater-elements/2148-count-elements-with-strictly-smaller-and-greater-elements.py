class Solution:
    def countElements(self, nums):

        # Tìm phần tử nhỏ nhất trong mảng
        mn = min(nums)

        # Tìm phần tử lớn nhất trong mảng
        mx = max(nums)

        # Biến đếm kết quả
        count = 0

        # Duyệt từng phần tử trong mảng
        for x in nums:

            # Nếu x lớn hơn số nhỏ nhất
            # và nhỏ hơn số lớn nhất
            if mn < x < mx:

                # Tăng biến đếm
                count += 1

        # Trả về kết quả
        return count