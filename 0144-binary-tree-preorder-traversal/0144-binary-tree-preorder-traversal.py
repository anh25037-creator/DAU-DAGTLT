# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):

        # danh sách lưu kết quả
        res = []

        # hàm đệ quy DFS
        def dfs(node):

            # nếu node rỗng thì dừng
            if not node:
                return

            # 1. xử lý node hiện tại trước (preorder)
            res.append(node.val)

            # 2. duyệt cây con bên trái
            dfs(node.left)

            # 3. duyệt cây con bên phải
            dfs(node.right)

        # bắt đầu từ root
        dfs(root)

        # trả về kết quả preorder
        return res