class Solution:
    def distributeCandies(self, candyType):

        # Tìm số loại kẹo khác nhau
        uniqueTypes = len(set(candyType))

        # Số lượng kẹo Alice được ăn
        canEat = len(candyType) // 2

        # Alice chỉ có thể ăn tối đa:
        # - số loại khác nhau
        # hoặc
        # - n / 2 viên kẹo
        return min(uniqueTypes, canEat)