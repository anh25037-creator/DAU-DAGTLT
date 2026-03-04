class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        total = 0
        empty = 0
        
        while numBottles > 0:
            total += numBottles      # uống hết chai đầy
            empty += numBottles      # có thêm chai rỗng
            
            numBottles = empty // numExchange  # đổi được bao nhiêu chai mới
            empty = empty % numExchange        # còn lại chai rỗng
        
        return total