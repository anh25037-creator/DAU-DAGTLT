class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        while len(s) > k:

            new_s = ""

            # chia nhóm size k
            for i in range(0, len(s), k):

                group = s[i:i+k]

                # tính tổng chữ số trong group
                total = 0
                for ch in group:
                    total += int(ch)

                # ghép vào chuỗi mới
                new_s += str(total)

            s = new_s

        return s