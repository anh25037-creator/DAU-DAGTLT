class Solution:
    def majorityElement(self, nums):
        # candidate: phần tử đang được xem là "ứng viên"
        candidate = None

        # count: số phiếu ủng hộ ứng viên hiện tại
        count = 0

        # duyệt từng phần tử trong mảng
        for num in nums:

            # nếu count = 0 → chưa có ứng viên hoặc ứng viên bị loại
            # => chọn số hiện tại làm ứng viên mới
            if count == 0:
                candidate = num

            # nếu số hiện tại giống ứng viên → tăng phiếu
            if num == candidate:
                count += 1
            else:
                # khác ứng viên → giảm phiếu (triệt tiêu nhau)
                count -= 1

        # sau khi duyệt xong, candidate còn lại là majority element
        return candidate