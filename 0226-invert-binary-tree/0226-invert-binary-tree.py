# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):

        # nếu cây rỗng thì trả về None
        if not root:
            return None

        # đổi chỗ 2 cây con trái và phải
        root.left, root.right = root.right, root.left

        # đệ quy đảo cây con bên trái
        self.invertTree(root.left)

        # đệ quy đảo cây con bên phải
        self.invertTree(root.right)

        # trả về root sau khi đã đảo
        return root
        