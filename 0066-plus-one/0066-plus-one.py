class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)

        # duyệt từ cuối mảng về đầu
        for i in range(n - 1, -1, -1):

            # nếu nhỏ hơn 9 → cộng 1 rồi return luôn
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # nếu là 9 → thành 0 (và carry sang trái)
            digits[i] = 0

        # nếu tất cả đều là 9 (ví dụ 999)
        return [1] + digits
