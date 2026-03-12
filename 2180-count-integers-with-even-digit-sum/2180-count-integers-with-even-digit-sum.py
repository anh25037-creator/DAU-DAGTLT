class Solution:
    def countEven(self, num):
        count = 0
        
        for i in range(1, num + 1):
            s = sum(int(d) for d in str(i))
            if s % 2 == 0:
                count += 1
                
        return count