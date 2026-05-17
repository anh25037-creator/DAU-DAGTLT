class Solution:
    def countPairs(self, nums, k):
        # lấy độ dài mảng
        n = len(nums)
        
        # biến đếm số cặp hợp lệ
        count = 0
        
        # duyệt từng chỉ số i
        for i in range(n):
            # duyệt các chỉ số j phía sau i để đảm bảo i < j
            for j in range(i + 1, n):
                
                # kiểm tra 2 điều kiện:
                # 1. nums[i] phải bằng nums[j]
                # 2. tích i * j chia hết cho k
                if nums[i] == nums[j] and (i * j) % k == 0:
                    
                    # nếu thỏa mãn thì tăng biến đếm
                    count += 1
        
        # trả về kết quả cuối cùng
        return count