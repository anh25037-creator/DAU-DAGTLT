class Solution:
    def isValid(self, s):
        
        # stack để lưu các dấu ngoặc mở
        stack = []
        
        # mapping dấu đóng -> dấu mở tương ứng
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # duyệt từng ký tự trong chuỗi
        for c in s:
            
            # nếu là dấu đóng
            if c in pairs:
                
                # nếu stack rỗng hoặc không khớp loại ngoặc
                if not stack or stack[-1] != pairs[c]:
                    return False
                
                # nếu khớp thì pop dấu mở
                stack.pop()
            
            else:
                # nếu là dấu mở thì push vào stack
                stack.append(c)
        
        # hợp lệ nếu stack rỗng
        return len(stack) == 0