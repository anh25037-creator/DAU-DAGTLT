# Kiểm tra xem ransomNote có thể tạo từ magazine hay không
class Solution:

    def canConstruct(self, ransomNote, magazine):

        # Dictionary dùng để lưu:
        # ký tự : số lần xuất hiện
        count = {}

        # Duyệt từng ký tự trong magazine
        for ch in magazine:

            # Nếu ký tự đã tồn tại trong dictionary
            if ch in count:

                # Tăng số lần xuất hiện lên 1
                count[ch] += 1

            # Nếu ký tự chưa tồn tại
            else:

                # Thêm ký tự vào dictionary
                # với số lượng ban đầu là 1
                count[ch] = 1

        # Duyệt từng ký tự trong ransomNote
        for ch in ransomNote:

            # Nếu ký tự không tồn tại trong dictionary
            # hoặc số lượng còn lại bằng 0
            if ch not in count or count[ch] == 0:

                # Không thể tạo ransomNote
                return False

            # Dùng 1 ký tự
            # nên giảm số lượng đi 1
            count[ch] -= 1

        # Nếu duyệt hết mà không lỗi
        # nghĩa là tạo được ransomNote
        return True