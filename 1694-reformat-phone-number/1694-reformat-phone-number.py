class Solution:
    def reformatNumber(self, number):
        digits = ""
        
        # Lấy các chữ số
        for c in number:
            if c.isdigit():
                digits += c

        res = []

        while len(digits) > 0:
            if len(digits) > 4:
                res.append(digits[:3])
                digits = digits[3:]
            elif len(digits) == 4:
                res.append(digits[:2])
                res.append(digits[2:])
                break
            else:
                res.append(digits)
                break

        return "-".join(res)