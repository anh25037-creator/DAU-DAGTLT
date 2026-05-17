class Solution:
    def smallerNumbersThanCurrent(self, nums):

        # Mảng kết quả
        result = []

        # Duyệt từng phần tử trong nums
        for i in range(len(nums)):

            # Biến đếm số phần tử nhỏ hơn nums[i]
            count = 0

            # So sánh với tất cả phần tử khác
            for j in range(len(nums)):

                # Nếu nums[j] nhỏ hơn nums[i]
                if nums[j] < nums[i]:
                    count += 1

            # Thêm kết quả vào mảng
            result.append(count)

        # Trả về kết quả
        return result