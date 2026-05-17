# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):

        # Nếu cây rỗng thì tổng = 0
        if not root:
            return 0

        total = 0

        # Kiểm tra nếu node con bên trái tồn tại
        # và nó là 1 lá (không có con trái + phải)
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        # Đệ quy sang cả cây con bên trái
        total += self.sumOfLeftLeaves(root.left)

        # Đệ quy sang cả cây con bên phải
        total += self.sumOfLeftLeaves(root.right)

        return total
        