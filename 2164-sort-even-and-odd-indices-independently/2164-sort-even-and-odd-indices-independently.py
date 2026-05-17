class Solution:
    def sortEvenOdd(self, nums):

        # Lấy các phần tử ở vị trí chẵn
        even = []

        # Lấy các phần tử ở vị trí lẻ
        odd = []

        # Duyệt từng vị trí
        for i in range(len(nums)):

            # Nếu là vị trí chẵn
            if i % 2 == 0:
                even.append(nums[i])

            # Nếu là vị trí lẻ
            else:
                odd.append(nums[i])

        # Sắp xếp vị trí chẵn tăng dần
        even.sort()

        # Sắp xếp vị trí lẻ giảm dần
        odd.sort(reverse=True)

        # Tạo biến để duyệt even và odd
        e = 0
        o = 0

        # Gán lại giá trị vào nums
        for i in range(len(nums)):

            # Nếu là vị trí chẵn
            if i % 2 == 0:
                nums[i] = even[e]
                e += 1

            # Nếu là vị trí lẻ
            else:
                nums[i] = odd[o]
                o += 1

        # Trả về kết quả
        return nums