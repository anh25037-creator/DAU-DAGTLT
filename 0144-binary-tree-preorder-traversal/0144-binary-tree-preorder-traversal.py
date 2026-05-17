# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        res = []

        def dfs(node):
            # nếu node rỗng thì dừng
            if not node:
                return

            # 1. thăm node hiện tại trước
            res.append(node.val)

            # 2. duyệt cây con bên trái
            dfs(node.left)

            # 3. duyệt cây con bên phải
            dfs(node.right)

        dfs(root)
        return res