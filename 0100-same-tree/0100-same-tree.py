# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        # Nếu cả hai đều rỗng
        if not p and not q:
            return True

        # Nếu một trong hai rỗng
        if not p or not q:
            return False

        # Nếu giá trị khác nhau
        if p.val != q.val:
            return False

        # Kiểm tra cây con trái và phải
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
        