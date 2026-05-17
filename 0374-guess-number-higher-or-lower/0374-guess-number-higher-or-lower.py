# API guess đã được định nghĩa sẵn trong bài
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        
        # left và right là khoảng tìm kiếm ban đầu [1, n]
        left, right = 1, n
        
        # tiếp tục tìm khi khoảng tìm kiếm còn hợp lệ
        while left <= right:
            
            # chọn số ở giữa để đoán
            mid = (left + right) // 2
            
            # gọi API để kiểm tra mid
            res = guess(mid)
            
            # nếu đoán đúng số cần tìm
            if res == 0:
                return mid
            
            # nếu res = 1 → số cần tìm lớn hơn mid
            elif res == 1:
                left = mid + 1  # bỏ nửa bên trái
            
            # nếu res = -1 → số cần tìm nhỏ hơn mid
            else:
                right = mid - 1  # bỏ nửa bên phải