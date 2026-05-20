#Tổng của hai số
#Tìm vị trí (index) của 2 số trong mảng sao cho tổng của chúng bằng target.
class Solution:
    def twoSum(self, nums, target):
        
        # Dictionary dùng để lưu:
        # số trong mảng -> vị trí(index) của số đó
        seen = {}
        
        # Duyệt từng phần tử trong mảng
        for i in range(len(nums)):
            
            # Tính số cần tìm để cộng lại bằng target
            need = target - nums[i]
            
            # Nếu số cần tìm đã xuất hiện trước đó
            if need in seen:
                
                # Trả về vị trí của:
                # - số đã lưu trước đó
                # - số hiện tại
                return [seen[need], i]
            
            # Lưu số hiện tại và vị trí của nó vào dictionary
            seen[nums[i]] = i