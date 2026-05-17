class Solution:
    def merge(self, nums1, m, nums2, n):
        
        # i: con trỏ trỏ vào phần tử cuối của phần đã có trong nums1
        i = m - 1
        
        # j: con trỏ trỏ vào phần tử cuối của nums2
        j = n - 1
        
        # k: vị trí cuối cùng trong nums1 (nơi sẽ ghi kết quả)
        k = m + n - 1
        
        # duyệt khi cả nums1 (phần hợp lệ) và nums2 đều còn phần tử
        while i >= 0 and j >= 0:
            
            # so sánh 2 phần tử cuối của 2 mảng
            if nums1[i] > nums2[j]:
                
                # nếu nums1[i] lớn hơn → đưa vào vị trí k
                nums1[k] = nums1[i]
                
                # giảm i để xét phần tử tiếp theo của nums1
                i -= 1
            
            else:
                # nếu nums2[j] lớn hơn hoặc bằng
                nums1[k] = nums2[j]
                
                # giảm j để xét phần tử tiếp theo của nums2
                j -= 1
            
            # giảm k sau mỗi lần ghi
            k -= 1
        
        # nếu nums2 còn phần tử chưa xử lý
        while j >= 0:
            
            # copy nốt các phần tử còn lại của nums2 vào nums1
            nums1[k] = nums2[j]
            
            j -= 1
            k -= 1