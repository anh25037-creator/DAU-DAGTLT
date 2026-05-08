class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        # tổng từ 0 đến n
        total = n * (n + 1) // 2

        # tổng thực tế của mảng
        actual = sum(nums)

        # phần thiếu
        return total - actual
        