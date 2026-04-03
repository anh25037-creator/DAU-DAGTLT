# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# The guess API is already defined for you.
# def guess(num: int) -> int:

# giả lập API (nếu bạn test local)
# giả lập hàm guess
def guess(num):
    pick = 6  # số cần đoán
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n):
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1


# chạy thử
s = Solution()
print(s.guessNumber(10))