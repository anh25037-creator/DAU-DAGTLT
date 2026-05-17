class Solution:
    def findClosestNumber(self, nums):
        
        # giả sử phần tử đầu tiên là đáp án tạm thời
        ans = nums[0]
        
        # duyệt từng phần tử trong mảng
        for x in nums:
            
            # so sánh theo 2 tiêu chí:
            # 1. |x| nhỏ hơn |ans| → x gần 0 hơn
            # 2. nếu |x| bằng nhau → chọn số lớn hơn
            if abs(x) < abs(ans) or (abs(x) == abs(ans) and x > ans):
                ans = x
                
        # trả về số gần 0 nhất (theo điều kiện đề bài)
        return ans