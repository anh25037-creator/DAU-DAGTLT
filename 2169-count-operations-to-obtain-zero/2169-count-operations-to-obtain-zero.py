class Solution:
    def countOperations(self, num1, num2):

        # Biến đếm số thao tác
        count = 0

        # Lặp khi cả num1 và num2 khác 0
        while num1 and num2:

            # Nếu num1 lớn hơn num2
            if num1 > num2:

                # Lấy num1 trừ num2
                num1 -= num2

            else:
                # Ngược lại lấy num2 trừ num1
                num2 -= num1

            # Tăng số lần thao tác
            count += 1

        # Trả về kết quả
        return count