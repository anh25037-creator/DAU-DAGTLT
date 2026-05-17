class Solution:
    def findDisappearedNumbers(self, nums):

        # Set dùng để lưu các số xuất hiện trong nums
        seen = set(nums)

        # Mảng kết quả
        result = []

        # Duyệt từ 1 đến n
        for i in range(1, len(nums) + 1):

            # Nếu số i không xuất hiện trong nums
            if i not in seen:

                # Thêm vào kết quả
                result.append(i)

        return result