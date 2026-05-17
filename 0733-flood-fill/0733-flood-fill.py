class Solution:
    def floodFill(self, image, sr, sc, color):

        # màu ban đầu tại điểm xuất phát
        old_color = image[sr][sc]

        # nếu màu mới giống màu cũ → không cần đổi
        if old_color == color:
            return image

        # số hàng và cột
        m, n = len(image), len(image[0])

        # DFS để tô màu
        def dfs(r, c):
            # nếu ra ngoài biên → dừng
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            # nếu không đúng màu cũ → dừng
            if image[r][c] != old_color:
                return

            # tô màu mới
            image[r][c] = color

            # lan sang 4 hướng
            dfs(r + 1, c)  # xuống
            dfs(r - 1, c)  # lên
            dfs(r, c + 1)  # phải
            dfs(r, c - 1)  # trái

        # bắt đầu từ điểm xuất phát
        dfs(sr, sc)

        return image