# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def preorder(node):
            if not node:
                return
            result.append(node.val)  # lấy trước
            preorder(node.left)      # trái
            preorder(node.right)     # phải
        
        preorder(root)
        return result
        