#Xóa các phần tử trùng lặp khỏi mảng đã được sắp xếp
class Solution:
    def removeElement(self, nums, val):
        
        # n là kích thước hiện tại của mảng hợp lệ
        n = len(nums)
        
        # i là con trỏ duyệt mảng
        i = 0
        
        # duyệt đến khi i vượt qua n
        while i < n:
            
            # nếu gặp phần tử cần xóa
            if nums[i] == val:
                
                # thay bằng phần tử cuối cùng trong vùng hợp lệ
                nums[i] = nums[n - 1]
                
                # giảm kích thước vùng hợp lệ
                n -= 1
            
            else:
                # chỉ tăng i khi phần tử không bị xóa
                i += 1
        
        # số phần tử còn lại
        return n