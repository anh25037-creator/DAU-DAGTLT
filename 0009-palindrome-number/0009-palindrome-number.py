class Solution:
    def isPalindrome(self, x):
        # chuyển số nguyên x sang chuỗi để dễ xử lý
        s = str(x)

        # s[::-1] là cách đảo ngược chuỗi trong Python
        # ví dụ: "121" → "121", "123" → "321"

        # so sánh chuỗi gốc với chuỗi đảo ngược
        # nếu giống nhau → là palindrome
        return s == s[::-1]