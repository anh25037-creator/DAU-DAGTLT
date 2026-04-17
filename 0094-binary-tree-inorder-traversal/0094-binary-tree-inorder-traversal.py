# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)      # đi trái
            result.append(node.val) # lấy giá trị
            inorder(node.right)     # đi phải
        
        inorder(root)
        return result
        