class Solution:
    def sumZero(self, n):

        # Mảng kết quả
        result = []

        # Thêm các cặp số đối nhau
        for i in range(1, n // 2 + 1):
            result.append(i)    # số dương
            result.append(-i)   # số âm

        # Nếu n lẻ thì thêm số 0
        if n % 2 == 1:
            result.append(0)

        # Trả về kết quả
        return result