# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # lấy giá trị của node trái và phải
        left_val = root.left.val
        right_val = root.right.val

        # kiểm tra tổng hai con có bằng root không
        return root.val == left_val + right_val