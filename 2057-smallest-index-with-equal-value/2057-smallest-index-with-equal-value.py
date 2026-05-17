class Solution:
    def smallestEqual(self, nums):

        # Duyệt từng vị trí trong mảng
        for i in range(len(nums)):

            # Kiểm tra i mod 10 có bằng nums[i] không
            if i % 10 == nums[i]:

                # Trả về vị trí đầu tiên thỏa điều kiện
                return i

        # Nếu không tìm thấy
        return -1