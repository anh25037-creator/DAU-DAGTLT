class Solution:
    def destCity(self, paths):

        # Tạo set lưu các thành phố có đường đi ra
        start = set()

        # Lưu cityA vào set
        for a, b in paths:
            start.add(a)

        # Tìm thành phố không nằm trong start
        for a, b in paths:

            # Nếu cityB không có đường đi ra
            if b not in start:
                return b