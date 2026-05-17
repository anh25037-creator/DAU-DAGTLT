class Solution:
    def lemonadeChange(self, bills):

        # Số tờ 5$ hiện có
        five = 0

        # Số tờ 10$ hiện có
        ten = 0

        # Duyệt từng khách hàng
        for bill in bills:

            # Nếu khách trả 5$
            if bill == 5:
                five += 1

            # Nếu khách trả 10$
            elif bill == 10:

                # Cần thối lại 5$
                if five == 0:
                    return False

                five -= 1
                ten += 1

            # Nếu khách trả 20$
            else:

                # Ưu tiên dùng 10$ + 5$
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                # Nếu không có 10$ thì dùng 3 tờ 5$
                elif five >= 3:
                    five -= 3

                # Không đủ tiền thối
                else:
                    return False

        # Thối được cho tất cả khách
        return True