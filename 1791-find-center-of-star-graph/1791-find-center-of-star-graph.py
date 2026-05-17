class Solution:
    def findCenter(self, edges):

        # Lấy 2 cạnh đầu tiên của đồ thị
        # Vì trong star graph, node trung tâm sẽ xuất hiện trong tất cả các cạnh
        a, b = edges[0]  # cạnh thứ nhất
        c, d = edges[1]  # cạnh thứ hai

        # Kiểm tra node nào xuất hiện ở cả 2 cạnh
        # Vì center node chắc chắn nằm trong cả edges[0] và edges[1]

        if a == c or a == d:
            # nếu a xuất hiện trong cạnh thứ 2 → a là center
            return a

        # nếu không phải a thì b chắc chắn là center
        return b