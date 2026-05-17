class Solution:
    def removeDuplicates(self, nums):
        
        # k là vị trí để ghi phần tử unique tiếp theo
        k = 0
        
        # duyệt từng phần tử trong mảng
        for n in nums:
            
            # nếu đây là phần tử đầu tiên
            # hoặc khác với phần tử cuối cùng đã lưu
            if k == 0 or n != nums[k - 1]:
                
                # ghi n vào vị trí k
                nums[k] = n
                
                # tăng vị trí lưu
                k += 1
        
        # trả về số lượng phần tử unique
        return k