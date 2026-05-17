# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):

        # nếu cây rỗng → độ sâu = 0
        if not root:
            return 0

        # tính độ sâu cây con bên trái
        left_depth = self.maxDepth(root.left)

        # tính độ sâu cây con bên phải
        right_depth = self.maxDepth(root.right)

        # lấy đường dài nhất + 1 (node hiện tại)
        return 1 + max(left_depth, right_depth)