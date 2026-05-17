class Solution:
    def wordPattern(self, pattern, s):

        # Tách chuỗi thành các từ
        words = s.split()

        # Nếu số ký tự và số từ khác nhau
        if len(pattern) != len(words):
            return False

        # Dictionary:
        # ký tự -> từ
        charToWord = {}

        # Dictionary:
        # từ -> ký tự
        wordToChar = {}

        # Duyệt từng vị trí
        for i in range(len(pattern)):

            ch = pattern[i]
            word = words[i]

            # Nếu ký tự đã tồn tại
            if ch in charToWord:

                # Kiểm tra có khớp từ cũ không
                if charToWord[ch] != word:
                    return False

            else:
                # Gán ký tự -> từ
                charToWord[ch] = word

            # Nếu từ đã tồn tại
            if word in wordToChar:

                # Kiểm tra có khớp ký tự cũ không
                if wordToChar[word] != ch:
                    return False

            else:
                # Gán từ -> ký tự
                wordToChar[word] = ch

        return True