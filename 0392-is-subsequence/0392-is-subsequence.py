#Có phải chuỗi con theo thứ tự hay không.
class Solution:
    def isSubsequence(self, s, t):

        # i dùng để duyệt chuỗi s
        i = 0

        # j dùng để duyệt chuỗi t
        j = 0

        # lặp khi:
        # - vẫn còn ký tự trong s
        # - và vẫn còn ký tự trong t
        while i < len(s) and j < len(t):

            # nếu ký tự hiện tại của s
            # giống ký tự hiện tại của t
            if s[i] == t[j]:

                # chuyển sang ký tự tiếp theo của s
                i += 1

            # luôn chuyển sang ký tự tiếp theo của t
            j += 1

        # nếu i đi hết chuỗi s
        # nghĩa là đã tìm đủ các ký tự của s theo đúng thứ tự
        return i == len(s)