class Solution:
    def findDifference(self, nums1, nums2):
        
        # chuyển nums1 thành set để loại bỏ phần tử trùng lặp
        # và tăng tốc độ tìm kiếm
        s1 = set(nums1)
        
        # chuyển nums2 thành set tương tự
        s2 = set(nums2)
        
        # s1 - s2: các phần tử chỉ có trong nums1
        # s2 - s1: các phần tử chỉ có trong nums2
        return [list(s1 - s2), list(s2 - s1)]