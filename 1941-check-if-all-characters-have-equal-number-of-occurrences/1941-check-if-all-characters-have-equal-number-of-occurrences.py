class Solution:
    def areOccurrencesEqual(self, s):

        # Import Counter để đếm số lần xuất hiện
        from collections import Counter

        # Đếm tần suất của từng ký tự
        freq = Counter(s)

        # Lấy các giá trị tần suất và đưa vào set
        # Nếu tất cả giống nhau thì set chỉ có 1 phần tử
        return len(set(freq.values())) == 1