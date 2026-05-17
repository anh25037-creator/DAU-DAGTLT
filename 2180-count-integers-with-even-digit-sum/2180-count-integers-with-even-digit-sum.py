class Solution:
    def countEven(self, num):
        # biến đếm số lượng số có tổng chữ số là số chẵn
        count = 0
        
        # duyệt tất cả các số từ 1 đến num
        for x in range(1, num + 1):
            
            # biến lưu tổng chữ số của số x
            s = 0
            
            # tạo bản sao của x để xử lý (không làm thay đổi x gốc)
            temp = x
            
            # tách từng chữ số của temp
            while temp > 0:
                
                # lấy chữ số cuối cùng của số
                digit = temp % 10
                s += digit   # cộng vào tổng chữ số
                
                # bỏ chữ số cuối để chuyển sang chữ số tiếp theo
                temp //= 10
            
            # sau khi tính xong tổng chữ số,
            # kiểm tra xem tổng đó có phải số chẵn không
            if s % 2 == 0:
                count += 1
        
        # trả về kết quả cuối cùng
        return count