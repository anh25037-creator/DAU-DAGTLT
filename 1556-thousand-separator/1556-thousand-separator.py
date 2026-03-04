class Solution:
    def thousandSeparator(self, n):
        return format(n, ",").replace(",", ".")