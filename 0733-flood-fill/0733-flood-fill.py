class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        rows = len(image)
        cols = len(image[0])

        original = image[sr][sc]

        # nếu màu mới giống màu cũ
        if original == color:
            return image

        def dfs(r, c):

            # ngoài biên
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # khác màu gốc
            if image[r][c] != original:
                return

            # đổi màu
            image[r][c] = color

            # 4 hướng
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image