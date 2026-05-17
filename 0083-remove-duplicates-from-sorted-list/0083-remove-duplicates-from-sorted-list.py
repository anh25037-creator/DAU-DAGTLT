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

class Solution:
    def deleteDuplicates(self, head):
        # con trỏ curr dùng để duyệt danh sách liên kết
        curr = head

        # duyệt đến khi hết list hoặc chỉ còn 1 node
        while curr and curr.next:

            # nếu giá trị node hiện tại bằng node kế tiếp
            if curr.val == curr.next.val:
                # bỏ node trùng bằng cách nối bỏ qua node kế tiếp
                curr.next = curr.next.next
            else:
                # nếu không trùng thì chuyển sang node tiếp theo
                curr = curr.next

        # trả về head của danh sách đã xử lý
        return head