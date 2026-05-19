class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # lưu tổng các số có 1 chữ số
        single_sum = 0

        # lưu tổng các số có 2 chữ số
        double_sum = 0

        # duyệt từng phần tử trong mảng nums
        for num in nums:

            # nếu là số 1 chữ số (0 -> 9)
            if num < 10:
                single_sum += num

            # nếu là số 2 chữ số (10 -> 99)
            elif 10 <= num < 100:
                double_sum += num

        # tính tổng tất cả phần tử trong mảng
        total = sum(nums)

        # Alice thắng nếu:
        # - chọn nhóm số 1 chữ số mà tổng lớn hơn phần còn lại
        # HOẶC
        # - chọn nhóm số 2 chữ số mà tổng lớn hơn phần còn lại

        return (
            single_sum > total - single_sum or
            double_sum > total - double_sum
        )