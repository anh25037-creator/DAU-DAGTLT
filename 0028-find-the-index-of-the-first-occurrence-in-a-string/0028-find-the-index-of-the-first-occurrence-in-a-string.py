## Tìm vị trí xuất hiện đầu tiên của needle trong haystack
class Solution:
    def strStr(self, haystack, needle):

        # Duyệt từng vị trí có thể bắt đầu
        for i in range(len(haystack) - len(needle) + 1):

            # Cắt chuỗi có độ dài bằng needle
            if haystack[i:i + len(needle)] == needle:

                # Trả về vị trí đầu tiên tìm thấy
                return i

        # Không tìm thấy
        return -1