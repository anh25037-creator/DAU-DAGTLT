class Solution:
    def checkValid(self, matrix):

        # Kích thước ma trận
        n = len(matrix)

        # Tập hợp chuẩn chứa các số từ 1 -> n
        valid = set(range(1, n + 1))

        # Kiểm tra từng hàng
        for row in matrix:

            # Nếu hàng không chứa đủ các số từ 1 -> n
            if set(row) != valid:
                return False

        # Kiểm tra từng cột
        for col in range(n):

            # Tạo danh sách chứa các phần tử của cột
            column = []

            for row in range(n):
                column.append(matrix[row][col])

            # Nếu cột không hợp lệ
            if set(column) != valid:
                return False

        # Nếu tất cả đều hợp lệ
        return True