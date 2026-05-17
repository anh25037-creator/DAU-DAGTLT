class Solution:
    def countWords(self, words1, words2):

        # Dictionary đếm số lần xuất hiện trong words1
        count1 = {}

        # Dictionary đếm số lần xuất hiện trong words2
        count2 = {}

        # Đếm số lần xuất hiện của từng từ trong words1
        for word in words1:

            if word in count1:
                count1[word] += 1
            else:
                count1[word] = 1

        # Đếm số lần xuất hiện của từng từ trong words2
        for word in words2:

            if word in count2:
                count2[word] += 1
            else:
                count2[word] = 1

        # Biến đếm số từ xuất hiện đúng 1 lần ở cả 2 mảng
        ans = 0

        # Duyệt từng từ trong words1
        for word in count1:

            # Kiểm tra:
            # - xuất hiện đúng 1 lần trong words1
            # - có trong words2
            # - xuất hiện đúng 1 lần trong words2
            if count1[word] == 1 and word in count2 and count2[word] == 1:

                # Tăng kết quả
                ans += 1

        # Trả về kết quả
        return ans