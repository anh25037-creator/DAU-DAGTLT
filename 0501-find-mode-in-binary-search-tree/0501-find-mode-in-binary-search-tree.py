# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root):

        count = {}
        
        # DFS duyệt cây
        def dfs(node):
            if not node:
                return
            
            count[node.val] = count.get(node.val, 0) + 1
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # Tần suất lớn nhất
        maxFreq = max(count.values())

        # Lấy các mode
        res = []

        for key in count:
            if count[key] == maxFreq:
                res.append(key)

        return res