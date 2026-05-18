class Solution:
    def isSameAfterReversals(self, num):
        # hàm đảo ngược một số nguyên
        def reverse(x):
            rev = 0

            # lặp cho đến khi hết chữ số
            while x > 0:
                digit = x % 10        # lấy chữ số cuối
                rev = rev * 10 + digit  # ghép vào số đảo
                x //= 10              # bỏ chữ số cuối

            return rev

        # bước 1: đảo lần 1
        reversed1 = reverse(num)

        # bước 2: đảo lần 2
        reversed2 = reverse(reversed1)

        # so sánh kết quả
        return reversed2 == num