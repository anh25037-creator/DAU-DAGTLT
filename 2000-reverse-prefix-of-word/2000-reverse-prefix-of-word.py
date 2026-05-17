class Solution:
    def reversePrefix(self, word, ch):
        
        # tìm vị trí xuất hiện đầu tiên của ch
        idx = word.find(ch)
        
        # nếu không tìm thấy ch → trả nguyên chuỗi
        if idx == -1:
            return word
        
        # đảo ngược đoạn từ 0 đến idx
        # word[:idx+1] → đoạn cần reverse
        # word[idx+1:] → phần còn lại giữ nguyên
        return word[:idx+1][::-1] + word[idx+1:]