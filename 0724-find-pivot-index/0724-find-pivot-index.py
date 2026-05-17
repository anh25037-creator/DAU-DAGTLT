class Solution:
    def pivotIndex(self, nums):

        # Tổng toàn bộ mảng
        total = sum(nums)

        # Tổng bên trái
        leftSum = 0

        # Duyệt từng vị trí
        for i in range(len(nums)):

            # Tổng bên phải
            rightSum = total - leftSum - nums[i]

            # Nếu 2 bên bằng nhau
            if leftSum == rightSum:
                return i

            # Cập nhật tổng bên trái
            leftSum += nums[i]

        # Không có pivot index
        return -1