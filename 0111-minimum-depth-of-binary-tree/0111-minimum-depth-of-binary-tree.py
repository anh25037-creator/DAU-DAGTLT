class Solution:
    def minDepth(self, root):

        # nếu cây rỗng → độ sâu = 0
        if not root:
            return 0

        # nếu không có cây con bên trái
        # thì bắt buộc phải đi xuống bên phải
        # (không được tính min vì bên trái không tồn tại)
        if not root.left:
            return 1 + self.minDepth(root.right)

        # nếu không có cây con bên phải
        # thì bắt buộc đi xuống bên trái
        if not root.right:
            return 1 + self.minDepth(root.left)

        # nếu có cả 2 cây con
        # chọn đường đi ngắn nhất giữa trái và phải
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )