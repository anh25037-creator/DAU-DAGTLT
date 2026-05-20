#Kiểm tra xem hai chuỗi có phải hoán vị của nhau hay không.
class Solution:
    def isAnagram(self, s, t):

        # sorted() dùng để sắp xếp ký tự theo alphabet
        # Ví dụ:
        # sorted("rat") -> ['a','r','t']
        # sorted("tar") -> ['a','r','t']

        # Nếu sau khi sắp xếp mà giống nhau
        # => hai chuỗi có cùng ký tự và cùng số lượng ký tự
        # => là anagram
        return sorted(s) == sorted(t)