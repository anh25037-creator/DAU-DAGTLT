class Solution:
    def isHappy(self, n):
        # lưu các số đã xuất hiện để phát hiện chu trình
        seen = set()

        while n != 1:
            # nếu số này đã xuất hiện → bị lặp vòng → không phải happy number
            if n in seen:
                return False
            
            # đánh dấu đã gặp
            seen.add(n)

            # tính tổng bình phương các chữ số
            total = 0
            while n > 0:
                digit = n % 10        # lấy chữ số cuối
                total += digit * digit  # bình phương và cộng vào tổng
                n //= 10              # bỏ chữ số cuối

            # cập nhật n thành giá trị mới
            n = total

        # nếu thoát vòng lặp do n == 1 → happy number
        return True
        