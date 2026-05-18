class Solution:
    def singleNumber(self, nums):
        # khởi tạo biến XOR = 0
        res = 0

        # duyệt từng số trong mảng
        for num in nums:
            # XOR dồn tất cả lại
            res ^= num

        # kết quả còn lại là số xuất hiện 1 lần
        return res