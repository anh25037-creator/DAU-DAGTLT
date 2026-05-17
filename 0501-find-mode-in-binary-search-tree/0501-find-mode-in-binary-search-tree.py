# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root):

        # Dictionary dùng để lưu:
        # key = giá trị node
        # value = số lần xuất hiện
        count = {}
        
        # Hàm DFS để duyệt toàn bộ cây
        def dfs(node):
            # Nếu node rỗng thì dừng
            if not node:
                return
            
            # Tăng tần suất của node.val lên 1
            count[node.val] = count.get(node.val, 0) + 1
            
            # Duyệt tiếp cây con bên trái
            dfs(node.left)

            # Duyệt tiếp cây con bên phải
            dfs(node.right)

        # Bắt đầu duyệt từ root
        dfs(root)

        # Tìm giá trị có tần suất lớn nhất
        maxFreq = max(count.values())

        # Danh sách kết quả (các mode)
        res = []

        # Duyệt qua dictionary để lấy các giá trị có tần suất = maxFreq
        for key in count:
            if count[key] == maxFreq:
                res.append(key)

        return res