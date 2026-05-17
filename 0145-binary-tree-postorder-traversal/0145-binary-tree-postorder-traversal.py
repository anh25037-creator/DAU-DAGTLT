# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):

        # danh sách lưu kết quả
        res = []

        # hàm đệ quy DFS
        def dfs(node):

            # nếu node rỗng thì dừng lại
            if not node:
                return

            # 1. duyệt toàn bộ cây con bên trái trước
            dfs(node.left)

            # 2. sau đó duyệt cây con bên phải
            dfs(node.right)

            # 3. cuối cùng mới xử lý node hiện tại (postorder)
            res.append(node.val)

        # bắt đầu từ root
        dfs(root)

        # trả về kết quả
        return res