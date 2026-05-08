class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        single_sum = 0
        double_sum = 0

        for num in nums:

            # số 1 chữ số
            if num < 10:
                single_sum += num

            # số 2 chữ số
            elif 10 <= num < 100:
                double_sum += num

        total = sum(nums)

        return (
            single_sum > total - single_sum or
            double_sum > total - double_sum
        )
        