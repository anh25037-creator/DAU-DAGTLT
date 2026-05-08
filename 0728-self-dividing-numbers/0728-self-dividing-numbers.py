class Solution(object):
    def selfDividingNumbers(self, left, right):

        res = []

        for num in range(left, right + 1):
            s = str(num)

            # nếu có số 0 → bỏ
            if '0' in s:
                continue

            ok = True

            for ch in s:
                d = int(ch)
                if num % d != 0:
                    ok = False
                    break

            if ok:
                res.append(num)

        return res