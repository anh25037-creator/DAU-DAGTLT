#Tìm ký tự được thêm vào trong t.
class Solution:
    def findTheDifference(self, s, t):

        # duyệt từng ký tự trong t
        for char in t:

            # nếu số lần xuất hiện trong t
            # nhiều hơn trong s
            # thì đó là ký tự được thêm
            if t.count(char) > s.count(char):
                return char