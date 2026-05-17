class Solution:
    def targetIndices(self, nums, target):

        # Sắp xếp mảng tăng dần
        nums.sort()

        # Danh sách lưu các vị trí có giá trị target
        result = []

        # Duyệt từng vị trí trong mảng
        for i in range(len(nums)):

            # Nếu phần tử tại vị trí i bằng target
            if nums[i] == target:

                # Thêm index vào result
                result.append(i)

        # Trả về danh sách kết quả
        return result