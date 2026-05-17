class Solution:
    def divideArray(self, nums):
        
        # import Counter để đếm tần suất các phần tử trong mảng
        from collections import Counter
        
        # đếm số lần xuất hiện của từng phần tử
        count = Counter(nums)
        
        # duyệt qua tất cả giá trị tần suất
        for v in count.values():
            
            # nếu có phần tử xuất hiện số lần lẻ
            # thì không thể chia thành các cặp
            if v % 2 != 0:
                return False
        
        # nếu tất cả đều xuất hiện chẵn lần
        return True