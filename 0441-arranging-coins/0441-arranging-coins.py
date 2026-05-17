class Solution:
    def arrangeCoins(self, n):
        
        # i là số coin cần cho hàng hiện tại (hàng 1, 2, 3, ...)
        i = 1
        
        # tiếp tục xây hàng khi còn đủ coin
        while n >= i:
            
            # dùng i coin để xây hàng hiện tại
            n = n - i
            
            # tăng số coin cần cho hàng tiếp theo
            i += 1
        
        # i đã vượt quá số hàng xây được
        # nên kết quả là i - 1
        return i - 1