class Solution:
    def mostWordsFound(self, sentences):

        # Biến lưu số lượng từ lớn nhất
        max_words = 0

        # Duyệt từng câu
        for sentence in sentences:

            # Tách câu thành các từ
            words = sentence.split()

            # Đếm số từ trong câu
            count = len(words)

            # Cập nhật giá trị lớn nhất
            max_words = max(max_words, count)

        # Trả về kết quả
        return max_words