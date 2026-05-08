# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        target = root.val  # giá trị cần so sánh

        def dfs(node):
            if not node:
                return True  # node rỗng thì bỏ qua

            # nếu khác giá trị gốc → không hợp lệ
            if node.val != target:
                return False

            # kiểm tra tiếp trái và phải
            return dfs(node.left) and dfs(node.right)

        return dfs(root)
        