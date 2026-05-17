# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root):

        # Giá trị chuẩn của cả cây (lấy từ root)
        target = root.val

        # Hàm DFS để kiểm tra toàn bộ cây
        def dfs(node):

            # Nếu node rỗng → không vi phạm gì
            if not node:
                return True

            # Nếu giá trị node khác giá trị chuẩn → không phải uni-valued
            if node.val != target:
                return False

            # Kiểm tra tiếp cây con bên trái và bên phải
            return dfs(node.left) and dfs(node.right)

        # Bắt đầu kiểm tra từ root
        return dfs(root)