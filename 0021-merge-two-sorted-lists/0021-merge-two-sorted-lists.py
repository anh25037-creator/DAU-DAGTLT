class Solution:
    def mergeTwoLists(self, list1, list2):
        # node giả giúp dễ thao tác
        dummy = ListNode(0)
        curr = dummy

        # duyệt khi cả 2 list còn node
        while list1 and list2:
            # chọn node có giá trị nhỏ hơn
            if list1.val <= list2.val:
                curr.next = list1      # nối list1 vào kết quả
                list1 = list1.next     # tiến list1
            else:
                curr.next = list2      # nối list2 vào kết quả
                list2 = list2.next     # tiến list2

            curr = curr.next           # tiến con trỏ kết quả

        # nối phần còn lại (vì 1 trong 2 list có thể chưa hết)
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        # bỏ node giả, trả về head thật
        return dummy.next