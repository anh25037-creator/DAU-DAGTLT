class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # dictionary để lưu: số -> vị trí xuất hiện gần nhất
        last_index = {}

        # duyệt mảng với cả chỉ số i và giá trị num
        for i, num in enumerate(nums):

            # nếu số này đã từng xuất hiện trước đó
            if num in last_index:

                # kiểm tra khoảng cách giữa 2 lần xuất hiện
                if i - last_index[num] <= k:
                    return True  # thỏa điều kiện -> trả về True

            # cập nhật lại vị trí mới nhất của num
            last_index[num] = i

        # duyệt xong không tìm thấy cặp thỏa điều kiện
        return False