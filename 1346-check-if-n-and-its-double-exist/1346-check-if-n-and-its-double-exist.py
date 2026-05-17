class Solution:
    def checkIfExist(self, arr):
        
        # set lưu các số đã gặp
        seen = set()
        
        # duyệt từng phần tử
        for x in arr:
            
            # kiểm tra 2 trường hợp:
            # 1. x là gấp đôi của số trước đó
            # 2. x là một nửa của số trước đó
            if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            
            # thêm x vào set
            seen.add(x)
        
        # không tìm thấy cặp hợp lệ
        return False