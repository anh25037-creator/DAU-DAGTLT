# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # giá trị của node
#         self.left = left        # con trái
#         self.right = right      # con phải

class Solution(object):

    def leafSimilar(self, root1, root2):
        """
        Kiểm tra 2 cây có dãy lá (leaf) giống nhau không
        """

        # Hàm phụ: lấy danh sách các lá của 1 cây
        def get_leaves(root):
            leaves = []  # mảng lưu các node lá

            # DFS duyệt cây
            def dfs(node):
                if not node:
                    return  # gặp node rỗng thì dừng

                # nếu node hiện tại là lá (không có con)
                if not node.left and not node.right:
                    leaves.append(node.val)  # thêm giá trị vào danh sách lá
                    return  # dừng nhánh này

                # tiếp tục duyệt trái và phải
                dfs(node.left)
                dfs(node.right)

            dfs(root)       # bắt đầu duyệt từ gốc
            return leaves   # trả về danh sách lá

        # so sánh 2 danh sách lá của 2 cây
        return get_leaves(root1) == get_leaves(root2)
        