# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root):

        # danh sách lưu tất cả các đường đi từ root đến leaf
        res = []

        # hàm DFS: duyệt cây và xây dựng đường đi
        def dfs(node, path):

            # nếu node rỗng thì dừng
            if not node:
                return

            # thêm giá trị node hiện tại vào chuỗi path
            path += str(node.val)

            # nếu là node lá (không có con trái và phải)
            if not node.left and not node.right:
                # lưu đường đi hoàn chỉnh vào kết quả
                res.append(path)
                return

            # nếu chưa phải leaf thì thêm ký hiệu "->"
            path += "->"

            # tiếp tục duyệt sang cây con bên trái
            dfs(node.left, path)

            # tiếp tục duyệt sang cây con bên phải
            dfs(node.right, path)

        # bắt đầu DFS từ root với path rỗng
        dfs(root, "")

        # trả về danh sách các đường đi
        return res
        