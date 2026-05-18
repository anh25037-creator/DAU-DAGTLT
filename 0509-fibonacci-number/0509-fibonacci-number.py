class Solution:
    def fib(self, n):
        # trường hợp cơ bản
        if n == 0:
            return 0
        if n == 1:
            return 1

        # f0 = F(0), f1 = F(1)
        f0, f1 = 0, 1

        # tính từ F(2) đến F(n)
        for i in range(2, n + 1):
            # lưu giá trị mới = tổng 2 số trước
            f0, f1 = f1, f0 + f1

        # f1 là kết quả cuối cùng F(n)
        return f1