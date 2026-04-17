# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        result = []
        
        def postorder(node):
            if not node:
                return
            postorder(node.left)      # trái
            postorder(node.right)     # phải
            result.append(node.val)   # lấy sau
        
        postorder(root)
        return result