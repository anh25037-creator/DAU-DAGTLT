# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):

        if not root:
            return 0

        total = 0

        # Kiểm tra lá bên trái
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        # Đệ quy trái + phải
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total
        