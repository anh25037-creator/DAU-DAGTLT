class Solution:
    def removeDuplicates(self, s):
        
        # stack để lưu kết quả tạm thời
        stack = []
        
        # duyệt từng ký tự trong chuỗi
        for c in s:
            
            # nếu stack không rỗng và ký tự hiện tại trùng với ký tự trên đỉnh stack
            if stack and stack[-1] == c:
                
                # xóa ký tự trùng (pop)
                stack.pop()
            
            else:
                # nếu không trùng thì thêm vào stack
                stack.append(c)
        
        # ghép lại thành chuỗi kết quả
        return "".join(stack)