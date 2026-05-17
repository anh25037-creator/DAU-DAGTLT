class Solution:
    def findFinalValue(self, nums, original):

        # Lặp vô hạn cho đến khi gặp break
        while True:

            # Nếu original có trong nums
            if original in nums:

                # Nhân đôi original
                original *= 2

            else:
                # Nếu không có thì dừng
                break

        # Trả về giá trị cuối cùng
        return original