#tìm tiền tố chung dài nhất giữa tất cả các chuỗi trong mảng.
class Solution:
    def longestCommonPrefix(self, strs):

        # Kiểm tra:
        # nếu mảng rỗng thì không có prefix
        if not strs:
            return ""

        # Sắp xếp mảng theo thứ tự từ điển
        # Ví dụ:
        # ["flower","flow","flight"]
        # ->
        # ["flight","flow","flower"]
        strs.sort()

        # Lấy chuỗi đầu tiên sau khi sort
        first = strs[0]

        # Lấy chuỗi cuối cùng sau khi sort
        last = strs[-1]

        # Biến dùng để lưu tiền tố chung
        prefix = ""

        # Duyệt từng vị trí ký tự
        # min(...) để tránh vượt quá độ dài chuỗi ngắn hơn
        for i in range(min(len(first), len(last))):

            # Nếu ký tự tại vị trí i giống nhau
            if first[i] == last[i]:

                # Thêm ký tự đó vào prefix
                prefix += first[i]

            # Nếu khác nhau
            else:

                # Dừng vòng lặp
                break

        # Trả về tiền tố chung dài nhất
        return prefix