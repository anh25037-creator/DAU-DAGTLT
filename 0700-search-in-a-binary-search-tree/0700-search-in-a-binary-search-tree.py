# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # Hàm tìm node có giá trị val trong BST
    def searchBST(self, root, val):

        # Nếu cây rỗng hoặc tìm thấy node cần tìm
        if root == None or root.val == val:
            return root

        # Nếu val nhỏ hơn node hiện tại
        # => tìm tiếp bên trái
        if val < root.val:
            return self.searchBST(root.left, val)

        # Ngược lại tìm bên phải
        return self.searchBST(root.right, val)
        