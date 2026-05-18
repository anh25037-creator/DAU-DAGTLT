class Solution(object):
    def selfDividingNumbers(self, left, right):

        # danh sách lưu kết quả
        res = []

        # duyệt từng số từ left đến right
        for num in range(left, right + 1):

            # đổi số thành chuỗi
            # ví dụ: 128 -> "128"
            s = str(num)

            # nếu chứa số 0
            # thì không phải self-dividing
            if '0' in s:
                continue

            # giả sử ban đầu hợp lệ
            ok = True

            # duyệt từng ký tự trong chuỗi
            for ch in s:

                # đổi ký tự thành số
                # ví dụ: '8' -> 8
                d = int(ch)

                # nếu num không chia hết cho chữ số d
                # thì không hợp lệ
                if num % d != 0:
                    ok = False
                    break

            # nếu vẫn hợp lệ
            # thêm vào kết quả
            if ok:
                res.append(num)

        return res