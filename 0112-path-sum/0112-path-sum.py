# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):

        # nếu cây rỗng → không có đường đi nào
        if not root:
            return False

        # nếu gặp node lá (không có con trái và phải)
        if not root.left and not root.right:
            # kiểm tra xem giá trị còn lại có đúng bằng node này không
            return targetSum == root.val

        # giảm targetSum đi giá trị của node hiện tại
        targetSum -= root.val

        # kiểm tra đệ quy:
        # chỉ cần 1 trong 2 nhánh có đường đi hợp lệ là True
        return (
            self.hasPathSum(root.left, targetSum) or
            self.hasPathSum(root.right, targetSum)
        )