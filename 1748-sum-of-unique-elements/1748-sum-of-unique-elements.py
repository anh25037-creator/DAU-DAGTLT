class Solution:
    def sumOfUnique(self, nums):

        # Biến lưu tổng các số xuất hiện đúng 1 lần
        total = 0

        # Duyệt từng phần tử trong mảng
        for i in nums:

            # Nếu số i chỉ xuất hiện đúng 1 lần
            if nums.count(i) == 1:

                # Cộng vào tổng
                total += i

        # Trả về kết quả
        return total