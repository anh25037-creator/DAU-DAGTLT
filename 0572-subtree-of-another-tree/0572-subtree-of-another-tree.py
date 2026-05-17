# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):

        # Hàm so sánh 2 cây có giống hệt nhau không
        def isSameTree(p, q):
            # Nếu cả hai đều rỗng → giống nhau
            if not p and not q:
                return True
            
            # Nếu một cây rỗng, một cây không → khác nhau
            if not p or not q:
                return False
            
            # Nếu giá trị khác nhau → không giống
            if p.val != q.val:
                return False
            
            # Kiểm tra tiếp cây con bên trái và bên phải
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # Hàm duyệt từng node của root
        def dfs(node):
            # Nếu node rỗng → không tìm thấy
            if not node:
                return False
            
            # Nếu cây tại node hiện tại giống subRoot → trả về True
            if isSameTree(node, subRoot):
                return True
            
            # Nếu không giống → tiếp tục tìm ở cây trái hoặc cây phải
            return dfs(node.left) or dfs(node.right)

        # Bắt đầu duyệt từ root
        return dfs(root)