# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):

        # nếu cả hai cây đều rỗng → giống nhau
        if not p and not q:
            return True

        # nếu chỉ một trong hai cây rỗng → khác nhau
        if not p or not q:
            return False

        # nếu giá trị tại node hiện tại khác nhau → khác nhau
        if p.val != q.val:
            return False

        # kiểm tra đệ quy:
        # so sánh cây con bên trái và bên phải
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )