# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkTree(self, root):

        # Lấy giá trị của node con bên trái
        left_val = root.left.val

        # Lấy giá trị của node con bên phải
        right_val = root.right.val

        # Kiểm tra:
        # nếu giá trị root bằng tổng 2 node con
        # thì trả về True, ngược lại False
        return root.val == left_val + right_val