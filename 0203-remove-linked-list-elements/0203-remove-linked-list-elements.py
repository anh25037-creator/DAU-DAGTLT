# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        # tạo node giả để xử lý trường hợp xóa head
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy  # bắt đầu từ dummy

        # duyệt danh sách
        while curr.next:

            # nếu node kế tiếp cần bị xóa
            if curr.next.val == val:
                # bỏ qua node đó
                curr.next = curr.next.next
            else:
                # nếu không thì đi tiếp
                curr = curr.next

        # trả về head mới (sau dummy)
        return dummy.next