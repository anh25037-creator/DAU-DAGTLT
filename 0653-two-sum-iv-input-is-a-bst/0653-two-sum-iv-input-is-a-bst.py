# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root, k):

        # Set lưu các giá trị đã gặp khi duyệt cây
        seen = set()

        # Hàm DFS duyệt toàn bộ cây
        def dfs(node):
            # Nếu node rỗng → không làm gì
            if not node:
                return False

            # Kiểm tra xem đã tồn tại giá trị "bù"
            # tức là k - node.val đã từng xuất hiện chưa
            if k - node.val in seen:
                return True

            # Nếu chưa tìm thấy cặp, lưu giá trị hiện tại vào set
            seen.add(node.val)

            # Tiếp tục tìm ở cây con trái hoặc phải
            return dfs(node.left) or dfs(node.right)

        # Bắt đầu duyệt từ root
        return dfs(root)