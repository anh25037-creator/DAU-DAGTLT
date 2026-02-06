class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        # Duyệt từng cặp phần tử
        for i in range(n):
            for j in range(i + 1, n):
                # Kiểm tra tổng của 2 số
                if nums[i] + nums[j] == target:
                    return [i, j]

