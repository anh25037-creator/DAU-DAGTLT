class Solution:
    # tìm số đứng ngay sau key nhiều lần nhất
    def mostFrequent(self, nums, key):
        
        # dictionary để đếm số lần xuất hiện của các target
        count = {}
        
        # duyệt mảng đến phần tử kế cuối (vì dùng i+1)
        for i in range(len(nums) - 1):
            
            # nếu gặp key tại vị trí i
            if nums[i] == key:
                
                # lấy phần tử ngay sau key
                target = nums[i + 1]
                
                # tăng số lần xuất hiện của target
                # nếu chưa có thì mặc định là 0
                count[target] = count.get(target, 0) + 1
        
        # tìm key có giá trị lớn nhất trong dictionary count
        # (trả về target xuất hiện nhiều nhất sau key)
        return max(count, key=count.get)