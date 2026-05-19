class Solution:
    def longestCommonPrefix(self, strs):
        
        # Nếu danh sách rỗng → không có prefix
        if not strs:
            return ""

        # Sắp xếp danh sách theo thứ tự từ điển
        strs.sort()

        # Lấy chuỗi nhỏ nhất (đầu danh sách sau sort)
        first = strs[0]

        # Lấy chuỗi lớn nhất (cuối danh sách sau sort)
        last = strs[-1]

        # Biến đếm vị trí ký tự đang so sánh
        i = 0

        # So sánh từng ký tự giữa first và last
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1  # nếu giống nhau thì tăng i để kiểm tra ký tự tiếp theo

        # Cắt chuỗi từ đầu đến vị trí i → chính là prefix chung
        return first[:i]