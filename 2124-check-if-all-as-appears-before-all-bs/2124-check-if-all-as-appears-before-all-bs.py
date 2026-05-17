class Solution:
    def checkString(self, s):

        # Duyệt từng cặp ký tự liền nhau
        for i in range(len(s) - 1):

            # Nếu gặp "ba"
            if s[i] == 'b' and s[i + 1] == 'a':

                # Sai điều kiện
                return False

        # Nếu không có "ba"
        return True