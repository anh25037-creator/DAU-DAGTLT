class Solution:
    def findContentChildren(self, g, s):
        g.sort()  # sắp xếp độ tham
        s.sort()  # sắp xếp kích thước bánh
        
        child = 0
        cookie = 0
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1   # trẻ này được thoả mãn
            cookie += 1      # chuyển sang bánh tiếp theo
        
        return child