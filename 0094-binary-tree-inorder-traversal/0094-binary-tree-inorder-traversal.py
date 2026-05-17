# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # danh sách lưu kết quả duyệt inorder
        res = []

        # hàm đệ quy DFS để duyệt cây
        def dfs(node):
            # nếu node rỗng thì dừng lại
            if not node:
                return

            # 1. duyệt toàn bộ cây con bên trái trước
            dfs(node.left)

            # 2. sau khi duyệt trái xong, thêm node hiện tại vào kết quả
            res.append(node.val)

            # 3. duyệt tiếp cây con bên phải
            dfs(node.right)

        # bắt đầu duyệt từ gốc cây
        dfs(root)

        # trả về danh sách kết quả inorder
        return res