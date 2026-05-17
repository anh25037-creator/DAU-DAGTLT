class Solution:
    def capitalizeTitle(self, title):

        # Tách chuỗi thành từng từ
        words = title.split()

        # Danh sách lưu kết quả
        result = []

        # Duyệt từng từ
        for word in words:

            # Nếu độ dài <= 2
            if len(word) <= 2:

                # Đổi toàn bộ thành chữ thường
                result.append(word.lower())

            else:
                # Chữ đầu viết hoa
                # Các chữ còn lại viết thường
                result.append(word[0].upper() + word[1:].lower())

        # Ghép các từ lại thành chuỗi
        return " ".join(result)