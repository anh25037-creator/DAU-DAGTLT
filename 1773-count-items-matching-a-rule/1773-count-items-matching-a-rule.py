class Solution:
    def countMatches(self, items, ruleKey, ruleValue):

        # Biến đếm số item thỏa điều kiện
        count = 0

        # Xác định vị trí cần kiểm tra
        if ruleKey == "type":
            index = 0

        elif ruleKey == "color":
            index = 1

        else:
            index = 2

        # Duyệt từng item
        for item in items:

            # Nếu giá trị tại vị trí index bằng ruleValue
            if item[index] == ruleValue:
                count += 1

        # Trả về kết quả
        return count