# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):

        # Hàm kiểm tra 2 cây có giống nhau không
        def sameTree(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        # Nếu root rỗng
        if not root:
            return False

        # Nếu cây hiện tại giống subRoot
        if sameTree(root, subRoot):
            return True

        # Kiểm tra tiếp bên trái hoặc bên phải
        return self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)