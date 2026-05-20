#Cộng thêm 1
class Solution(object):
    def plusOne(self, digits):
        """
        digits: mảng các chữ số của một số nguyên lớn
        ví dụ: [1,2,3] đại diện cho số 123
        """

        n = len(digits)  # lấy độ dài mảng

        # duyệt từ phải sang trái (từ hàng đơn vị → hàng cao hơn)
        for i in range(n - 1, -1, -1):

            # digits[i] là chữ số tại vị trí i

            # ví dụ:
            # digits = [1,2,3]
            # index:     0 1 2
            # value:     1 2 3
            # nên digits[2] = 3 (hàng đơn vị)

            if digits[i] < 9:
                # nếu chữ số < 9 thì chỉ cần +1 là xong
                digits[i] += 1
                return digits  # trả luôn vì không có nhớ (carry)

            # nếu chữ số = 9:
            # 9 + 1 = 10 → ghi 0, nhớ 1 sang trái
            digits[i] = 0

        # nếu tất cả đều là 9 (vd: [9,9,9])
        # sau khi cộng sẽ thành [0,0,0]
        # phải thêm 1 ở đầu → [1,0,0,0]
        return [1] + digits