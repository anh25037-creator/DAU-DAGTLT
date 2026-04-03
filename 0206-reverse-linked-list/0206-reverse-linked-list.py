# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next   # lưu lại node sau
            curr.next = prev        # đảo chiều
            prev = curr             # cập nhật prev
            curr = next_node        # đi tiếp
        
        return prev
        