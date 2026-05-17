class Solution:
    def mostCommonWord(self, paragraph, banned):

        # Chuyển tất cả ký tự thành chữ thường
        paragraph = paragraph.lower()

        # Thay các dấu câu bằng khoảng trắng
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        # Tách các từ
        words = paragraph.split()

        # Chuyển banned thành set để tìm nhanh hơn
        banned_set = set(banned)

        # Dictionary đếm số lần xuất hiện
        count = {}

        # Đếm tần suất các từ không bị cấm
        for word in words:

            # Nếu từ không nằm trong banned
            if word not in banned_set:

                # Tăng số lần xuất hiện
                count[word] = count.get(word, 0) + 1

        # Tìm từ xuất hiện nhiều nhất
        answer = ""
        max_count = 0

        for word in count:

            if count[word] > max_count:
                max_count = count[word]
                answer = word

        # Trả về kết quả
        return answer