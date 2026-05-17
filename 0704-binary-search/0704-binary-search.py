class Solution:
    def search(self, nums, target):
        
        # con trỏ trái và phải
        left, right = 0, len(nums) - 1
        
        # lặp khi còn khoảng tìm kiếm
        while left <= right:
            
            # tìm vị trí giữa
            mid = (left + right) // 2
            
            # nếu tìm thấy target
            if nums[mid] == target:
                return mid
            
            # nếu giá trị giữa nhỏ hơn target → tìm bên phải
            elif nums[mid] < target:
                left = mid + 1
            
            # nếu lớn hơn target → tìm bên trái
            else:
                right = mid - 1
        
        # không tìm thấy
        return -1