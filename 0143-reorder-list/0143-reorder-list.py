# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # 1. tìm middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. đảo nửa sau
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 3. trộn 2 list
        first = head
        second = prev
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2