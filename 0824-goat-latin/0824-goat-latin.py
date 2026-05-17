class Solution:
    def toGoatLatin(self, sentence):

        # Các nguyên âm
        vowels = "aeiouAEIOU"

        # Tách câu thành từng từ
        words = sentence.split()

        # Mảng kết quả
        result = []

        # Duyệt từng từ
        for i in range(len(words)):

            word = words[i]

            # Nếu bắt đầu bằng nguyên âm
            if word[0] in vowels:

                # Thêm "ma"
                newWord = word + "ma"

            else:
                # Chuyển chữ đầu xuống cuối rồi thêm "ma"
                newWord = word[1:] + word[0] + "ma"

            # Thêm số lượng 'a' theo vị trí
            newWord += "a" * (i + 1)

            # Thêm vào kết quả
            result.append(newWord)

        # Ghép các từ lại thành câu
        return " ".join(result)