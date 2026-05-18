class Solution:
    def missingNumber(self, nums):
        # n là số phần tử trong mảng
        # vì mảng có n phần tử nhưng giá trị nằm trong [0, n]
        n = len(nums)

        # Tổng của dãy số liên tiếp từ 0 đến n
        # công thức: n * (n + 1) / 2
        total = n * (n + 1) // 2

        # sum(nums) là tổng các số thực sự có trong mảng
        # số bị thiếu = tổng đầy đủ - tổng hiện có
        return total - sum(nums)
        