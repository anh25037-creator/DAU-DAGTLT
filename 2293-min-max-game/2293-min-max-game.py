class Solution:
    def minMaxGame(self, nums):

        # Lặp lại quá trình cho đến khi mảng còn 1 phần tử
        while len(nums) > 1:

            # Mảng mới sau mỗi lần xử lý cặp phần tử
            newNums = []

            # Duyệt theo từng cặp (2*i, 2*i+1)
            # Vì mỗi vòng sẽ giảm còn n/2 phần tử
            for i in range(len(nums) // 2):

                # Nếu index i của newNums là chẵn
                # → lấy min của cặp tương ứng trong nums
                if i % 2 == 0:
                    newNums.append(min(nums[2*i], nums[2*i + 1]))

                # Nếu index i là lẻ
                # → lấy max của cặp tương ứng trong nums
                else:
                    newNums.append(max(nums[2*i], nums[2*i + 1]))

            # Cập nhật nums thành mảng mới
            nums = newNums

        # Khi chỉ còn 1 phần tử → trả kết quả
        return nums[0]