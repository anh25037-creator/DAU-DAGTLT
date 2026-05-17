class Solution:
    def areOccurrencesEqual(self, s):

        # Dictionary dùng để đếm số lần xuất hiện
        count = {}

        # Duyệt từng ký tự trong chuỗi
        for ch in s:

            # Nếu ký tự đã có trong dictionary
            if ch in count:
                count[ch] += 1

            # Nếu chưa có thì gán bằng 1
            else:
                count[ch] = 1

        # Lấy số lần xuất hiện đầu tiên
        first = list(count.values())[0]

        # Kiểm tra các tần suất còn lại
        for value in count.values():

            # Nếu có tần suất khác first
            if value != first:
                return False

        # Nếu tất cả bằng nhau
        return True