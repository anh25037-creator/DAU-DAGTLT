class Solution:
    def searchInsert(self, nums, target):
        
        # con trỏ trái và phải
        left, right = 0, len(nums) - 1
        
        # binary search
        while left <= right:
            
            # tìm vị trí giữa
            mid = (left + right) // 2
            
            # nếu tìm thấy target → trả luôn index
            if nums[mid] == target:
                return mid
            
            # nếu mid nhỏ hơn target → tìm bên phải
            elif nums[mid] < target:
                left = mid + 1
            
            # nếu mid lớn hơn target → tìm bên trái
            else:
                right = mid - 1
        
        # nếu không tìm thấy:
        # left là vị trí cần chèn
        return left