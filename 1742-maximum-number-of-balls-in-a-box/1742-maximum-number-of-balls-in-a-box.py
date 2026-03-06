class Solution:
    def countBalls(self, lowLimit, highLimit):
        box = {}

        for i in range(lowLimit, highLimit + 1):
            s = sum(int(d) for d in str(i))  # tổng chữ số
            
            if s in box:
                box[s] += 1
            else:
                box[s] = 1

        return max(box.values())